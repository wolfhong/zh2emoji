#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from PIL import Image, ImageDraw, ImageFont


def word2image(word, width=400, fontpath='PingFangBold.ttf'):
    '''
    @brief 将一个中文字符转为图片
    @params word: 一个中文字,__len__长度为1
    @params width: 返回的图片宽的数字,默认400,高根据宽自动调节
    @params fontpath: 字体文件的路径
    @return image
    '''
    # assert len(word) == 1
    page_width, page_height = (400, 450)
    word_color = '#000000'  # 文字颜色,黑色
    bg_color = '#ffffff'  # 背景颜色,白色

    img = Image.new('RGBA', (page_width, page_height), bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontpath, 400)
    draw.text((0, -50), word, word_color, font)

    height = int(width * 1.0 / page_width * page_height)
    img = img.resize((width, height), Image.NEAREST)
    # img.save('test.png')
    # img.show()
    return img


def image2print(img, char=u'❤️ ', width=40):
    '''
    @brief 将图片转化为字符串,字符串可以在终端打印出来
    @params img: 待打印的白底黑字的图片.
    @params char: 替换图片的字符
    @params width: 由于像素点转为打印字符占用屏幕宽度挺大的, 所以需要对图片进行相应缩小.
    @return string
    '''
    ascii_char = [char, u'  ']

    def select_ascii_char(r, g, b):
        ''' 在灰度图像中,灰度值最高为255,代表白色,最低为0,代表黑色 '''
        gray = int((19595 * r + 38469 * g + 7472 * b) >> 16)  # 'RGB－灰度值'转换公式
        unit = 256.0 / len(ascii_char)  # ascii_char中的一个字符所能表示的灰度值区间
        return ascii_char[int(gray/unit)]

    txt = ""
    old_width, old_height = img.size
    height = int(width * 1.0 / old_width * old_height)
    img = img.resize((width, height), Image.NEAREST)

    for h in xrange(height):
        for w in xrange(width):
            txt += select_ascii_char(*img.getpixel((w, h))[:3])
        txt += '\n'
    return txt


if __name__ == '__main__':
    ''' demo
    使用不同的填充方法显示来展示"茴"字
    其中, 对于ascii 建议后面多一个空格填充;
    对于emoji表情, 可能跟终端的打印方式有关, 对比后自行决定后面需不需要加上空格填充;
    对于中文,输出正好;
    '''
    print(image2print(word2image(u'茴'), u'W '))
    print(image2print(word2image(u'茴'), u'❤️ '))
    print(image2print(word2image(u'茴'), u'茴', width=40))
    print(image2print(word2image(u'熊'), u'🐻 '))
