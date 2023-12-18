class LastNotRepetitiveChar:
    def __init__(self, lst):
        my_ans = []
        for s in lst:
            my_ans.append(self.get_last_rep_char(s))
        return my_ans

    def get_last_rep_char(self, s):
        d = {}
        last_non_rep = None
        for i in s:
            if d.get(i):
                if last_non_rep == i:
                    last_non_rep = None
            else:
                d[i] = 1
                last_non_rep = i
        return last_non_rep


class Test_Class:
    def __init__(self):
        # self.invoke_all_postive_tests()
        # self.invoke_all_negative_tests()
        self.test1()

    def test1(self):
        l = ['Abc', 'abcabc', 'abcdeabc', 'abaabcdef']
        actual_ans = ['c', None, 'e', 'f']
        assert LastNotRepetitiveChar(l) == actual_ans


if __name__ == '__main__':
    Test_Class()
