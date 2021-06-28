base, mod = 113, 10 ** 9 + 9  # base值和模
text='cbadeajsssx'
n = len(text)
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = (prefix[i - 1] * base + ord(text[i - 1])) % mod
m1={}
def mult(leng):
    return pow(base,leng,mod)
def hash2(l,r):
    return (prefix[r+1]-prefix[l]*mult(r-l+1))%mod
def hash(s):
    a=0
    for ch in s:
        a=(a*base+ord(ch))%mod
    return a
