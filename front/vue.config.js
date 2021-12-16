module.exports = {
    publicPath: '/Trello-Sierra/',

    devServer: {
      proxy: 'http://localhost:5000'
    },

    transpileDependencies: [
      'vuetify'
    ]
}
