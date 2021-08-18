#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成
# 了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon
# 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。
#
#  在结果列表中，选择 字典序最小 的名字作为真实名字。
#
#
#
#  示例：
#
#
# 输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], syn
# onyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
# 输出：["John(27)","Chris(36)"]
#
#
#
#  提示：
#
#
#  names.length <= 100000
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 哈希表 字符串 计数
#  👍 45 👎 0


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        f = {}
        names.sort()

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a > b:
                a, b = b, a
            if a != b:
                f[b] = a
        ab=[]
        for s in synonyms:
            li = s.split(',')
            x, y = li[0][1:], li[1][:-1]
            if x in ('Ghc','Aeax','Tlv','Qxkjt','Qweye') or y in ('Aeax','Ghc','Tlv','Qxkjt','Qweye'):
                ab.append((x,y))
            union(x, y)
        sizes = collections.defaultdict(int)
        for s in names:
            i = s.index('(')
            num = int(s[i + 1:-1])
            sizes[find(s[:i])] += num
        res = []
        for name in sizes:
            a = name + '(' + str(sizes[name]) + ')'
            res.append(a)
        return res

# 定义并查集
class UnionFind:
    def __init__(self, n, realNames):
        self.n = n
        self.parent = list(range(n))
        self.realNames = realNames

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if self.realNames[rooti] > self.realNames[rootj]:  # 确保字典序较小的作为根节点
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.parent[rootj] = rooti


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        n = len(names)
        realNames, counts = [], []
        idxMap = {}
        # 1. 拆分名字、频率
        for i in range(n):
            realNames.append(names[i][:names[i].find('(')])
            counts.append(int(names[i][len(realNames[-1]) + 1:len(names[i]) - 1]))
            idxMap[realNames[-1]] = i
        # 将synonyms中的名字也加入并查集
        for synonym in synonyms:
            pair = synonym.split(',')
            name1, name2 = pair[0][1:], pair[1][:-1]
            if name1 not in idxMap:
                idxMap[name1] = len(realNames)
                realNames.append(name1)
            if name2 not in idxMap:
                idxMap[name2] = len(realNames)
                realNames.append(name2)
        # 2. 创建并查集
        unionFind = UnionFind(len(realNames), realNames)
        # 3. 遍历synonyms，将其加入并查集
        for synonym in synonyms:
            pair = synonym.split(',')
            name1, name2 = pair[0][1:], pair[1][:-1]
            unionFind.unite(idxMap[name1], idxMap[name2])
        # 4. 累计真实名称个数
        counter = collections.defaultdict(int)
        for i in range(n):
            counter[unionFind.find(i)] += counts[i]
        # 5. 输出真实名称个数
        ans = []
        for k, v in counter.items():
            ans.append(realNames[k] + '(' + str(v) + ')')
        return ans


Solution().trulyMostPopular(["Fcclu(70)", "Ommjh(63)", "Dnsay(60)", "Qbmk(45)", "Unsb(26)", "Gauuk(75)", "Wzyyim(34)", "Bnea(55)", "Kri(71)", "Qnaakk(76)", "Gnplfi(68)", "Hfp(97)", "Qoi(70)", "Ijveol(46)", "Iidh(64)", "Qiy(26)", "Mcnef(59)", "Hvueqc(91)", "Obcbxb(54)", "Dhe(79)", "Jfq(26)", "Uwjsu(41)", "Wfmspz(39)", "Ebov(96)", "Ofl(72)", "Uvkdpn(71)", "Avcp(41)", "Msyr(9)", "Pgfpma(95)", "Vbp(89)", "Koaak(53)", "Qyqifg(85)", "Dwayf(97)", "Oltadg(95)", "Mwwvj(70)", "Uxf(74)", "Qvjp(6)", "Grqrg(81)", "Naf(3)", "Xjjol(62)", "Ibink(32)", "Qxabri(41)", "Ucqh(51)", "Mtz(72)", "Aeax(82)", "Kxutz(5)", "Qweye(15)", "Ard(82)", "Chycnm(4)", "Hcvcgc(97)", "Knpuq(61)", "Yeekgc(11)", "Ntfr(70)", "Lucf(62)", "Uhsg(23)", "Csh(39)", "Txixz(87)", "Kgabb(80)", "Weusps(79)", "Nuq(61)", "Drzsnw(87)", "Xxmsn(98)", "Onnev(77)", "Owh(64)", "Fpaf(46)", "Hvia(6)", "Kufa(95)", "Chhmx(66)", "Avmzs(39)", "Okwuq(96)", "Hrschk(30)", "Ffwni(67)", "Wpagta(25)", "Npilye(14)", "Axwtno(57)", "Qxkjt(31)", "Dwifi(51)", "Kasgmw(95)", "Vgxj(11)", "Nsgbth(26)", "Nzaz(51)", "Owk(87)", "Yjc(94)", "Hljt(21)", "Jvqg(47)", "Alrksy(69)", "Tlv(95)", "Acohsf(86)", "Qejo(60)", "Gbclj(20)", "Nekuam(17)", "Meutux(64)", "Tuvzkd(85)", "Fvkhz(98)", "Rngl(12)", "Gbkq(77)", "Uzgx(65)"], ["(Gnplfi,Qxabri)", "(Uzgx,Siv)", "(Bnea,Lucf)", "(Qnaakk,Msyr)", "(Grqrg,Gbclj)", "(Uhsg,Qejo)", "(Csh,Wpagta)", "(Xjjol,Lucf)", "(Qoi,Obcbxb)", "(Npilye,Vgxj)", "(Aeax,Ghc)", "(Txixz,Ffwni)", "(Qweye,Qsc)", "(Kri,Tuvzkd)", "(Ommjh,Vbp)", "(Pgfpma,Xxmsn)", "(Uhsg,Csh)", "(Qvjp,Kxutz)", "(Qxkjt,Tlv)", "(Wfmspz,Owk)", "(Dwayf,Chycnm)", "(Iidh,Qvjp)", "(Dnsay,Rngl)", "(Qweye,Tlv)", "(Wzyyim,Kxutz)", "(Hvueqc,Qejo)", "(Tlv,Ghc)", "(Hvia,Fvkhz)", "(Msyr,Owk)"])
