import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/** @type {import('next').NextConfig} */
const nextConfig = {
  future: {
    webpack5: true,
  },
  css: {
    sourceMap: true,
  },
  image: {
    formats: ['image/avif', 'image/webp'],
  },
  env: {
    customKey: process.env.CUSTOM_VALUE,
  },
  webpack: (config) => {
    config.resolve.alias['@'] = path.resolve(__dirname);
    return config;
  },
};

export default nextConfig;
