const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    // outras configuracoes
    plugins: [
        new BundleTracker({path:__frontend : './webpack-starts.json' }),               ///se der problema assim tenata ({path:__dirname: './webpack-starts.jason'}),
    ],
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name]-[hash].js',
        publicPath: '/static/bundles/',
    },
}