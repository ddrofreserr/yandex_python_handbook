with open('secret.txt', encoding='UTF-8') as stena:
    code = stena.read()
    ans = [chr(ord(sym) % 256) for sym in code.rstrip('\n')]
    print(*ans, sep='')
