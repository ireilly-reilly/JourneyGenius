const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  // overlay: false,

  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  },
  devServer: {
    proxy: {
      '/api': {
        target: 'https://maps.googleapis.com',
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      },
    },
  },
})
