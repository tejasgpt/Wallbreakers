class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        PROBLEM STATEMENT:
        Given a list of words, each word can be written as a concatenation of the Morse code of each letter.
        For example, "cba" can be written as "-.-..--...", 
        (which is the concatenation "-.-." + "-..." + ".-"). 
        We'll call such a concatenation, the transformation of a word.
        Return the number of different transformations among all words we have.
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse = set()
        
        for word in words:
            temp = ""
            for char in word:
                temp += morse_code[ord(char)-ord('a')]
            morse.add(temp)
        return len(morse)
