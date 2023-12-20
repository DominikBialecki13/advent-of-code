calibration_value = 0

digit_map = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
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

with open("calibration document.txt", "r") as file:
    for line in file:
        digits_in_line = ""
        while len(line) > 0:
            for digit in digit_map:
                if line.startswith(digit):
                    digits_in_line += digit_map[digit]
                    break
            line = line[1:]
        first_digit = int(digits_in_line[0]) * 10
        second_digit = int(digits_in_line[-1])
        value = first_digit + second_digit
        calibration_value += value
        
print(calibration_value)
