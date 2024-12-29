def get_level_difference(level_one: int, level_two: int) -> int:
    """Returns the difference between two values"""
    return abs(int(level_one) - int(level_two))

def is_report_safe(report: []) -> bool:
    """Returns true if levels aren't all increasing/decreasing
    OR any two adjacent levels differ by zero or more than three"""
    levels_increasing = True
    levels_decreasing = True
    last_number = 0

    for i in range(len(report)):
        current_number = int(report[i])
        if i > 0:
            # report is unsafe if any consecutive numbers are equal
            if last_number == current_number:
                return False

            # report is unsafe if all numbers don't increment/decrement
            levels_increasing &= last_number < current_number
            levels_decreasing &= last_number > current_number
            if not levels_increasing and not levels_decreasing:
                return False

            # report is unsafe if any consecutive numbers have difference greater than three
            level_difference = get_level_difference(last_number, current_number)
            if level_difference < 1 or level_difference > 3:
                return False

        last_number = current_number
    return True

safe_reports = 0
with open('unusual_data.txt') as input_file:
    for row in input_file.readlines():
        if is_report_safe(row.replace('\n','').split(' ')):
            safe_reports += 1

print(safe_reports)
