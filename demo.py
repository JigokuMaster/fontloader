import appuifw, os, e32, fontloader

app_lock = e32.Ao_lock()
ttf_loader = fontloader.FontLoader()


# simple file-browser dialog , copied from filebrowser.py i don't who wrote it

s = lambda s:s.encode('utf-8')

u = lambda s:s.decode('utf-8')

def select_file(label, dironly = False, dirname = ''):
    isdir = lambda fname:os.path.isdir(os.path.join(dirname, fname))

    isfile = lambda fname:(not os.path.isdir(os.path.join(dirname, fname)))

    markdir = lambda fname:(fname + '\\')


    def chkdir(d):
        d = s(d)
        if (not d.endswith('\\')):
            return (d + '\\')
        else:
            return d


    while True:
        if (not dirname):
            items = map(chkdir, e32.drive_list())
        else:
            lst = os.listdir(dirname)
            dirs = map(markdir, filter(isdir, lst))
            dirs.sort()
            if (not dironly):
                files = filter(isfile, lst)
                files.sort()
            else:
                files = []
            items = ((['..'] + dirs) + files)
        ans = appuifw.popup_menu(map(u, items), u(label))
        if (ans is None):
            return None
        fname = items[ans]
        if (fname == '..'):
            return fname
        fname = os.path.join(dirname, fname)
        if os.path.isdir(fname):
            ans = select_file(fname, dironly, fname)
            if (ans != '..'):
                return ans
            if (dironly and (ans == '..')):
                return fname
        else:
            return fname




def load_font():
    font_fp = None
    try:
        import powlite_fm
        
        fileman = powlite_fm.manager()
        font_fp = fileman.AskUser(None, 'file', ['.ttf'], False)
    except:
        font_fp = select_file('choose font file')
        
    if font_fp:
        ttf_loader.load(unicode(font_fp))    

def test_font():            
    load_font()    
    fonts = appuifw.available_fonts()
    i = appuifw.popup_menu(fonts, u'test available fonts')
    if i == None:
        return
        
    t = appuifw.app.body
    t.font = fonts[i]
    t.clear()
    t.add('\n\nusing font: %s\n\n' %t.font[0])
    t.add(u"The quick brown fox jumped over the lazy dog")
    

def quit():
    global ttf_loader
    del ttf_loader
    app_lock.signal()
    
def main():
    appuifw.app.body = appuifw.Text()
    appuifw.app.menu = [(u'Load Font',  test_font), (u'Exit', quit)]
    test_font()
    app_lock.wait()


main()