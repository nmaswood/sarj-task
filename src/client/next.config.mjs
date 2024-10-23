/** @type {import('next').NextConfig} */
const nextConfig = {
  // Enable module aliasing
  moduleDirectories: ['node_modules', 'app'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/$1',
  },
  // Optional: Enable absolute imports for TypeScript
  experimental: {
    esmExternals: 'loose',
  },
  // Optional: Specify Webpack configuration (for advanced use cases)
  // webpack: (config) => config,
};

export default nextConfig;
