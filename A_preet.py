def madness(n):
    print(f"Level {n}")
    if n > 0:
        madness(n - 1)
        madness(n - 1)

madness(5)
