module.exports = {
    publicPath: '/Better-Trello/',

    devServer: {
      proxy: 'http://localhost:5000'
    },

    transpileDependencies: [
      'vuetify'
    ]
}
