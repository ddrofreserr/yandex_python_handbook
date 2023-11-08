def shift(phrase, step):
    ans = ''
    for sym in phrase:
        if 64 < ord(sym) < 91:
            new_ord = ord(sym) + step
            if 90 < new_ord < 97:
                ans += chr(new_ord - 26)
            elif new_ord < 65:
                ans += chr(new_ord + 26)
            else:
                ans += chr(new_ord)
        elif 96 < ord(sym) < 123:
            new_ord = ord(sym) + step
            if 96 < new_ord < 123:
                ans += chr(new_ord)
            elif new_ord < 97:
                ans += chr(new_ord + 26)
            else:
                ans += chr(new_ord - 26)
        else:
            ans += sym
    return ans


with open('public.txt', encoding='UTF-8') as file_in:
    phrase = file_in.read()

with open('private.txt', 'w', encoding='UTF-8') as file_out:
    file_out.write(shift(phrase, int(input())))
