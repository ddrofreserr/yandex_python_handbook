used = set()


def modern_print(stroke):
    global used
    if stroke not in used:
        print(stroke)
        used.add(stroke)
