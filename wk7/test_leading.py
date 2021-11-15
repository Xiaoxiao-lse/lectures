import unittest
import leading

class Testleading_substrings(unittest.TestCase):
    '''Tests for leading_substrings'''
    def test_empty(self):
        inputted=""
        outputted=leading.substrings(inputted)
        output_expected=[]
        self.assertEqual(output_expected, outputted, "The list is empty.")
    def test_single(self):
        inputted="x"
        outputted=leading.substrings(inputted)
        output_expected=["x"]
        self.assertEqual(output_expected, outputted, "The list contains one term")
    def test_with_space(self):
        inputted="ab c"
        outputted=leading.substrings(inputted)
        output_expected=["a","ab","ab ","ab c"]
        self.assertEqual(output_expected, outputted, "The list contains one element with space")


if __name__ == '__main__':
    unittest.main()
