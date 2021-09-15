from os import path


def get_asset_url(filename):
    assets="assets"
    return path.join(assets,filename)
    
