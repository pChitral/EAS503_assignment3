import unittest
import os
import assignment3
from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestAssignment3(unittest.TestCase):
    def setUp(self):
        self.assignment3 = assignment3

    @weight(1)
    @visibility('visible')
    @number("1.1")
    def test_ex1_1(self):
        value = self.assignment3.ex1('test1234')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("1.2")
    def test_ex1_2(self):
        value = self.assignment3.ex1('password123')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("1.3")
    def test_ex1_3(self):
        value = self.assignment3.ex1('SuperPasswrd90')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("1.4")
    def test_ex1_4(self):
        value = self.assignment3.ex1('letmein!')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("1.5")
    def test_ex1_5(self):
        value = self.assignment3.ex1('Password123@!')
        self.assertEqual(True, value)

    @weight(1)
    @visibility('visible')
    @number("1.6")
    def test_ex1_6(self):
        value = self.assignment3.ex1('InWard@1234')
        self.assertEqual(True, value)

    @weight(1)
    @visibility('visible')
    @number("1.7")
    def test_ex1_7(self):
        value = self.assignment3.ex1('Test3451')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("1.8")
    def test_ex1_8(self):
        value = self.assignment3.ex1('AnandTech!892')
        self.assertEqual(True, value)

    @weight(1)
    @visibility('visible')
    @number("1.9")
    def test_ex1_9(self):
        value = self.assignment3.ex1('aaaaaaaaaaaaaa')
        self.assertEqual(False, value)

    @weight(1)
    @visibility('visible')
    @number("1.10")
    def test_ex1_10(self):
        value = self.assignment3.ex1('12345!')
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("2.1")
    def test_ex2_1(self):
        value = self.assignment3.ex2('This is a test sentence!')
        self.assertEqual(4, value)

    @weight(3)
    @visibility('visible')
    @number("2.2")
    def test_ex2_2(self):
        value = self.assignment3.ex2('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        self.assertEqual(5.46, value)

    @weight(3)
    @visibility('visible')
    @number("3.1")
    def test_ex3_1(self):
        value = self.assignment3.ex3('ex3_data.txt')
        self.assertEqual((50, 643, 4298), value)

    @weight(3)
    @visibility('visible')
    @number("4.1")
    def test_ex4_1(self):
        value = self.assignment3.ex4(0.06)
        self.assertEqual(12, value)

    @weight(3)
    @visibility('visible')
    @number("4.2")
    def test_ex4_2(self):
        value = self.assignment3.ex4(0.1)
        self.assertEqual(8, value)

    @weight(3)
    @visibility('visible')
    @number("5.1")
    def test_ex5_1(self):
        value = self.assignment3.ex5(15)
        self.assertEqual(17, value)

    @weight(3)
    @visibility('visible')
    @number("5.2")
    def test_ex5_2(self):
        value = self.assignment3.ex5(35)
        self.assertEqual(13, value)

    @weight(3)
    @visibility('visible')
    @number("5.3")
    def test_ex5_3(self):
        value = self.assignment3.ex5(12)
        self.assertEqual(9, value)

    @weight(3)
    @visibility('visible')
    @number("5.4")
    def test_ex5_4(self):
        value = self.assignment3.ex5(27)
        self.assertEqual(111, value)

    @weight(3)
    @visibility('visible')
    @number("6.1")
    def test_ex6_1(self):
        value = self.assignment3.ex6(2)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("6.2")
    def test_ex6_2(self):
        value = self.assignment3.ex6(3)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("6.3")
    def test_ex6_3(self):
        value = self.assignment3.ex6(5)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("6.4")
    def test_ex6_4(self):
        value = self.assignment3.ex6(25)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("7.1")
    def test_ex7_1(self):
        value = self.assignment3.ex7(5)
        self.assertEqual([3, 5], value)

    @weight(3)
    @visibility('visible')
    @number("7.2")
    def test_ex7_2(self):
        value = self.assignment3.ex7(25)
        self.assertEqual([3, 5, 7, 11, 13, 17, 19, 23], value)

    @weight(3)
    @visibility('visible')
    @number("8.1")
    def test_ex8_1(self):
        value = self.assignment3.ex8(25, 75)
        self.assertEqual(25, value)

    @weight(3)
    @visibility('visible')
    @number("8.2")
    def test_ex8_2(self):
        value = self.assignment3.ex8(3, 13)
        self.assertEqual(1, value)

    @weight(3)
    @visibility('visible')
    @number("8.3")
    def test_ex8_3(self):
        value = self.assignment3.ex8(24, 62)
        self.assertEqual(2, value)

    @weight(3)
    @visibility('visible')
    @number("8.4")
    def test_ex8_4(self):
        value = self.assignment3.ex8(24, 48)
        self.assertEqual(24, value)

    @weight(3)
    @visibility('visible')
    @number("9.1")
    def test_ex9_1(self):
        value = self.assignment3.ex9('ex9_data.txt')
        self.assertEqual(('student733', 86.2, 'student202', 65.4), value)

    @weight(3)
    @visibility('visible')
    @number("10.1")
    def test_ex10_1(self):
        import random
        random.seed(1234)
        data = [random.randint(50, 150) for ele in range(100)]
        data[45] = 1
        data[46] = 2
        data[90] = 250
        data[34] = 300

        result = [50, 50, 51, 52, 52, 52, 53, 53, 54,
                  55, 55, 55, 55, 56, 58, 58, 59, 59, 59, 60, 61, 61,
                  61, 62, 64, 64, 64, 68, 68, 68, 69, 69, 69, 70, 71,
                  72, 73, 75, 77, 80, 81, 81, 84, 84, 84, 85, 88, 88, 89,
                  92, 94, 94, 95, 95, 98, 103, 106, 108, 108, 109, 109, 109,
                  110, 111, 111, 112, 113, 114, 115, 115, 117, 117, 119, 121,
                  124, 124, 125, 126, 128, 129, 132, 132, 133, 134, 135, 135,
                  135, 136, 138, 140, 141, 148, 148, 149, 149, 150]
        value = self.assignment3.ex10(data, 2)

        self.assertEqual(result, value)

    @weight(3)
    @visibility('visible')
    @number("10.2")
    def test_ex10_2(self):
        import random
        random.seed(1234)
        data = [random.randint(250, 450) for ele in range(100)]
        data[45] = 90
        data[46] = 76
        data[90] = 800
        data[34] = 900

        result = [251, 251, 253, 254, 254, 254, 256, 257, 258, 260,
                  260, 261, 263, 266, 267, 268, 269, 269, 271, 272, 273, 273,
                  275, 278, 279, 279, 286, 286, 286, 288, 289, 289, 291, 292,
                  295, 296, 301, 305, 310, 313, 313, 318, 319, 319, 320, 326,
                  327, 328, 335, 338, 338, 340, 340, 346, 356, 362, 366, 366,
                  368, 368, 369, 371, 373, 373, 374, 377, 378, 380, 381, 385,
                  385, 392, 392, 394, 398, 399, 400, 403, 407, 409, 415, 417,
                  418, 419, 420, 420, 421, 421, 422, 427, 431, 432, 446, 447, 449, 449]

        value = self.assignment3.ex10(data, 2)
        self.assertEqual(result, value)

    @weight(3)
    @visibility('visible')
    @number("11.1")
    def test_ex11_1(self):
        value = self.assignment3.ex11(
            [21, 21, 1, 2, 3, 3, 3, 4, 5, 6, 7, 7, 8])
        self.assertEqual([21, 1, 2, 3, 4, 5, 6, 7, 8], value)

    @weight(3)
    @visibility('visible')
    @number("11.2")
    def test_ex11_2(self):
        value = self.assignment3.ex11(
            ['The', 'Man', 'The', 'Boy', 'Output', 'The', 'Man'])
        self.assertEqual(['The', 'Man', 'Boy', 'Output'], value)

    @weight(3)
    @visibility('visible')
    @number("12.1")
    def test_ex12_1(self):
        value = self.assignment3.ex12(28)
        self.assertEqual([1, 2, 4, 7, 14], value)

    @weight(3)
    @visibility('visible')
    @number("12.2")
    def test_ex12_2(self):
        value = self.assignment3.ex12(496)
        self.assertEqual([1, 2, 4, 8, 16, 31, 62, 124, 248], value)

    @weight(3)
    @visibility('visible')
    @number("13.1")
    def test_ex13_1(self):
        value = self.assignment3.ex13(28)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("13.2")
    def test_ex13_2(self):
        value = self.assignment3.ex13(76)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("13.3")
    def test_ex13_3(self):
        value = self.assignment3.ex13(496)
        self.assertEqual(True, value)

    @weight(3)
    @visibility('visible')
    @number("13.4")
    def test_ex13_4(self):
        value = self.assignment3.ex13(512)
        self.assertEqual(False, value)

    @weight(3)
    @visibility('visible')
    @number("14.1")
    def test_ex14_1(self):
        points = (
            (8, 3),
            (2, 10),
            (11, 3),
            (6, 6),
            (5, 8),
            (4, 12),
            (12, 1),
            (9, 4),
            (6, 9),
            (1, 14),
        )
        value = self.assignment3.ex14(points)
        self.assertEqual((-1.11, 14.08), value)

    @weight(3)
    @visibility('visible')
    @number("14.2")
    def test_ex14_2(self):
        points = (
            (3, 8),
            (10, 2),
            (3, 11),
            (6, 6),
            (8, 5),
            (12, 4),
            (1, 12),
            (4, 9),
            (9, 6),
            (14, 1),
        )
        value = self.assignment3.ex14(points)
        self.assertEqual((-0.79, 11.92), value)

    @weight(10)
    @visibility('visible')
    @number("15.1")
    def test_ex15_1(self):
        title = 'Cereal Yields (kg/ha)'
        header = ('Country', '1980', '1990', '2000', '2010')
        data = (
            ('China', 2937, 4321, 4752, 5527),
            ('Germany', 4225, 5411, 6453, 6718),
            ('United States', 3772, 4755, 5854, 6988),
        )
        if os.path.exists('ex15_1.txt'):
            os.remove('ex15_1.txt')
        self.assignment3.ex15(title, header, data, 'ex15_1.txt')
        expected_result = open('ex15_1_solution.txt').read()
        actual_result = open('ex15_1.txt').read()
        self.assertEqual(expected_result, actual_result)

    @weight(10)
    @visibility('visible')
    @number("15.2")
    def test_ex15_2(self):
        title = 'MOST ACTIVE BY SHARE VOLUME'
        header = ('Symbol', 'Name', 'Last', 'Change', 'Share Volume')
        data = (
            ('AMD', 'Advanced Micro Devices, Inc.',
             '$120.88', '+4.27', '121,475,927'),
            ('AAPL', 'Apple Inc.', '$164.71', '+1.97', '80,725,613'),
            ('OPEN', 'Opendoor Technologies Inc', '$8.42', '-2.55', '53,559,847'),
            ('NVDA', 'NVIDIA Corporation', '$240.82', '+3.34', '49,046,544'),
            ('ZNGA', 'Zynga Inc.', '$9.18', '+0.37', '48,193,380'),
        )
        if os.path.exists('ex15_2.txt'):
            os.remove('ex15_2.txt')
        self.assignment3.ex15(title, header, data, 'ex15_2.txt')
        expected_result = open('ex15_2_solution.txt').read()
        actual_result = open('ex15_2.txt').read()
        self.assertEqual(expected_result, actual_result)

    @weight(10)
    @visibility('visible')
    @number("15.3")
    def test_ex15_3(self):
        title = 'Student Grades'
        header = ('Student ID', 'Test1', 'Test2',
                  'Midterm', 'Quizzes', 'Final')
        data = (
            (2014255, 55, 78, 63, 50, 80),
            (2014301, 83, 45, 88, 52, 47),
            (2014023, 75, 70, 42, 74, 63),
            (2014155, 67, 87, 54, 87, 86),
        )
        if os.path.exists('ex15_3.txt'):
            os.remove('ex15_3.txt')
        self.assignment3.ex15(title, header, data, 'ex15_3.txt')
        expected_result = open('ex15_3_solution.txt').read()
        actual_result = open('ex15_3.txt').read()
        self.assertEqual(expected_result, actual_result)

    @weight(3)
    @visibility('visible')
    @number("16.1")
    def test_ex16_1(self):
        value = self.assignment3.ex16(range(1, 20))
        self.assertEqual([3, 4, 6, 8, 9, 12, 15, 16, 18], value)

    @weight(3)
    @visibility('visible')
    @number("16.2")
    def test_ex16_2(self):
        value = self.assignment3.ex16(range(101, 140))
        self.assertEqual([
            102,
            104,
            105,
            108,
            111,
            112,
            114,
            116,
            117,
            120,
            123,
            124,
            126,
            128,
            129,
            132,
            135,
            136,
            138], value)

    @weight(3)
    @visibility('visible')
    @number("17.1")
    def test_ex17_1(self):
        value = self.assignment3.ex17(range(20))
        expected_value = [
            0, 5, 6, 15, 12,
            25, 18, 35, 24, 45,
            30, 55, 36, 65, 42,
            75, 48, 85, 54, 95
        ]
        self.assertEqual(expected_value, value)

    @weight(3)
    @visibility('visible')
    @number("17.2")
    def test_ex17_2(self):
        value = self.assignment3.ex17(range(200, 220))
        expected_value = [
            600, 1005, 606, 1015,
            612, 1025, 618, 1035,
            624, 1045, 630, 1055,
            636, 1065, 642, 1075, 648, 1085, 654, 1095]

        self.assertEqual(expected_value, value)

    @weight(3)
    @visibility('visible')
    @number("18.1")
    def test_ex18_1(self):
        input_dict = {
            'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31,
        }
        value = self.assignment3.ex18(input_dict, 31)
        expected_value = ['January', 'March', 'May',
                          'July', 'August', 'October', 'December']
        self.assertEqual(expected_value, value)

    @weight(3)
    @visibility('visible')
    @number("18.2")
    def test_ex18_2(self):
        input_dict = {
            'January': 31,
            'February': 28,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31,
        }
        value = self.assignment3.ex18(input_dict, 30)
        expected_value = ['April', 'June', 'September', 'November']
        self.assertEqual(expected_value, value)

    @weight(3)
    @visibility('visible')
    @number("19.1")
    def test_ex19_1(self):
        value = self.assignment3.ex19('ex19_data_1.txt')
        expected_value = 0.499675
        self.assertEqual(expected_value, value)

    @weight(3)
    @visibility('visible')
    @number("19.2")
    def test_ex19_2(self):
        value = self.assignment3.ex19('ex19_data_2.txt')
        expected_value = round(0.49939999999999996, 6)
        self.assertEqual(expected_value, round(value, 6))

    @weight(3)
    @visibility('visible')
    @number("19.3")
    def test_ex19_3(self):
        value = self.assignment3.ex19('ex19_data_3.txt')
        expected_value = "The file does not have any valid number to compute the median"
        self.assertEqual(expected_value, value)


    @weight(5)
    @visibility('visible')
    @number("20.1")
    def test_ex20_1(self):
        value = self.assignment3.simulateProblem()
        expected_value = bool     
        self.assertEqual(type(value[0]), expected_value)

    @weight(5)
    @visibility('visible')
    @number("20.2")
    def test_ex20_2(self):
        value = self.assignment3.simulateProblem()
        expected_value = bool
        self.assertEqual(type(value[1]), expected_value)

    @weight(5)
    @visibility('visible')
    @number("20.3")
    def test_ex20_3(self):
        win_due_to_sticking, win_due_to_switching = self.assignment3.ex20()
        self.assertEqual(abs(win_due_to_sticking-0.25) < 0.05, True)

    @weight(5)
    @visibility('visible')
    @number("20.4")
    def test_ex20_4(self):
        win_due_to_sticking, win_due_to_switching = self.assignment3.ex20()
        self.assertEqual(abs(win_due_to_switching-0.25) < 0.05, True)




