import unittest
import day4

class TestDay4(unittest.TestCase):

    def test_get_random_numbers(self):
        self.assertEqual(day4.get_random_numbers("day4input.txt"), [17, 2, 33, 86, 38, 41, 4, 34, 91, 61, 11, 81, 3, 59, 29, 71, 26, 44, 54, 89, 46, 9, 85, 62, 23, 76, 45, 24, 78, 14, 58, 48, 57, 40, 21, 49, 7, 99, 8, 56, 50, 19, 53, 55, 10, 94, 75, 68, 6, 83, 84, 88, 52, 80, 73, 74, 79, 36, 70, 28, 37, 0, 42, 98, 96, 92, 27, 90, 47, 20, 5, 77, 69, 93, 31, 30, 95, 25, 63, 65, 51, 72, 60, 16, 12, 64, 18, 13, 1, 35, 15, 66, 67, 43, 22, 87, 97, 32, 39, 82])
        self.assertEqual(day4.get_random_numbers("day4testinput.txt"), [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1])

    def test_get_board_array(self):
        test_board = [
            "10 27 53 91 86",
            "15 94 47 38 61",
            "32 68  8 88  9",
            "35 84  3  7 87",
            "62 78 90 66 64",
        ]
        self.assertEqual(day4.get_board_array(test_board),
            [
                [10, 27, 53, 91, 86],
                [15, 94, 47, 38, 61],
                [32, 68, 8, 88, 9],
                [35, 84, 3, 7, 87],
                [62, 78, 90, 66, 64]
            ]
        )

    def test_mark_number(self):
        test_marked_boards = [
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        ]
        test_board0 = [
            [0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0],
            [2, 0, 0, 0, 2]
        ]
        test_expected_marked_boards0 = [
            [
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1]
            ]
        ]
        test_board1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2]
        ]
        test_expected_marked_boards1 = [
            [
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1]
            ]
        ]

        self.assertEqual(day4.mark_number(2, test_board0, 0, test_marked_boards), test_expected_marked_boards0)
        self.assertEqual(day4.mark_number(2, test_board1, 0, test_marked_boards), 0)

    def test_check_bingo(self):
        test_board0 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        test_board1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1]
        ]
        test_board2 = [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1]
        ]

        self.assertEqual(day4.check_bingo(test_board0), False)
        self.assertEqual(day4.check_bingo(test_board1), True)
        self.assertEqual(day4.check_bingo(test_board2), True)

    def test_check_bingos(self):
        test_boards0 = [
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        ]
        test_boards1 = [
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1]
            ]
        ]

        self.assertEqual(day4.check_bingos(test_boards0), -1)
        self.assertEqual(day4.check_bingos(test_boards1), 1)

    def test_find_winning_board_number(self):
        file = "day4testinput.txt"
        random_numbers = day4.get_random_numbers(file)
        boards = day4.get_boards(file)
        marked_boards = day4.empty_boards(len(boards))
        winning_board_number = day4.find_winning_board_number(random_numbers, boards, marked_boards)[1]

        self.assertEqual(day4.check_bingo(marked_boards[winning_board_number]), True)

        file = "day4input.txt"
        random_numbers = day4.get_random_numbers(file)
        boards = day4.get_boards(file)
        marked_boards = day4.empty_boards(len(boards))
        winning_board_number = day4.find_winning_board_number(random_numbers, boards, marked_boards)[1]

        self.assertEqual(day4.check_bingo(marked_boards[winning_board_number]), True)

    def test_calculate_final_score(self):
        file = "day4testinput.txt"
        random_numbers = day4.get_random_numbers(file)
        boards = [
            [
                [3, 15, 0, 2, 22],
                [9, 18, 13, 17, 5],
                [19, 8, 7, 25, 23],
                [20, 11, 10, 24, 4],
                [14, 21, 16, 12, 6]
            ]
        ]
        marked_boards = [
            [
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
            ]
        ]
        winning_number = day4.find_winning_board_number(random_numbers, boards, marked_boards)[0]
        winning_board_number = day4.find_winning_board_number(random_numbers, boards, marked_boards)[1]

        self.assertEqual(day4.calculate_final_score(boards, marked_boards, winning_board_number, winning_number), 1946)

    def test_part1(self):
        self.assertEqual(day4.part1("day4testinput.txt"), 4512)
        self.assertEqual(day4.part1(), 38594)

    def test_part2(self):
        self.assertEqual(day4.part2("day4testinput.txt"), 1924)
        self.assertEqual(day4.part2(), 21184)

if __name__ == "__main__":
    unittest.main()