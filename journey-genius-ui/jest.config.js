// jest.config.js

module.exports = {
    moduleNameMapper: {
      '^@/(.*)$': '<rootDir>/src/$1',
    },
    transform: {
      '^.+\\.vue$': 'vue-jest',
      '^.+\\.js$': 'babel-jest', // You may need to add this line if you're using ES modules in your tests
    },
  };
  