with open("puzzle_9-10_input.txt", "r") as file:
    input = file.read()
    rules, updates = input.split("\n\n")
    rules_by_line = rules.split("\n")
    updates_by_line = updates.split("\n")
    updates_by_line.pop()
    out = []
    for update_line in updates_by_line:
        pages = update_line.split(",")
        mid_idx = (len(pages) - 1) // 2
        relevant_rules_1 = []
        relevant_rules_2 = []
        for page in pages:
            relevant_rules_1.extend([rule for rule in rules_by_line if page in rule])
        relevant_rules_1 = list(dict.fromkeys(relevant_rules_1))
        for rule in relevant_rules_1:
            b, a = rule.split("|")
            if b in pages and a in pages:
                relevant_rules_2.append(rule)
        relevant_rules_2 = list(dict.fromkeys(relevant_rules_2))
        update_passes = True
        copy_rr2 = relevant_rules_2.copy()
        while copy_rr2:
            for rule in copy_rr2:
                b, a = rule.split("|")
                b_i = pages.index(b)
                a_i = pages.index(a)
                if b_i < a_i:
                    copy_rr2.remove(rule)
                else:
                    update_passes = False
                    pages.remove(b)
                    pages.insert(pages.index(a), b)
                    copy_rr2 = relevant_rules_2.copy()
                    break

        if not update_passes:
            out.append(int(pages[mid_idx]))
    print(sum(out))
