with open(input(), 'r', encoding='UTF-8') as file_in:
    text = []
    for line in file_in.readlines():
        while '\t' in line:
            line = line.replace('\t', '')
        text += line.split(' ')
        ans = [word for word in text if word != '' and word != '\n']
with open(input(), 'a', encoding='UTF-8') as file_out:
    for word in ans:
        if word.endswith('\n'):
            file_out.write(word)
        else:
            file_out.write(word + ' ')
