class Solution(object):
    def findWordsContaining(self, words, x):
        i=0
        j=0
        arr =[]
        for i in range(len(words)):
            for j in range(len(x)):
                if x[j] in words[i]:
                    arr.append(i)

        return arr

        
        
        
        