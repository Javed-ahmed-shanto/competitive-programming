n, k = map(int, input().split())

solvable_problem = 0
total_time = 0

for i in range(1, n+1):
    time_to_solve = 5 * i

    total_time += time_to_solve
    
    if total_time + k <= 240:
        solvable_problem += 1

print(solvable_problem)