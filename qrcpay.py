#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pyqrcode

transfer = pyqrcode.create('BCD\n001\n1\nSCT\nASPKAT2LXXX\nChristoph Pranzl\nAT682032032202496141\nEUR7.50\n\nLunch Yume-City\n',
                       version=6,
                       mode='binary',
                       error='M',
                       encoding='utf-8'
)
transfer.png('qrcpay.png')
