# time complexity:  O(n*m^2)  (ignoring initial data parsing from file)
# space complexity: O(n) (ignoring inputs)

def read_input():
    reports = []
    with open('01-input-data') as f:
        for line in f:
            levels = []
            split_line = ' '.join(line.split()).split(' ')

            for n in split_line:
                levels.append(int(n))
            
            reports.append(levels)

    return reports

# O(m)
def is_safe(levels):
    safe = True
    increasing = levels[0] < levels[1]

    for r in range(1, len(levels)):
        diff = levels[r] - levels[r - 1]

        if abs(diff) > 3 or diff == 0 or (increasing and diff < 0) or (not increasing and diff > 0):
            safe = False
            break

    return safe

# O(n*m^2)
def process():
    safe_reports = 0

    for report in reports:
        safe_reports += 1 if is_safe(report) or any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report))) else 0 # brute forcing to the win :(

    return safe_reports

reports = read_input()

print(process())
