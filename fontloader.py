import os, _fontloader

# this  function can throw errors
def load(fp):
    return _fontloader.load(fp)


def unload(font_id):
    _fontloader.unload(font_id)


class FontLoader(object):
    def __init__(self, auto_unload = True):
        self.auto_unload = auto_unload
        self.font_ids = []

    def load(self, font_fp):
        if os.path.exists(font_fp):
            font_id = _fontloader.load(font_fp)
            if font_id in self.font_ids:
                return font_id
            
            self.font_ids.append(font_id)
            return font_id
    
    def unload(self, font_id):
        _fontloader.unload(font_id)
        
    def __del__(self):
        if self.auto_unload:
            for font_id in self.font_ids:
                self.unload(font_id)

                
                

 