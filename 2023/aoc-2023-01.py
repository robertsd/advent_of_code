from functools import reduce, partial


with open("aoc-001.txt") as f:
    read_data = f.readlines()


def find_first_number(num_string, words_as_numbers = True):
    if words_as_numbers:
        num_string = num_string.replace("one", "1") \
                                .replace("two", "2") \
                                .replace("three", "3") \
                                .replace("four", "4") \
                                .replace("five", "5") \
                                .replace("six", "6") \
                                .replace("seven", "7") \
                                .replace("eight", "8") \
                                .replace("nine", "9")
    num = ''.join(filter(str.isnumeric, num_string))
    return num


def scan_for_numbers(num_string, side="left", **kwargs):
    num_found = False
    pos = 0 if side == "left" else len(num_string)
    while (not num_found):
        try_string = num_string[:pos] if side =="left" else num_string[pos:]
        result = find_first_number(try_string, **kwargs)
        if (len(result)> 0):
                num_found = True
        if side == "left":        
            pos += 1
        else:
            pos -= 1
    return result


def calibration(num_string, words_as_numbers=True):
     return int(
                scan_for_numbers(num_string, "left", words_as_numbers = words_as_numbers) + \
                scan_for_numbers(num_string, "right", words_as_numbers = words_as_numbers)
                )


def solve(words_as_numbers):
    mapfunc = partial(calibration, words_as_numbers=words_as_numbers)
    calibrations = map(mapfunc, read_data)
    return reduce(lambda x, y: x + y, calibrations)


print(solve(False), solve(True))



