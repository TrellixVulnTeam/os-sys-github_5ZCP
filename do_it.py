import os
ti = ''

def all_dict(dictory, exceptions=None, file_types=None, maps=True, files=True, print_data=False):
    global ti
    data = []
    string_data = ''
    e = exceptions
    if 'list' in str(type(e)) or e == None:
        pass
    else:
        raise TypeError('expected a list but got a %s' % type(e))
    e = file_types
    if 'list' in str(type(e)) or e == None:
        pass
    else:
        raise TypeError('expected a list but got a %s' % type(e))
    
    print_ = print_data
    
    for dirname, dirnames, filenames in os.walk(dictory):
        # print path to all subdirectories first.
        if maps:
            for subdirname in dirnames:
                dat = os.path.join(dirname, subdirname)
                data.append(dat)
                string_data = string_data + '\n' + dat
                if print_:
                    print(dat)

        # print path to all filenames.
        if files:
            for filename in filenames:
                s = False
                fname_path = filename
                file = fname_path.split('.', 1)
                no = int(len(file) - 1)
                file_type = '/*.' + str(file[-1])
                ti += file_type
                if not file_types == None:
                    for b in range(0, len(e)):
                        if file_type[b] == os.path.splitext(fname_path)[1]:
                            s = True
                            
                if e == None:
                    s = True
                if s:
                    s = False   
                            
                    dat = os.path.join(dirname, filename)
                    data.append(dat)
                    string_data = string_data + '\n' + dat
                    if print_:
                        
                        print(dat)
        

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if not exceptions == None:
            
            for ip in range(0, int(len(exceptions))):
                exception = exceptions[ip]
                
                if exception in dirnames:
                    # don't go into any .git directories.
                    dirnames.remove(exception)
    for dire in data:
        yield dire
"""
lol = []
w=[]
for i in all_dict('C:\\mattie\\own lib\\own lib\\win32_extentions',maps=False):
    i = i.replace('C:\\mattie\\own lib\\own lib\\win32_extentions\\','')
    print(i)
    if '.pyd' in i:
        w.append(i)
    else:
        lol.append(i.replace('.py',''))
print(lol)
print('')
print('--------------------------')
print('')
new = []
for i in w:
    print(i[:-1])
    fh = open(i[:-1],'w+')
    fh.write(f'from win32_extentions.{i.replace(".pyd", "")} import *')
    fh.close()
    new.append(i[:-1])
print(new)
raise SystemExit
"""
count = 0
def do(path):
    return os.path.dirname(path)
for i in all_dict(r'C:\Users\matthijs\AppData\Local\Programs\Python\Python37\Lib\site-packages\pip', maps=False,file_types=['.py','py']):
    with open(i) as file:
        if '"Using cached' in file.read():
            print(i)
print('ok')

try:
    os.mkdir('bars')
except:
    pass
for p in all_dict(r'D:\lmms files\preset\thonny-master\thonny', files=False):
    try:
        os.mkdir(os.path.join(os.path.abspath(''), 'py_ide', str(p.replace(r'D:\lmms files\preset\thonny-master\thonny', '')).replace('thonny', 'py_ide')))
    except:
        pass

for i in all_dict(r'D:\lmms files\preset\thonny-master\thonny', maps=False):
    count += 1
    try:
        os.mkdir('\\'.join(str(os.path.join(os.path.abspath(''), 'py_ide', str(i.replace(r'D:\lmms files\preset\thonny-master\thonny', '')).replace('thonny', 'py_ide'))).replace('tqdm','bars').split('\\')[:-1])[2:-1])
    except:
        pass
    try:
        try:
            os.mkdir('C:\\mattie\own lib\\own lib' + '\\' + 'py_ide' + str(i.replace('D:\\lmms files\\preset\\thonny-master\\thonny', '')).replace('thonny', 'py_ide'))
        except Exception as ex:
            print(ex)
        fh = open('C:\\mattie\own lib\\own lib' + '\\' + 'py_ide' + str(i.replace('D:\\lmms files\\preset\\thonny-master\\thonny', '')).replace('thonny', 'py_ide'), 'wb')
        f = open(i, 'rb').read()
        fh.write(bytes(bytes(bytes(bytes(bytes(bytes(f.replace(b'thonny', b'py_ide')).replace(b'tra', b'bra')).replace(b'Tqdm', b'Bars')).replace(b'docs.editproject.com/en/{{ docs_version }}/', b'stranica.nl/docs/')).replace(b'idle', b'edit')).replace(b'Idle', b"edit")).replace(b'IDLE', b'edit').replace(b'after_edit', b'after_idle'))
        fh.close()
    except Exception as ex:
        print(ex)
        '''
        try:
            if os.path.isdir(do(os.path.join(os.path.abspath(''), 'edit', str(i.replace('C:\\Users\\matthijs\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib\\', '')).replace('idlelib', 'edit')))):
                pass
            else:
                os.mkdir(do(os.path.join(os.path.abspath(''), 'edit', str(i.replace('C:\\Users\\matthijs\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib\\', '')).replace('idlelib', 'edit'))))
        except Exception as exc:
            raise ex from exc
            '''
