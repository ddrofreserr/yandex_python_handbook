def can_eat(knight, figure):
    if abs(knight[0] - figure[0]) == 2 and abs(knight[1] - figure[1]) == 1:
        return True
    elif abs(knight[0] - figure[0]) == 1 and abs(knight[1] - figure[1]) == 2:
        return True
    return False
