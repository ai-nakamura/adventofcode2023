# setup
f = open("day1input.txt", "r")
test = f.read().split()


def first_num(calibration_value):
    for char in calibration_value:
        if char.isnumeric():
            return char
    return ''


def last_num(calibration_value):
    for char in calibration_value[::-1]:
        if char.isnumeric():
            return char
    return ''


total_calibration_value = 0
for item in test:
    value = f"{first_num(item)}{last_num(item)}"
    total_calibration_value += int(value)

print(total_calibration_value)
