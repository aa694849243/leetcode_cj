# 最大公约数
# m个数gcd的时间复杂度为m+logC，C为m的最大值
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
print(gcd(4,5))