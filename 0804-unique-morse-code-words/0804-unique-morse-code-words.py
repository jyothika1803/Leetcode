class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hashmap={}
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet="abcdefghijklmnopqrstuvwxyz"
        for i in range(26):
            hashmap[alphabet[i]]=morse[i]
        unique=set()
        for word in words:
            morse_code=""
            for char in word:
                morse_char=hashmap[char]
                morse_code+=morse_char
            unique.add(morse_code)
        return len(unique)
        