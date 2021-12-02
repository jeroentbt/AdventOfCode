import intcodecomputer
import unittest


class TestIntCodeComputer(unittest.TestCase):

    def test_convert_string_to_list_of_ints(self):
        self.assertEqual(intcodecomputer.stringToListOfInts('1,2,3'), [1, 2, 3])

    def test_convert_list_of_ints_to_string(self):
        self.assertEqual(intcodecomputer.listOfIntsToString([1, 2, 3]), '1,2,3')

    def test_addition(self):
        self.assertListEqual(intcodecomputer.runProgram([1,0,0,0,99]), [2,0,0,0,99])

    def test_multiplication(self):
        self.assertListEqual(intcodecomputer.runProgram([2,3,0,3,99]), [2,3,0,6,99])
        self.assertListEqual(intcodecomputer.runProgram([2,4,4,5,99,0]), [2,4,4,5,99,9801])

    def test_end(self):
        self.assertListEqual(intcodecomputer.runProgram([99,0,0,3,99]), [99,0,0,3,99])

    def test_mutliple_opcodes(self):
        self.assertListEqual(
            intcodecomputer.runProgram([1,9,10,3,2,3,11,0,99,30,40,50]),
            [3500,9,10,70,2,3,11,0,99,30,40,50])
        self.assertListEqual(
            intcodecomputer.runProgram([1,1,1,4,99,5,6,0,99]),
            [30,1,1,4,2,5,6,0,99])

if __name__ == '__main__':
    unittest.main()
