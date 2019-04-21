#coding=utf-8
from __future__ import print_function
import re
from config import train_path, dict_path, uni_dict_path,\
    rm_list_path, punc_path, pre_dict_path
import cPickle

class Dictionary(object):
    def __init__(self):
        self.__DICT = {}
        self.__PUNC = []
        self.__TOKENS = 0
        self.__PREDICT = {}

    #write dict to file
    def WriteDict(self, dict_path):
        DictF = open(dict_path, 'w')

        DictF.write(str(self.__TOKENS) + '\n')
        for word in self.__DICT:
            DictF.write(word.encode('utf-8') + ' ' + str(self.__DICT[word]) + '\n')

        print (len(self.__DICT))

        DictF.close()

    #read dict from file
    def ReadDict(self, dict_path):
        DictF = open(dict_path, 'r')

        line = DictF.readline()
        self.__TOKENS = int(line)
        line = DictF.readline()
        while line:
            [word, num] = line.split(' ')
            word = word.decode('utf-8')
            num = int(num)
            self.__DICT[word] = num
            line = DictF.readline()

        print (len(self.__DICT))
        DictF.close()
        return self.__DICT, self.__TOKENS


    def MkDict(self, train_path):
        TrainF = open(train_path, 'r')
        PuncSet = set()
        for line in TrainF:
            sentence = line.strip().split(' ')
            sentence = [word for word in sentence if word != '']
            if sentence == []:
                continue
            sentence[0] = '<S>/s'

            for WordPos in sentence:

                [word, pos] = WordPos.split('/')
                word = word.strip().decode('utf-8')

                if pos == 'w':
                    PuncSet.add(word)

                re_obj2 = re.search(u'^[\uff10-\uff19|\uff21-\uff3a+|\uff41-\uff5a|'
                                    u'\u4e00|\u4e8c|\u4e09|\u56db|\u4e94|\u516d|\u4e03|\u516b|\u4e5d|\u96f6|\u5341|\u767e|\u5343|\u4e07|\u4ebf|\u5146|\uff2f|'
                                    u'\uff0e|\xb7|\uff0d]+$', word)
                if re_obj2:
                    continue

                self.__DICT[word] = self.__DICT.get(word, 0) + 1
                self.__TOKENS += 1

        self.__PUNC = list(PuncSet)

    def MkPreDict(self, pre_dict_path, train_path):
        TrainF = open(train_path, 'r')
        for word in dict:
            self.__PREDICT[word]={}

        for line in TrainF:
            sentence = line.strip().split(' ')
            sentence = [word for word in sentence if word != '']

            if sentence==[]:
                continue

            sentence[0] = '<S>'

            for i, next_word in enumerate(sentence[1:]):
                next_word = sentence[i] = sentence[i].split('/')[0].strip().decode('utf-8')
                word = sentence[i-1]
                if self.__DICT.get(word) and self.__DICT.get(next_word):
                    self.__PREDICT[word][next_word] = 1 + self.__PREDICT[word].get(next_word, 0)
                    # print (sentence[i+1].encode('utf-8')+' 前面的词是 '+sentence[i].encode('utf-8'))

    def WritePunc(self, punc_path):
        PuncF = open(punc_path, 'w')

        for p in self.__PUNC:
            PuncF.write(p.encode('utf-8') + '\n')

        PuncF.close()

    def ReadPunc(self, punc_path):
        PuncF = open(punc_path, 'r')

        for line in PuncF:
            p = line.decode('utf-8')
            self.__PUNC.append(p)

        PuncF.close()
        return self.__PUNC

    #just a try function
    def SelectUniWord(self, uni_dict_path):
        UniDictF = open(uni_dict_path, 'w')

        UniList = []

        for word in self.__DICT:
            if(self.__DICT[word]==1):
                UniList.append(word)
        for word in UniList:
            UniDictF.write(word+'\n')

        UniDictF.close()
        print (len(UniList))

    def WritePreDict(self, pre_dict_path):
        f = open(pre_dict_path, 'w')
        cPickle.dump(self.__PREDICT, f)
        f.close()

    def ReadPreDict(self, pre_dict_path):
        f = open(pre_dict_path, 'r')
        self.__PREDICT = cPickle.load(f)
        f.close()
        return self.__PREDICT

d = Dictionary()
# d.MkDict(train_path)
# d.WriteDict(dict_path)
# d.WritePunc(punc_path)
dict, tokens = d.ReadDict(dict_path)
punc = d.ReadPunc(punc_path)
# d.MkPreDict(pre_dict_path, train_path)
# d.WritePreDict(pre_dict_path)
pre_dict = d.ReadPreDict(pre_dict_path)
# print ('loaded')