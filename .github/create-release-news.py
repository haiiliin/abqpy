"""
Run this file by `python create-release-news.py "20xx.x.x"` to create a release news file.
"""
import os
import sys
import datetime


current_version = sys.argv[1]
if current_version.startswith("v"):
    current_version = current_version[1:]
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")

minor_version = ".".join(current_version.split(".")[1:])
news = f"""---
title: The 20**.{minor_version} release is out!
authors: ["haiiliin"]
date: {datetime.date.today().strftime("%Y-%m-%d")}
---

The abqpy `2016/2017/2018/2019/2020/2021/2022.{minor_version}` release is out! Check out the release notes at GitHub:
- [abqpy 2016.{minor_version}](https://github.com/haiiliin/abqpy/releases/tag/v2016.{minor_version})
- [abqpy 2017.{minor_version}](https://github.com/haiiliin/abqpy/releases/tag/v2017.{minor_version})
- [abqpy 2018.{minor_version}](https://github.com/haiiliin/abqpy/releases/tag/v2018.{minor_version})
- [abqpy 2019.{minor_version}](https://github.com/haiiliin/abqpy/releases/tag/v2019.{minor_version})
- [abqpy 2020.{minor_version}](https://github.com/haiiliin/abqpy/releases/tag/v2020.{minor_version})
- [abqpy 2021.{minor_version}](https://github.com/haiiliin/abqpy/releases/tag/v2021.{minor_version})
- [abqpy 2022.{minor_version}](https://github.com/haiiliin/abqpy/releases/tag/v2022.{minor_version})
"""

filepath = f'content/news/release-20xx.{minor_version}.md'
if not os.path.exists(filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(news)
    print(f"Created {filepath}")
