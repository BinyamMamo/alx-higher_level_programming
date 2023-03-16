#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or (not isinstance(roman_string, str)):
        return None
    base_nums = {
        "I": "1",
        "V": "5",
        "X": "10",
        "L": "50",
        "C": "100",
        "D": "100",
        "M": "1000"
    }
    special_nums = {
        "IV": "a",
        "IX": "b",
        "XL": "c",
        "XC": "d",
        "CD": "e",
        "CM": "f"
    }

    reference = {
        "a": "4",
        "b": "9",
        "c": "40",
        "d": "90",
        "e": "400",
        "f": "900"
    }

    num = 0
    for sp in special_nums.keys():
        roman_string = roman_string.replace(sp, special_nums[sp])
    roman_string = roman_string[::-1]
    for digit in roman_string:
        if digit in reference.keys():
            num += int(reference.get(digit))
        else:
            num += int(base_nums[digit])
    return num


# romans = ['MCCXCV', 'CCXCVIII', 'CDXXXVIII', 'CCLIV', 'CCCXXXV',
#           'MCCXCIV', 'CMLXVI', 'XXXV', 'CCCXCIII', 'CMLXXXVIII']
# for roman in romans:
#     print(roman, roman_to_int(roman))
