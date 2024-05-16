const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    // outras configuracoes
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),               ///se der problema assim tenata ({path:__dirname: './webpack-starts'})
    ],
}