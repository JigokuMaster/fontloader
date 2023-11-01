### Simple PyS60 extension to load custom fonts files


### Note :

The extension is compiled for S60v3 only ,

use [_fontloader.pyd](./_fontloader.pyd) for PyS60 1.45,

use [kf__fontloader.pyd](./kf__fontloader.pyd) PyS60 2.0

### Basic usage

import fontloader

# font_fp must be unicode ,  example u'C:\\font.ttf'
font_id = fontloader.load(font_fp)

# use it with appuifw controls like Canvas / Text ...

# remove the loaded font from font bitmap server
fontloader.unload(font_id)


# you can also use FontLoader class if you want to unload all fonts automatically when closing the app. 


ttf_loader = fontloader.FontLoader()

ttf_loader.load(font_fp)

see also [demo.py](./demo.py)




