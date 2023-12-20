calibration_value = 0

with open("calibration document.txt", "r") as file:
    for line in file:
        digits_in_line = ""
        while len(line) > 0:
            if line.startswith("1"):
                digits_in_line = digits_in_line + "1"
            elif line.startswith("2"):
                digits_in_line = digits_in_line + "2"
            elif line.startswith("3"):
                digits_in_line = digits_in_line + "3"
            elif line.startswith("4"):
                digits_in_line = digits_in_line + "4"
            elif line.startswith("5"):
                digits_in_line = digits_in_line + "5"
            elif line.startswith("6"):
                digits_in_line = digits_in_line + "6"
            elif line.startswith("7"):
                digits_in_line = digits_in_line + "7"
            elif line.startswith("8"):
                digits_in_line = digits_in_line + "8"
            elif line.startswith("9"):
                digits_in_line = digits_in_line + "9"
            elif line.startswith("one"):
                digits_in_line = digits_in_line + "1"
            elif line.startswith("two"):
                digits_in_line = digits_in_line + "2"
            elif line.startswith("three"):
                digits_in_line = digits_in_line + "3"
            elif line.startswith("four"):
                digits_in_line = digits_in_line + "4"
            elif line.startswith("five"):
                digits_in_line = digits_in_line + "5"
            elif line.startswith("six"):
                digits_in_line = digits_in_line + "6"
            elif line.startswith("seven"):
                digits_in_line = digits_in_line + "7"
            elif line.startswith("eight"):
                digits_in_line = digits_in_line + "8"
            elif line.startswith("nine"):
                digits_in_line = digits_in_line + "9"
            line = line[1:]
        first_digit = int(digits_in_line[0]) * 10
        second_digit = int(digits_in_line[-1])
        value = first_digit + second_digit
        calibration_value = calibration_value + value
print(calibration_value)
