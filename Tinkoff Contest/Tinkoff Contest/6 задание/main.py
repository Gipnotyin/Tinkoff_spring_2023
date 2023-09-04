class Gang:
    def __init__(gang, count: int, parent: 'Gang' = None):
        gang.parent: 'Gang' = parent or gang
        gang.count = count

    def refresh(gang) -> None:
        stack = [gang]
        while not stack[-1].parent is stack[-1]:
            stack.append(stack[-1].parent)

        while stack:
            b = stack.pop()
            b.count += b.parent.count
            b.parent = b.parent.parent

    def __contains__(g1: 'Gang', g2: 'Gang') -> bool:
        g1.refresh()
        g2.refresh()
        return g1.parent is g2.parent

    def union(g1: 'Gang', g2: 'Gang') -> None:
        if g1 in g2: return
        newGang = Gang(1, Gang(0))
        g1.parent.parent = newGang
        g1.refresh()
        g2.parent.parent = newGang
        g2.refresh()


def solve():
    nHaunts, nQuestions = map(int, input().split()[:2])
    gangs = [Gang(1, Gang(0)) for _ in range(nHaunts + 1)]
    for _ in range(nQuestions):
        match input().split():
            case '1', x, y, *_:
                # объединить x и y
                Gang.union(gangs[int(x)], gangs[int(y)])
            case '2', x, y, *_:
                # находятся ли x и y в одной банде?
                yield 'YES' if gangs[int(x)] in gangs[int(y)] else 'NO'
            case '3', x, *_:
                # в скольких бандах был x?
                (gang := gangs[int(x)]).refresh()
                yield f"{gang.count}"


print('\n'.join(solve()))