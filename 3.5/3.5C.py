from sys import stdin

for stroke in stdin:
    if not stroke.startswith('#'):
        stop = stroke.find('#')
        if stop != -1:
            print(stroke[:stop])
        else: 
            print(stroke.rstrip('\n'))
