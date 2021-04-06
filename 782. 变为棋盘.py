'''一个 N x N的 board 仅由 0 和 1 组成 。每次移动，你能任意交换两列或是两行的位置。

输出将这个矩阵变为 “棋盘” 所需的最小移动次数。“棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。如果不存在可行的变换，输出 -1。

示例:
输入: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
输出: 2
解释:
一种可行的变换方式如下，从左到右：

0110     1010     1010
0110 --> 1010 --> 0101
1001     0101     1010
1001     0101     0101

第一次移动交换了第一列和第二列。
第二次移动交换了第二行和第三行。


输入: board = [[0, 1], [1, 0]]
输出: 0
解释:
注意左上角的格值为0时也是合法的棋盘，如：

01
10

也是合法的棋盘.

输入: board = [[1, 0], [1, 0]]
输出: -1
解释:
任意的变换都不能使这个输入变为合法的棋盘。
 

提示：

board 是方阵，且行列数的范围是[2, 30]。
board[i][j] 将只包含 0或 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/transform-to-chessboard
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


# 因为行变换，行的排列不会变，而列变换后对行的影响是等于0的，因为假如两行是相同的，无论行变换还是列变换，这两行还是相同的，如果是不同的，变换后还是不同的
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        N = len(board)
        ans = 0
        for count in (collections.Counter(map(tuple, board)), collections.Counter(zip(*board))):
            # (count里面有两条序列，两条行序列和两条列序列）
            if len(count) != 2 or sorted(count.values()) != [N // 2, (N + 1) // 2]:
                return -1
            line1, line2 = count
            if not all(x ^ y for (x, y) in zip(line1, line2)):#两条线必须要完全错开才行，如果11（竖着相同）那么无论横变换还是竖变换都无法使它们不同
                return -1
            starts = [+(line1.count(1) * 2 > N)] if N % 2 else [0, 1] #如果偶数，则0开始和1开始都要试一下，如果奇数则以数量多的那个数开始
            ans += min(sum((i - x) % 2 for i, x in enumerate(line1, start)) for start in starts)//2
            #(i-x)%2表示i与x异奇偶的数量，假如以0开始则一定是同奇偶的（那我们计算异奇偶的数量-表示错误的位置），以1开始就是异奇偶是正确的
        return ans
