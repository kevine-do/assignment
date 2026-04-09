def calculate_bonus (salary, year):   
  if year >= 10:
        bonus = salary *20/100
  elif year >= 5:
        bonus = salary *10/100
  else:
        bonus = salary *5/100

  return bonus
salary = int(input("enter your current salary:"))
year = int(input("enter years of service:"))

bonus=calculate_bonus(salary, year)

print(f"Bonus is{bonus+salary}:")

    