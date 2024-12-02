# time complexity: O(n)  (ignoring initial data parsing from file)
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

def process():
    safe_reports = 0

    for report in reports:
        diffs = [report[r] - report[r - 1] for r in range(1, len(report))]
        d = {
            'positives': 0,
            'negatives': 0,
            'invalid': 0,
        }

        for diff in diffs:
            if diff > 0:
                d['positives'] += 1
            elif diff < 0:
                d['negatives'] += 1

            if abs(diff) > 3 or (d['positives'] > 0 and d['negatives'] > 0) or diff == 0:
                d['invalid'] += 1
        
        if d['invalid'] == 0:
            safe_reports += 1

    return safe_reports

# def process():
#     safe_reports = 0

#     for report in reports:
#         safe = True
#         increasing = report[0] < report[1]

#         for r in range(1, len(report)):
#             diff = report[r] - report[r - 1]

#             if abs(diff) > 3 or diff == 0 or (increasing and diff < 0) or (not increasing and diff > 0):
#                 safe = False
#                 break

#         if safe:
#             safe_reports += 1

#     return safe_reports

reports = read_input()

print(process())
