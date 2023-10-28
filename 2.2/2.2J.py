password_unmod = input()
mladr = int(password_unmod[0]) + int(password_unmod[1])
starr = int(password_unmod[1]) + int(password_unmod[2])
print(max(mladr, starr), min(mladr, starr), sep='')