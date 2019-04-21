# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import division
import math
import re
from mk_dict import dict, punc, tokens, pre_dict
from config import num_letter

class NGram(object):
    def segment(self, test_path, test_out_path, method='DP'):
        test_f = open(test_path, 'r')
        out_f = open(test_out_path, 'w')
        for sentence in test_f:
            sentence = sentence.strip().decode('gbk')
            if method=='DP':
                final_seg = self.__DP(sentence)
            '''
            else:
                pre_seg = self.__pre_max_seg(sentence, dict)
                pos_seg = self.__post_max_seg(sentence, dict)
                all_word, pre_word = self.__merge_pre_post(sentence, pre_seg, pos_seg)
                final_seg = self.__max_log_pro(all_word, pre_word)
            '''
            for word in final_seg:
                out_f.write(word.encode('gbk')+' ')

            out_f.write('\n')
        test_f.close()
        out_f.close()

    def __DP(self, sentence, max_pre_len = 12):
        sen_len = len(sentence)
        max_pro = {0:0}
        max_pro_pos = {0:-1}
        end = 1
        num_handle_flag = -1
        while(end <= sen_len):
            max_tmp = float('-Inf')
            start = end - min(max_pre_len, end)
            while(start < end):
                word_len = end - start

                seg_obj = re.search(num_letter, sentence[end-1 : ])
                if(seg_obj and num_handle_flag < 0):
                    seg_tmp = seg_obj.group()
                    seg_len = len(seg_tmp)
                    pre_word = sentence[max_pro_pos[end-1] : end-1]
                    max_pro[end+seg_len-1] = max_pro[end-1] + self.__get_2gram_pro(seg_tmp, pre_word)
                    max_pro_pos[end+seg_len-1] = end-1
                    end += seg_len-2
                    num_handle_flag = 1
                    break

                seg_word = sentence[start: end]
                if not max_pro.has_key(start):
                    start += 1
                    continue
                if (dict.get(seg_word) or word_len == 1):
                    pre_word = sentence[max_pro_pos[start]: start] if max_pro_pos[start]!=-1 else '<S>'
                    pro = max_pro[start] + self.__get_2gram_pro(seg_word, pre_word)
                    if (pro >= max_tmp):
                        max_tmp = pro
                        max_pro[end] = max_tmp
                        max_pro_pos[end] = start
                start += 1
            num_handle_flag -= 1
            end += 1
        seg_result = []
        end -= 1
        while (end != 0):
            start = max_pro_pos[end]
            seg_result.append(sentence[start : end])
            end = start
        seg_result.reverse()
        return seg_result

    def __get_pro(self, word):
        dict_len = len(dict)
        pro = (dict.get(word, 0) + 1)/(tokens + dict_len)
        return math.log(pro)

    def __get_2gram_pro(self, word, pre_word):
        d_len = len(dict)-1
        if dict.get(pre_word):
            freq = sum([value for _, value in pre_dict[pre_word].items()])
            pro = (pre_dict[pre_word].get(word, 0)+1) / (freq+d_len)
        elif dict.get(word):
            pro = 1/d_len
        else:
            pro = 1/(2*d_len)

        return math.log(pro)