def counterGame(n):
    turn = 0
    while n > 1:
        if (n & (n - 1)) == 0:
            n //= 2
        else:
            power = 1
            while power <= n:
                power <<= 1
            n -= power >> 1
        turn ^= 1
    return "Richard" if turn == 0 else "Louise"
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(counterGame(n))
