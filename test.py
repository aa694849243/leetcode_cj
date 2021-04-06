c = [(1, 1), (2, 2), (3, 3)]
c = {1: 1, 2: 2}
while c:
   a=c.keys()
   for i in a:
      c.pop(i)
      break
