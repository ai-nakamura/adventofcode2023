# setup
f = open("day1input.txt", "r")
test = f.read().split()

alpha_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
starting_char = ["o", "t", "f", "s", "e", "n"]


def first_num(calibration_value):
    for idx, char in enumerate(calibration_value):
        if char.isnumeric():
            return char
        if char in starting_char:
            try:
                substring = calibration_value[idx:idx+5]
                for s in substring:
                    if s.isnumeric():
                        return s
                    for digit in alpha_num:
                        if digit in substring and digit.startswith(s):
                            return alpha_num[digit]
            except IndexError:
                pass
    return ''


def last_num(calibration_value):
    for idx, char in enumerate(calibration_value[::-1]):
        if char.isnumeric():
            return char
        if char in starting_char:
            try:
                fix_idx = len(calibration_value) - 1
                substring = calibration_value[fix_idx - idx:fix_idx - idx + 5]
                for digit in alpha_num:
                    if digit in substring:
                        return alpha_num[digit]
            except IndexError:
                pass
    return ''


# t = "vbtwonebffmphmxdeighttwo6sevenrvsqjthree"
# t2 = "fbprf9twonccnkkdf98eight"
# t3 = "xhvsst4twoxvkrjgjtzs5bxgqhvrkrl"
# t4 = "one22sevenp5"
# print(f"{first_num(t)}{last_num(t)}")
# print(f"{first_num(t2)}{last_num(t2)}")
# print(f"{first_num(t3)}{last_num(t3)}")
# print(f"{first_num(t4)}{last_num(t4)}")

total_calibration_value = 0
for item in test:
    value = f"{first_num(item)}{last_num(item)}"
    total_calibration_value += int(value)
print(total_calibration_value)
