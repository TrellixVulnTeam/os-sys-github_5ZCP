import py_compile
import os
for dname, dirs, files in os.walk(r"C:\mattie\py_ide\py_ide\dist"):
    for fname in files:
        if fname.endswith('.py'):
            py_compile.compile(os.path.join(dname,fname), os.path.join(dname,fname.replace('.py','.pyc')))
            print('done:', os.path.join(dname,fname),'file placed in:', os.path.join(dname,fname.replace('.py','.pyc')))
