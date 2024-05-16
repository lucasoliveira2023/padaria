const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  mode:'developement',
  context: __dirname,
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'static', 'bundles'),
    filename: '.js',
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
};
