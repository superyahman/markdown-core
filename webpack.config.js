const path = require('path')

const loaders = [
  {
    test: /\.json$/,
    loader: 'json-loader'
  },
  {
    test: /\.js$/,
    loader: 'babel-loader',
    exclude: /node_modules/,
    query: {
      presets: [
        ['env', {
          'targets': {
            'browsers': ['last 2 versions']
          }
        }]
      ]
    }
  },
  {
    test: /\.css$/,
    loader: 'style-loader!css-loader'
  },
  {
    test: /\.(ttf|eot|svg|woff2?)(\?v=.+?)?$/,
    loader: 'url-loader?limit=1000000'
  }
]

module.exports = [
  {
    entry: {
      'markdown-core': './markdown-core-browser.js'
    },
    output: {
      path: path.join(__dirname, 'dist'),
      filename: '[name].min.js',
      library: 'mdc',
      libraryTarget: 'umd'
    },
    module: { loaders }
  },
  {
    entry: {
      'index': './test/index.js'
    },
    output: {
      path: path.join(__dirname, 'test'),
      filename: '[name].bundle.js'
    },
    module: { loaders }
  }
]