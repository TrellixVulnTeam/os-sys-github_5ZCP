import os
replacement = b"logger"
for dname, dirs, files in os.walk(r"C:\mattie\own lib\own lib\logger"):
    for fname in files:
        print(fname)
        fpath = os.path.join(dname, fname)
        print(fpath)
        with open(fpath, "rb") as f:
            s = f.read()
        s = s.replace(b"logging", replacement)
        with open(fpath, "wb") as f:
            f.write(s)
