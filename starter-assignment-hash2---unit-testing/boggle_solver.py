import unittest
from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["ABC", "ABDE", "CFI", "AEI", "CEG"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ABC", "ABDE", "CFI"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Normal_case_5x5(self):
        grid = [["T", "E", "S", "T", "S"],
                ["A", "B", "C", "D", "E"],
                ["F", "G", "H", "I", "J"],
                ["K", "L", "M", "N", "O"],
                ["P", "Q", "R", "S", "T"]]
        dictionary = ["TESTS", "ABCDE", "FGHIJ", "KLMNO", "PQRST"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["TESTS", "ABCDE", "FGHIJ", "KLMNO", "PQRST"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Normal_case_10x10(self):
        grid = [list("ABCDEFGHIJ") for _ in range(10)]
        dictionary = ["ABCDEFGHIJABCDEFGHIJ"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ABCDEFGHIJABCDEFGHIJ"]
        self.assertEqual(sorted(solution), sorted(expected))

class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["A", "B", "C"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []  # No words of length >= 3
        self.assertEqual(sorted(solution), sorted(expected))

    def test_EmptyGrid_case_0x0(self):
        grid = []
        dictionary = ["HELLO", "THERE"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Word_That_Take_The_Entire_Grid(self):
        grid = [["A", "B", "S", "T"],
                ["E", "M", "I", "O"],
                ["U", "S", "N", "E"],
                ["S", "S", "E", "S"]]
        dictionary = ["ABSTEMIOUSNESSES", "SESSENSUOIMETSBA"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []
        self.assertEqual(sorted(solution), sorted(expected))


class TestSuite_Qu(unittest.TestCase):

    def test_isValid_Grid(self):
        grid = [["Qu", "Qu"], ["Qu", "Qu"]]
        dictionary = ["QUQU", "QUQUQU"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["QUQU", "QUQUQU"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Simple_Qu_Case(self):
        grid = [["A", "Qu"], ["B", "C"]]
        dictionary = ["AQU", "QUA", "QUAC", "AQUC"]
        mygame = Boggle(grid, dictionary)
        solution = sorted(mygame.getSolution())
        expected = sorted(["AQU", "AQUC"])
        self.assertEqual(expected, solution)

    def test_Q_without_U_Case(self):
        grid = [["Q", "A"], ["B", "C"]]
        dictionary = ["QA", "QAB", "QAC"]
        mygame = Boggle(grid, dictionary)
        solution = sorted(mygame.getSolution())
        expected = sorted(["QA", "QAB", "QAC"])
        self.assertEqual(expected, solution)

    def test_Simple_St_Case(self):
        grid = [["St", "A"], ["B", "C"]]
        dictionary = ["STAB", "STACK", "STAR"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["STAB"]
        self.assertEqual(sorted(solution), sorted(expected))

class TestSuite_Complete_Coverage(unittest.TestCase):

    def test_All_Directions(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["ABE", "CFI", "ADG", "CEG", "AEI", "BDH", "GDA"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ABE", "CFI", "ADG", "CEG", "AEI"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Winding_Path(self):
        grid = [["A", "B", "C"],
                ["H", "G", "D"],
                ["I", "F", "E"]]
        dictionary = ["ABCDEFGHI"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ABCDEFGHI"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Returns_All_Matching_Words(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["AB", "ABC", "ABCD", "ABDC"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ABCD", "ABDC"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Recursive_Steps(self):
        grid = [["A", "A"], ["A", "A"]]
        dictionary = ["AAA", "AAAA"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["AAA", "AAAA"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Pathologically_Slow(self):
        grid = [["A", "A"], ["A", "A"]]
        dictionary = ["A" * 10]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["AAAAAAAAAA"]
        self.assertEqual(sorted(solution), sorted(expected))

class TestSuite_Simple_Edge_Cases_Extended(unittest.TestCase):

    def test_Duplicate_Letters_Immediate_Loop(self):
        grid = [["A", "A", "A"],
                ["A", "A", "A"],
                ["A", "A", "A"]]
        dictionary = ["AAA"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["AAA"]
        self.assertEqual(sorted(solution), sorted(expected))


    def test_Words_Cant_Cell_More_Than_Once(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["ABA", "BAB", "CAC"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []  # Words reuse cells, which is invalid
        self.assertEqual(sorted(solution), sorted(expected))

    def test_Words_That_Only_Are_3_or_More_Chars(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["AB", "ABC", "ABCD", "ABCDE"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ABC", "ABCD", "ABCDE"]
        self.assertEqual(sorted(solution), sorted(expected))

    def test_No_Words_In_Grid(self):
        grid = [["X", "Y", "Z"],
                ["Q", "W", "E"],
                ["R", "T", "Y"]]
        dictionary = ["APPLE", "BANANA", "CHERRY"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []
        self.assertEqual(sorted(solution), sorted(expected))

# Ensure that the test runner runs all tests
if __name__ == '__main__':
    unittest.main()