def is_report_safe(report):
    num_levels = len(report)
    if num_levels < 2:
        return True, -1

    decreasing = True if report[1] < report[0] else False
    for i, (x, y) in enumerate(zip(report[:num_levels-1], report[1:])):
        diff = y - x

        if abs(diff) > 3 or (decreasing and diff >= 0) or (not decreasing and diff <= 0):
            return False, i
    else:
        return True, -1

safe_reports = 0
safe_reports_tolerate = 0

with open('data/day_2_data.txt') as f:
    for line in f:
        report = list(map(int, line.strip().split(' ')))
        
        result, ind = is_report_safe(report)
        if result:
            safe_reports += 1
        else:
            if ind != 0:
                result, _ = is_report_safe(report[1:])
                if result:
                    safe_reports_tolerate += 1
                    continue

            result, _ = is_report_safe(report[:ind] + report[ind+1:])
            if result:
                safe_reports_tolerate += 1
                continue
            result, _ = is_report_safe(report[:ind+1] + report[ind+2:])
            if result:
                safe_reports_tolerate += 1
                continue


print(f'Safe reports = {safe_reports}')
print(f'Safe reports with tolerance = {safe_reports + safe_reports_tolerate}')