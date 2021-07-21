def find(li, target):
    l, r = 0, len(li) - 1
    while l < r:
        mid = l + (r - l) // 2
        if li[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l
find([1,1,1,3,6,6,7],7)
