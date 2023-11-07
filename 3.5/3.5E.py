from sys import stdin


def pal(word):
    ans = True
    word = word.lower()
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            ans = False
    return ans


pals = set()
for line in stdin.readlines():
    for word in line.rstrip('\n').split(' '):
        if pal(word) and word != '':
            pals.add(word)

for each in sorted(pals):
    print(each)
