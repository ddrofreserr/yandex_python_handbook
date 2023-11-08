import os

file_size = os.path.getsize(input())
if file_size >= 1024:
    file_size_kb = file_size // 1024 + (file_size % 1024 != 0) * 1
    if file_size_kb >= 1024:
        file_size_mb = file_size_kb // 1024 + (file_size_kb % 1024 != 0) * 1
        if file_size_mb >= 1024:
            file_size_gb = file_size_mb // 1024 + (file_size_mb % 1024 != 0) * 1
            print(f'{file_size_gb}ГБ')
        else:
            print(f'{file_size_mb}МБ')
    else:
        print(f'{file_size_kb}КБ')
else:
    print(f'{file_size}Б')
