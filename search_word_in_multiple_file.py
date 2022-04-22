#!/usr/bin/env python
# encoding: utf-8
import os

base_path = 'D:\\WindowsTemp\\USER\\Desktop\\test'
search_exts = '.txt .md'.split(" ")
search_word = 'red yellow'.split(" ")

def find():
    for root, dirs, files in os.walk(base_path):
        for filename in files:
            for ext in search_exts:
                if(filename.endswith(ext)):
                    file = os.path.join(root, filename)
                    search_file(file, search_word)

def search_file(file, word):
    with open(file, 'r') as f:
        for num, content in enumerate(f.readlines(), 1):
            for key in word:
                if str(key) in content:
                    print(f'found <{content}> at Line {num} in file: {file}')


if __name__ == "__main__":
    find()
