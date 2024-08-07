class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        d = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
            50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety",
            100: "Hundred", 1000: "Thousand", 1000000: "Million",
            1000000000: "Billion"
        }
        
        def get_string(n):
            l = []
            h = n // 100
            if h:
                l.append(d[h])
                l.append(d[100])
            l2 = n % 100
            if l2 >= 20:
                l.append(d[(l2 // 10) * 10])
                if l2 % 10 > 0:
                    l.append(d[l2 % 10])
            elif l2 > 0:
                l.append(d[l2])
            return " ".join(l)

        pg = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []
        while num:
            digits = num % 1000
            s = get_string(digits)
            if s:
                res.append(s + pg[i])
            num = num // 1000
            i += 1
        res.reverse()
        return " ".join(res).strip()

