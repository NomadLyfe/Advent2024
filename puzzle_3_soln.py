with open("puzzle_3-4_input.txt", "r") as file:
    reports = file.read().split("\n")
    reports.pop()
    safe_reports = []
    for report in reports:
        prev_level = None
        prev_trend = None
        for level in [int(l) for l in report.split(" ")]:
            trend = None
            safe = True
            if prev_level:
                if abs(level - prev_level) <= 3:
                    if prev_level < level:
                        trend = "inc"
                        if trend == prev_trend or not prev_trend:
                            pass
                        else:
                            safe = False
                            break
                    elif prev_level > level:
                        trend = "dec"
                        if trend == prev_trend or not prev_trend:
                            pass
                        else:
                            safe = False
                            break
                    else:
                        safe = False
                        break
                else:
                    safe = False
                    break
            else:
                pass
            prev_level = level
            prev_trend = trend
        if safe:
            safe_reports.append(report)

print(len(safe_reports))