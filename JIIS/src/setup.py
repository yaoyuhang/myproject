#!/usr/bin/env python

from distutils.core import setup,Extension,os
import string

def cmd1(str):
    print str
    temp = os.popen(str).readlines()[0][:-1]
    print temp
    return temp

def cmd2(str):
    return string.split (cmd1(str))

setup(name = "mecab-python",
	version = cmd1("/mecab/mecab-0.996/mecab-config --version"),
	py_modules=["MeCab"],
	ext_modules = [
		Extension("_MeCab",
			["MeCab_wrap.cxx",],
			include_dirs=cmd2("/mecab/mecab-0.996/mecab-config --inc-dir"),
			library_dirs=cmd2("/mecab/mecab-0.996/mecab-config --libs-only-L"),
			libraries=cmd2("/mecab/mecab-0.996/mecab-config --libs-only-l"))
			])
