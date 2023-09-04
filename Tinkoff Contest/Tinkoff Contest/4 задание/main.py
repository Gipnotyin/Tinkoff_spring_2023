from functools import cache


def solve(a: list[int], n: int) -> str:
    @cache
    def solve(s, i=0):
        # если набрали сумму
        if s == 0: return 0

        # если перебрали
        if s < 0: return -1

        # если закончились монетки
        if i >= len(a): return -1

        # пробуем включить монету
        x = solve(s - a[i], i + 1)
        if x >= 0: return x | (1 << i)

        # пробуем не включать монету
        x = solve(s, i + 1)
        if x >= 0: return x

        return -1

    a *= 2  # удваиваем монеты
    x = solve(n)
    if x == -1: return "-1"
    ans = [t for i, t in enumerate(a) if x & (1 << i)]  # в каком порядке выводить?
    return f'{len(ans)}\n{" ".join(map(str, ans))}'



target, n = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(arr, target))