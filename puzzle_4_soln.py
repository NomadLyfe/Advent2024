def check_if_safe(arr):
    prev_level = None
    prev_trend = None
    safe = True
    trends = []
    for level in arr:
        trend = None
        if prev_level:
            diff = abs(level - prev_level)
            if diff <= 3:
                if prev_level < level:
                    trend = "inc"
                    if trend == prev_trend or not prev_trend:
                        pass
                    else:
                        safe = False
                    trends.append((trend, True))
                elif prev_level > level:
                    trend = "dec"
                    if trend == prev_trend or not prev_trend:
                        pass
                    else:
                        safe = False
                    trends.append((trend, True))
                else:
                    safe = False
                    trend = False
                    trends.append((trend, False))
            else:
                safe = False
                if prev_level < level:
                    trend = "inc"
                    trends.append((trend, False))
                else:
                    trend = "dec"
                    trends.append((trend, False))
        else:
            pass
        prev_level = level
        prev_trend = trend
    return safe, trends

with open("puzzle_3-4_input.txt", "r") as file:
    reports = file.read().split("\n")
    reports.pop()
    safe_reports = []
    for report in reports:
        safe, trends = check_if_safe([int(l) for l in report.split(" ")])
        if safe:
            safe_reports.append(report)
        else:
            report_as_ints = [int(l) for l in report.split(" ")]
            for i, level in enumerate(report_as_ints):
                a = [int(l) for l in report.split(" ")]
                a.pop(i)
                safe, trends = check_if_safe(a)
                if safe:
                    safe_reports.append(report)
                    break

    print(len(safe_reports))
