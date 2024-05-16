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
        test: /\.svg$/,
        use: [
          {
            loader:'svg-url-loader',
         
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
       directory:path.join(__dirname,'public'),
    },
    compress: true,
    port: 8080,
  }
};
