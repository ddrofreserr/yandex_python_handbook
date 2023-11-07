from sys import stdin
import json

output_list = stdin.readlines()
ans = 0

with open('scoring.json', encoding='UTF-8') as answers_file:
    answers = json.load(answers_file)
    for problem in answers:
        points_per_ans = problem['points'] // len(problem['tests'])
        for test in problem['tests']:
            if output_list.pop(0).rstrip('\n') == test['pattern']:
                ans += points_per_ans

print(ans)
