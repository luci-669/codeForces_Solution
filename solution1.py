t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if c - b  == 1 and a + 2 == c:
        print("YES")
    else:
        print("NO")
