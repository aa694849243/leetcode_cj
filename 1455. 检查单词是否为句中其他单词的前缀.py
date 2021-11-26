# ����һ���ַ��� sentence ��Ϊ���Ӳ�ָ��������Ϊ searchWord �����о����������� �����ո� �ָ��ĵ�����ɡ�
#
#  ����������� searchWord �Ƿ�Ϊ���� sentence �����ⵥ�ʵ�ǰ׺��
#
#
#  ��� searchWord ��ĳһ�����ʵ�ǰ׺���򷵻ؾ��� sentence �иõ�������Ӧ���±꣨�±�� 1 ��ʼ����
#  ��� searchWord �Ƕ�����ʵ�ǰ׺���򷵻�ƥ��ĵ�һ�����ʵ��±꣨��С�±꣩��
#  ��� searchWord �����κε��ʵ�ǰ׺���򷵻� -1 ��
#
#
#  �ַ��� S �� ǰ׺ �� S ���κ�ǰ���������ַ�����
#
#
#
#  ʾ�� 1��
#
#
# ���룺sentence = "i love eating burger", searchWord = "burg"
# �����4
# ���ͣ�"burg" �� "burger" ��ǰ׺���� "burger" �Ǿ����е� 4 �����ʡ�
#
#  ʾ�� 2��
#
#
# ���룺sentence = "this problem is an easy problem", searchWord = "pro"
# �����2
# ���ͣ�"pro" �� "problem" ��ǰ׺���� "problem" �Ǿ����е� 2 ��Ҳ�ǵ� 6 �����ʣ�����Ӧ�÷�����С�±� 2 ��
#
#
#  ʾ�� 3��
#
#
# ���룺sentence = "i am tired", searchWord = "you"
# �����-1
# ���ͣ�"you" ���Ǿ������κε��ʵ�ǰ׺��
#
#
#  ʾ�� 4��
#
#
# ���룺sentence = "i use triple pillow", searchWord = "pill"
# �����4
#
#
#  ʾ�� 5��
#
#
# ���룺sentence = "hello from the other side", searchWord = "they"
# �����-1
#
#
#
#
#  ��ʾ��
#
#
#  1 <= sentence.length <= 100
#  1 <= searchWord.length <= 10
#  sentence ��СдӢ����ĸ�Ϳո���ɡ�
#  searchWord ��СдӢ����ĸ��ɡ�
#  ǰ׺���ǽ��ܸ����ڴʸ������أ��м䲻�ܲ��������ɷ֣���������λ���ǹ̶��ġ���-λ�ڴʸ�֮ǰ���������� ǰ׺_�ٶȰٿ� ��
#
#  Related Topics �ַ��� �ַ���ƥ�� ? 20 ? 0


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lst = sentence.split()
        for i,word in enumerate(lst):
            if word.startswith(searchWord):
                return i+1
        return -1