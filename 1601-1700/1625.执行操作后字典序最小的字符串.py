class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        m = {s}
        t = [s]

        def change(s):
            li = [int(i) for i in s]
            step = 0
            while step < 10:
                for i in range(len(li)):
                    if i % 2:
                        li[i] = (li[i] + a) % 10
                yield ''.join(str(i) for i in li)
                step += 1

        while 1:
            tree = []
            for tmp in t:
                n_tmp = tmp[b:] + tmp[:b]
                if n_tmp in m:
                    continue
                m.add(n_tmp)
                tree.append(n_tmp)
                for n_s in change(n_tmp):
                    tree.append(n_s)
                    m.add(n_s)
            if not tree:
                break
            t = tree
        return min(m)


print(Solution().findLexSmallestString("43987654", 7, 3))
