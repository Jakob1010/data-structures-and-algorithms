class Codec:

    def encode(self, strs):
        if len(strs) == 0:
            return unichr(258)
        
        encoded = unichr(257).join(s for s in strs)
        return encoded
        

    def decode(self, s):
        if s == unichr(258):
            return []
        
        decoded = s.split(unichr(257))
        return decoded
        
        
