dict = {'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'Й': 'I',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'Kh',
        'Ц': 'Tc',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ъ': '',
        'Ы': 'Y',
        'Ь': '',
        'Э': 'E',
        'Ю': 'Iu',
        'Я': 'Ia'
        }


def trans(text):
    result = ''
    for letter in text:
        if letter.upper() in dict:
            if letter.isupper():
                result += dict[letter.upper()]
            else:
                result += dict[letter.upper()].lower()
        else:
            result += letter
    return result


with open('cyrillic.txt', 'r', encoding='UTF-8') as inp_file:
    text = inp_file.read()

with open('transliteration.txt', 'w', encoding='UTF-8') as trans_file:
    trans_file.write(trans(text))
