with open("puzzle_9-10_input.txt", "r") as file:
    input = file.read()
    rules, updates = input.split("\n\n")
    rules_by_line = rules.split("\n")
    updates_by_line = updates.split("\n")
    updates_by_line.pop()

    before, after = rules_by_line[0].split("|")
    before = int(before)
    after = int(after)
    template = [before, after]
    out = []
    for update_line in updates_by_line:
        pages = update_line.split(",")
        mid_idx = (len(pages) - 1) // 2
        relevant_rules_1 = []
        relevant_rules_2 = []
        for page in pages:
            relevant_rules_1.extend([rule for rule in rules_by_line if page in rule])
        for rule in relevant_rules_1:
            b, a = rule.split("|")
            if b in pages and a in pages:
                relevant_rules_2.append(rule)
        update_passes = True
        for rule in relevant_rules_2:
            b, a = rule.split("|")
            if pages.index(b) < pages.index(a):
                pass
            else:
                update_passes = False
        if update_passes:
            out.append(int(pages[mid_idx]))
    print(out)
    print(sum(out))