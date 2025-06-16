t = int(input())

# Process each test case
for _ in range(t):
    try:
        a, b = input().split()
        result = int(a) // int(b)
        print(result)
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code:", e)
