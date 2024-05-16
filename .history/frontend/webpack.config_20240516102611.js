const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  mode:'development',
  context: __dirname,
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'static', 'bundles'),
    filename: 'bundle.js',
    publicPath: '/static/bundles/',
  },
  plugins: [
    new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-react', '@babel/preset-env'],
          },
        },
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  devServer: {
    static: {
       path.join(__dirname,'static'),
    }
    compress: true,
    port: 9000,
    hot: true,
    historyApiFallback: true,
  }
};
