#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from zh2emoji import word2image, image2print


def test_print():
    ''' test
    使用不同的填充方法显示来展示"茴"字
    其中, 对于ascii 建议后面多一个空格填充;
    对于emoji表情, 可能跟终端的打印方式有关, 对比后自行决定后面需不需要加上空格填充;
    对于中文,输出正好;
    '''
    print(image2print(word2image('茴'), 'W '))
    print(image2print(word2image('茴'), '❤️ '))
    print(image2print(word2image('茴'), '茴', width=40))
    print(image2print(word2image('熊'), '🐻 '))
