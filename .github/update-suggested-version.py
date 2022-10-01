"""
Run this file by `python update-suggested-version.py "20xx.x.x"` to update the version in
README.md, README-zh-cn.md, and docs/source/getting_started.rst.
"""
import os
import re
import sys


current_version = sys.argv[1]
if current_version.startswith("v"):
    current_version = current_version[1:]
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")

for file in ['docs/source/getting_started.rst']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'abqpy(=+?)20\d\d\.\d+?\.\d+?'
    repl = f'abqpy\g<1>{current_version}'
    content = re.sub(pattern, repl, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
