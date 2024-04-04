k, n, w = map(int, input().split())   
results = []

for i in range(1, w+1):
    results.append(i * k)

total_sum = sum(results)
if n >= total_sum:
    print(0)
else:
    print(total_sum-n)