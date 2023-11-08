def is_palindrome(num):
    if isinstance(num, int):
        num = [i for i in str(abs(num))]
    elif isinstance(num, str):
        num = [i for i in str(num)]
    for i in range(len(num) // 2):
        if num[i] != num[-i - 1]:
            return False
    return True
