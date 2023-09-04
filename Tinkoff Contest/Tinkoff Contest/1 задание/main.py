n, max_dollars = map(int, input().split())
answer = 0
for price in map(int, input().split()):
    if price <= max_dollars:
        answer = max(price, answer)

print(answer)
