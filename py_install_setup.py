from os_sys.py_install.make_install_files import *
packages=[]
packages.extend(find_packages(r'C:\mattie\own lib\own lib\os_sys'))
packages.extend(find_packages(r'C:\mattie\own lib\own lib\server'))
packages.extend(find_packages(r'C:\mattie\own lib\own lib\edit'))
packages.extend(find_packages(r'C:\mattie\own lib\own lib\ins'))
packages.extend(find_packages(r'C:\mattie\own lib\own lib\pygui'))
setup(name='os_sys', version='2.0.3', path=r'C:\mattie\own lib\own lib', packages=packages)
