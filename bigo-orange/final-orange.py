def messageSpreading():
    while True:
        try:
            T = int(input())
            for _ in range(T):
                N = int(input())
                print(2 * N - 2)
        except EOFError:
            break
    return


messageSpreading()
