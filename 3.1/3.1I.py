while (stroke := input()) != '':
    if not stroke.startswith('#'):
        stop = stroke.find('#')
        if stop != -1:
            print(stroke[:stop])
        else: print(stroke)
