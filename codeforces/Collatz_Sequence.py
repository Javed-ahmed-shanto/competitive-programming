number = int(input())
steps = 0

for i in range(200):
    if number == 1:
        break
    else:
      if number % 2 == 1:
            number = number * 3 + 1
      elif number % 2 == 0:
            number = number / 2
      steps += 1
    # fill in the rest of this program
    
if number == 1:
    print("It took", steps, "steps")
else:
    print("The number didn't reach 1 yet")