class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        p=dict()
        p['a']=a
        p['b']=b
        p['c']=c
        s=""
        la=''
        while True:
            if p['c']>= max(p['a'],p['b']):
                if la!='c':
                    if p['c']>=2:
                        s+='cc'
                        la='c'
                        p['c']-=2
                    else:
                        s+='c'
                        la='c'
                        p['c']-=1
                if p['a']==0 and p['b']==0:
                    return s
                else:
                    if p['a']>p['b']:
                        if p['a']>=2:
                            s+='aa'
                            la='a'
                            p['a']-=2
                        else:
                            s+='a'
                            la='a'
                            p['a']-=1
                    else:
                        s+='b'
                        la='b'
                        p['b']-=1
                if p['a']==0 and p['b']==0 and p['c']==0:
                    return s
                print(p)
                print(s+'1')
                print(la)
            elif p['b']>=max(p['a'],p['c']):
                if la!='b':
                    if p['b']>= 2:
                        s+='bb'
                        la='b'
                        p['b']-=2
                    else:
                        s+='b'
                        la='b'
                        p['b']-=1
                if p['a']==0 and p['c']==0:
                    return s
                else:
                    if p['a']>p['c']:
                        s+='a'
                        la='a'
                        p['a']-=1
                    else:
                        s+='c'
                        la='c'
                        p['c']-=1
                if p['a']==0 and p['b']==0 and p['c']==0:
                    return s
                print(p)
                print(s+'2')
                print(la)
            elif p['a']>=max(p['b'],p['c']):
                if la!='a':
                    if p['a']>=2:
                        s+='aa'
                        la='a'
                        p['a']-=2
                    else:
                        s+='a'
                        la='a'
                        p['a']-=1
                if p['c']==0 and p['b']==0:
                    return s
                else:
                    if p['c']>p['b']:
                        s+='c'
                        la='c'
                        p['c']-=1
                    else:
                        s+='b'
                        la='b'
                        p['b']-=1
                if p['a']==0 and p['b']==0 and p['c']==0:
                    return s
                print(p)
                print(s+'3')
                print(la)
            # print(p)
        return s