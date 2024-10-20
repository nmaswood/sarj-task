# app/services/book_service.py
import aiohttp
from bs4 import BeautifulSoup
from app.models import Book

async def get_book(book_id: int):
    # Check if book exists in database
    book = await Book.get(book_id)
    if book:
        return book

    # If not, fetch from Project Gutenberg
    content_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    metadata_url = f"https://www.gutenberg.org/ebooks/{book_id}"

    async with aiohttp.ClientSession() as session:
        # Fetch content
        async with session.get(content_url) as content_response:
            if content_response.status == 200:
                content = await content_response.text()
            else:
                content = "Content not available"

        # Fetch metadata
        async with session.get(metadata_url) as metadata_response:
            if metadata_response.status == 200:
                html_content = await metadata_response.text()
                metadata = extract_metadata(html_content)
            else:
                metadata = {}

    # Save book to database
    book = await Book.create(id=book_id, content=content, metadata=metadata)
    return book

def extract_metadata(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    metadata = {}

    # Extract title
    title_tag = soup.find('h1', itemprop='name')
    if title_tag:
        metadata['title'] = title_tag.text.strip()

    # Extract author(s)
    author_tags = soup.find_all('a', rel='marcrel:aut')
    metadata['authors'] = [author.text.strip() for author in author_tags]

    # Extract language
    language_tag = soup.find('tr', attrs={'property': 'dcterms:language'})
    if language_tag:
        metadata['language'] = language_tag.find('td').text.strip()

    # Extract release date
    release_date_tag = soup.find('tr', attrs={'property': 'dcterms:issued'})
    if release_date_tag:
        metadata['release_date'] = release_date_tag.find('td').text.strip()

    # Extract download count
    downloads_tag = soup.find('th', string='Downloads')
    if downloads_tag:
        metadata['downloads'] = downloads_tag.find_next('td').text.strip()

    return metadata

async def get_saved_books(user):
    return await Book.filter(user=user)

async def search_books(query: str):
    # Implement search logic
    pass
