# -*- coding:utf-8 -*-

from __future__ import print_function

train_path = r'data/199801.txt'
dict_path = r'dict/dict01.txt'
uni_dict_path = r'dict/uni_dict.txt'
rm_list_path = r'data/rm_list.txt'
test_path = r'data/testset.txt'
test_out_path = r'data/testset_out.txt'
test_post_out_path = r'data/test_post_out.txt'
punc_path = r'dict/punc.txt'
pre_dict_path = r'dict/pre_dict.txt'

punc = [' ', u'\u3000', u'\x30fb', u'\u3002', u'\uff0c', u'\uff01', u'\uff1f', u'\uff1b',
        u'\uff1a', u'\u201c', u'\u201d', u'\u2018', u'\u2019', u'\uff08', u'\uff09',
        u'\u3010', u'\u3011', u'\uff5b', u'\uff5d', u'-', u'\uff5e', u'\uff3b',
        u'\uff3d', u'\u3014', u'\u3015', u'\uff0e', u'\uff20', u'\uffe5', u'\u2022', u'.',
        u'\u300e', u'\u300f', u'\u2014', u'\u2026', u'\u3008', u'\u3009', u'\u300a', u'\u300b']

num_letter = u'^[\uff10-\uff19|\uff21-\uff3a+|\uff41-\uff5a|\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d|\u96f6|\u5341|\u767e|\u5343|\u4e07|\u4ebf|\u5146|\uff2f|\uff0e|\xb7|\uff0d]+'