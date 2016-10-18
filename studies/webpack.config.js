

module.exports = {

  entry: './assets/javascripts/test.js',

  output: {
    path: './static/studies',
    filename: 'test.js',
  },

  module: {
    loaders: [

      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },

      {
        test: /\.scss$/,
        loaders: [
          'style',
          'css?sourceMap',
          'sass?sourceMap',
        ],
      },

    ]
  },

  devtool: 'source-map',

};
