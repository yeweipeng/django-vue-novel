var path = require('path')
var webpack = require('webpack')

var HtmlWebpackPlugin = require('html-webpack-plugin')
,   CleanPlugin = require('clean-webpack-plugin')
,   BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin

module.exports = {
  entry: './src/main.js',
  output: {
    path: path.resolve(__dirname, './dist/dy_book'),
    publicPath: '/dist/dy_book/',
    filename: 'build.js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader'
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'url-loader?limit=8192',
        options: {
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /vux.src.*?js$/,
        loader: 'babel-loader'
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.vue', '.css', '.json'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
      'components': path.resolve(__dirname, './src/components')
    }
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    proxy: {
      '/book/api/*': {
        target: 'http://127.0.0.1:8000',
        secure: false
      }
    }
  },
  performance: {
    hints: false
  },
  plugins: [
    new webpack.ProvidePlugin({
        _: 'lodash'
    }),
    new CleanPlugin(['dist/dy_book']),
    new HtmlWebpackPlugin({
      filename: './dy_book.html',
      template: './index_template.html',
      inject: true
    })
  ],
  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production' || process.env.NODE_ENV === 'profile') {
  module.exports.output.filename = 'build.[hash:4].js'
  module.exports.devtool = '#cheap-module-source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      // sourceMap: true,
      minimize: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}

if (process.env.NODE_ENV === 'profile') {
  module.exports.plugins = (module.exports.plugins || []).concat([
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      reportFilename: '../profile/reports-index.html',
      openAnalyzer: true
    }),
  ])
}

const vuxLoader = require('vux-loader')
module.exports = vuxLoader.merge(module.exports, {
  options: {},
  plugins: [
    {
      name: 'vux-ui'
    }
    ]
})
