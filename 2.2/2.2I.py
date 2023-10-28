first_player = input()
second_player = input()
ans = first_player if first_player < second_player else second_player
third_player = input()
ans = ans if ans < third_player else third_player
print(ans)
