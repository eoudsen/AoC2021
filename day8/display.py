from collections import Counter


class Display:

    def __init__(self, left_digits, right_digits):
        self.zero = ""
        self.one = ""
        self.two = ""
        self.three = ""
        self.four = ""
        self.five = ""
        self.six = ""
        self.seven = ""
        self.eight = ""
        self.nine = ""
        self.bottom_left = ""
        self.bottom_right = ""
        self.top_right = ""
        self.result_number = 0
        for left_digit in left_digits:
            if len(left_digit) == 2:
                self.one = left_digit
            if len(left_digit) == 3:
                self.seven = left_digit
            if len(left_digit) == 4:
                self.four = left_digit
            if len(left_digit) == 7:
                self.eight = left_digit
        for digit in left_digits:
            if len(digit) == 6:
                for c in self.one:
                    if c not in digit:
                        self.six = digit
                        self.top_right = c
                        break

        for c in self.one:
            if c != self.top_right:
                self.bottom_right = c
                break
        final_map = Counter(''.join(left_digits))
        self.bottom_left = list(final_map.keys())[list(final_map.values()).index(4)]
        for digit in left_digits:
            if len(digit) == 5 and self.top_right not in digit and self.bottom_left not in digit:
                self.five = digit
            elif len(digit) == 5 and self.top_right in digit and self.bottom_left in digit and self.bottom_right not in digit:
                self.two = digit
            elif len(digit) == 6 and self.top_right in digit and self.bottom_left in digit and self.bottom_right in digit:
                self.zero = digit
            elif len(digit) == 6 and self.top_right in digit and self.bottom_left not in digit:
                self.nine = digit

        result_str = ""
        for right_digit in right_digits:
            if len(right_digit) == 2:
                result_str += "1"
                continue
            if len(right_digit) == 3:
                result_str += "7"
                continue
            if len(right_digit) == 4:
                result_str += "4"
                continue
            if len(right_digit) == 7:
                result_str += "8"
                continue
            if sorted(right_digit) == sorted(self.zero):
                result_str += "0"
                continue
            if sorted(right_digit) == sorted(self.two):
                result_str += "2"
                continue
            if sorted(right_digit) == sorted(self.five):
                result_str += "5"
                continue
            if sorted(right_digit) == sorted(self.six):
                result_str += "6"
                continue
            if sorted(right_digit) == sorted(self.nine):
                result_str += "9"
                continue
            result_str += "3"
        self.result_number = int(result_str)
