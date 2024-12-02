reports = []

with open("2/input.txt") as inpt:
    for line in inpt:
        report = []
        for reading in line.split():
            report.append(int(reading))
        reports.append(report)

safe = 0
for report in reports:
    increasing = report[0] - report[1] < 0
    is_safe = True
    for i in range(1, len(report)):
        if not 1 <= abs(report[i-1] - report[i]) <= 3 or (report[i-1] - report[i] < 0) != increasing:
            is_safe = False
            break
    if is_safe:
        safe += 1

print(safe)
