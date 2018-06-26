#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from zh2emoji import word2image, image2print

unicode_type = unicode if sys.version_info[0] == 2 else str


def show_animation(words):
    '''
    @brief 将words一句话在终端依次打印出来
    '''
    for word in words:
        _img = word2image(word)
        print(image2print(_img))
        time.sleep(0.2)


if __name__ == '__main__':
    ''' demo:该例子会在终端刷出一句话出来 '''
    content = sys.argv[1] if len(sys.argv) > 1 else '请输入一行话'
    if not isinstance(content, unicode_type):
        content = content.decode(sys.stdin.encoding)
    show_animation(content)
