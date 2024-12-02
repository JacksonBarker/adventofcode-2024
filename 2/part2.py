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
    if not is_safe:
        for i in range(0, len(report)):
            damped = report.copy()
            damped.pop(i)
            increasing = damped[0] - damped[1] < 0
            damped_safe = True
            for j in range(1, len(damped)):
                if not 1 <= abs(damped[j-1] - damped[j]) <= 3 or (damped[j-1] - damped[j] < 0) != increasing:
                    damped_safe = False
                    break
            if damped_safe:
                is_safe = True
                break
    if is_safe:
        safe += 1

print(safe)
