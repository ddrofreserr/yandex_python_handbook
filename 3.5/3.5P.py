from sys import stdin

phrase_search = input().lower()


def search(phrase, file):
    for word in phrase.split(' '):
        if word not in file:
            return False
        else:
            file = file[file.index(word):]
    return True


def spaces(text):
    i = 0
    while len(text) > i:
        if text[i - 1] == ' ' and text[i] == ' ':
            text = text[:i] + text[i + 1:]
        else:
            i += 1
    return text


ans = []
for line in stdin.readlines():
    file_name = line.rstrip('\n')
    with open(file_name, encoding='UTF-8') as file:
        text = file.read()
        while '&nbsp;' in text:
            text = text.replace('&nbsp;', ' ')
        while '\\n' in text:
            text = text.replace('\\n', ' ')
        text = spaces(text.lower())
        if search(phrase_search, text):
            ans.append(file_name)
if len(ans) != 0:
    print(*ans)
else:
    print('404. Not Found')
