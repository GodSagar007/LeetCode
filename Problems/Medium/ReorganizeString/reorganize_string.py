class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        c = Counter(s)
        max_freq_char,max_freq = c.most_common(1)[0] 
        if 2*max_freq>len(s)+1:
            return ""
        
        res = [""]*len(s)
        index = 0

        while max_freq:
            res[index] = max_freq_char
            index+=2
            max_freq-=1     
        del c[max_freq_char]

        for char in c.elements():
            if index >= len(s):
                index = 1
            res[index] = char
            index+=2

        return "".join(res)
