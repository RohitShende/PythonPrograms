class Solution:
    # @param A : integer
    # @return a strings
    ascii_for_A = 64

    def convertToTitle(self, A):
        n = A
        res = []
        # print("for n=", n)
        while n > 0:
            # print(n)
            a = n % 26

            if a == 0:
                a = 26
                n = n-1

            # print(a, chr(a + self.ascii_for_A))
            n = n // 26
            res.append(chr(a + self.ascii_for_A))
        return ''.join(res)

if __name__ == '__main__':
    for i in range(40):
        print(i, Solution().convertToTitle(i))