import os
def all_dict():
    l = []
    for dirname, dirnames, filenames in os.walk(os.path.abspath('')):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            data = os.path.join(dirname, subdirname)
            if '__pycache__' in subdirname:
                dirnames.remove(subdirname)
            elif 'os_sys.egg-info' in subdirname:
                dirnames.remove(subdirname)
            elif 'build' in subdirname:
                dirnames.remove(subdirname)
            elif 'dist' in subdirname:
                dirnames.remove(subdirname)
            elif 'docs' in subdirname:
                dirnames.remove(subdirname)
            elif 'django' in subdirname:
                dirnames.remove(subdirname)
                
            else:
                pass
        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            data = os.path.join(dirname, filename)
            data = data.replace('.\\', '')
            l.append(data)
    for i in l:
        yield i
count = 0
error = 0
no_error = 0

for package in all_dict():
    count += 1
    try:
        exec(open(package).read())
        no_error += 1
    except Exception as ex:
        print(ex)
        error += 1
        pass
from tkinter import Tk
from tkinter import messagebox
messagebox.showinfo('test result', 'fails: %s\nnon_fails: %s\ntotal: %s' % (str(error), str(no_error), str(count)))
