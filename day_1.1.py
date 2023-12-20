calibration_value = 0

with open("calibration document.txt", "r") as file:
    for line in file:
        digits_in_line = ""
        for character in line:
            if character.isdigit():
                digits_in_line = digits_in_line + character
        first_digit = int(digits_in_line[0]) * 10
        second_digit = int(digits_in_line[-1])
        value = first_digit + second_digit
        calibration_value = calibration_value + value
print(calibration_value)
