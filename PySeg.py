#coding=utf-8

import Common
import codecs

class PySeg:
    def __init__(self):
        self.trie = Common.Trie()
        self.maxWordLen = 2
        self.loadDict()
    
    def loadDict(self):
        f = codecs.open("Dict/SogouLabDic.dic", "r+", encoding='gbk')
        print 'loading SogouLabDic.dic...'
        while True:
            try:
                line = f.readline()
            except:
                continue
            if len(line) == 0:  break
            data = line.split()
            word = data[0].strip()
            word = word.encode('utf-8')
            self.trie.insert(word)
            self.maxWordLen = max(self.maxWordLen, len(word))
        f.close()
        print "Done! maxWordLen = %d" % (self.maxWordLen)

    def seg(self, sentence):
        s_len = len(sentence)
        tokens = []
        i = 0;
        while i < s_len:
            for j in xrange(min(self.maxWordLen, s_len-i), 0, -1):
                if i + j > s_len:  continue
                token = sentence[i:i+j].encode('utf-8')
                if self.trie.find(token):
                    tokens.append(token)
                    i = i + j
                    break
                elif j == 1:
                    tokens.append(token)
                    i = i + j
                    break

        return tokens
            

segmentor = PySeg()

tokens = segmentor.seg(u'中华人民共和国是一个前所未有的傻逼国家')
for token in tokens:
    print token
