class Solution:
    def get_bit_number(self,letter):
        return ord(letter) - ord('a')
    
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmasks = [0] * n
        max_product = 0
        
        # create bitmask
        for i,word in enumerate(words):
            bitmask = 0
            for c in word:
                bitmask |= 1 << self.get_bit_number(c)
            bitmasks[i] = bitmask
            
        
        # compare letters
        for i in range(n):
            for j in range(i,n):
                if bitmasks[i] & bitmasks[j] == 0:
                    max_product = max(max_product,len(words[i]) * len(words[j]))
        
        return max_product