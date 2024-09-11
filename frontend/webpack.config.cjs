//import path from 'path';
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
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      
      {
        test: /\.svg$/,
        use: [
          {
            loader:'svg-url-loader',
            options: {
              limit: 10000,
            },         
          },
        ]        
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  devServer: {
    static: {
      directory:path.join(__dirname,'public'),
    },
    compress: true,
    port: 8080,
  },
  resolve: {
    extensions: ['.js', '.jsx'], //para resolver essas externsoes
  },
};
