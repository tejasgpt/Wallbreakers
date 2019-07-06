class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        PROBLEM STATEMENT:
        Given a paragraph and a list of banned words, 
        return the most frequent word that is not in the list of banned words.  
        It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
        Words in the list of banned words are given in lowercase, and free of punctuation.  
        Words in the paragraph are not case sensitive.  The answer is in lowercase.
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        paragraph = paragraph.replace(',',' ')
        words = (w.strip("?.';!") for w in paragraph.lower().split(' '))
        wordFreq = dict()
        for word in words:
            if word in banned or len(word)==0:
                continue
            if word in wordFreq:
                wordFreq[word] += 1
            else:
                wordFreq[word] = 1
        maxword = ''
        maxcount = 0
        for itr,word in enumerate(wordFreq):
            if wordFreq[word] > maxcount:
                maxword = word
                maxcount = wordFreq[word]
        return maxword
