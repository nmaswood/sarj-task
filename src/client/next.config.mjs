// Log environment variables during build
console.log('Building with environment variables:', {
  NEXT_PUBLIC_BASE_URL: process.env.NEXT_PUBLIC_BASE_URL,
  NODE_ENV: process.env.NODE_ENV
});

/** @type {import('next').NextConfig} */
const nextConfig = {
  // Explicitly set environment variables
  env: {
    NEXT_PUBLIC_BASE_URL: process.env.NEXT_PUBLIC_BASE_URL || 'http://localhost:3000',
  },
  // Log environment during build
  onDemandEntries: {
    // Add build-time logging
    webpack: (config, { buildId, dev, isServer}) => {
      console.log('Webpack build environment:', {
        NEXT_PUBLIC_BASE_URL: process.env.NEXT_PUBLIC_BASE_URL,
        buildId,
        dev,
        isServer
      });
      
      config.resolve.alias['@'] = path.resolve(__dirname);
      return config;
    },
  },
};

export default nextConfig;
