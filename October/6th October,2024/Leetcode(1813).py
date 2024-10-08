class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        i, j = 0, 0
        pref = []
        suff = []
        if s1 == s2:
            return True
        if s1 in s2:
            return True
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                pref.append(s1[i])
                i += 1
                j += 1
            else:
                break
        p = i
        i, j = len(s1) - 1, len(s2) - 1
        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                suff.append(s1[i])
                i -= 1
                j -= 1
            else:
                break
        e = i
        return p>e
        print(p, e)
        print(pref)
        print(suff)
        # for i in range(p,e)
        if len(pref) == 0 and len(suff) == 0:
            return False
        return True