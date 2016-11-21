#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from zh2emoji import word2image, image2print


def str2unicode(ustr, decoding='utf-8'):
    if isinstance(ustr, unicode):
        return ustr
    return unicode(ustr, decoding, 'replace')


def show_animation(words):
    '''
    @brief 将words一句话在终端依次打印出来
    '''
    for word in words:
        _img = word2image(word)
        print image2print(_img)
        time.sleep(0.5)


if __name__ == '__main__':
    ''' demo:该例子会在终端刷出一句话出来 '''
    content = sys.argv[1] if len(sys.argv) > 1 else u'请输入一行话'
    show_animation(str2unicode(content))
