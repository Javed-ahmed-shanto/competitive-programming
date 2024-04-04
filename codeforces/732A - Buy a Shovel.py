k, r = map(int, input().split())
count = []

for i in range(1, 11):
    if k*i % 10 == 0 or k*i % 10 == r:
        count.append(i)

min_count = min(count)
print(min_count)

#another way
# k, r = map(int, input().split())

# min_count = float('inf') 

# for i in range(1, 11):  
#     if k * i % 10 == 0 or k * i % 10 == r:
#         min_count = min(min_count, i)

# print(min_count)
