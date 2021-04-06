:'
给定一个文本文件 file.txt，请只打印这个文件中的第十行。

示例:

假设 file.txt 有如下内容：

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
你的脚本应当显示第十行：

Line 10
说明:
1. 如果文件少于十行，你应当输出什么？
2. 至少有三种不同的解法，请尝试尽可能多的方法来解题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/tenth-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'
grep -n "" file.txt | grep -w '10' | cut -d: -f2
sed -n '10p' file.txt
awk '{if(NR==10){print $0}}' file.txt

#作者：novice2master
#链接：https://leetcode-cn.com/problems/tenth-line/solution/ni-yun-xing-guo-ma-by-novice2master/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。