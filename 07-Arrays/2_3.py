# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
weeks = [0, 0, 0, 0]
total = 0
different = {
   "food": 0,
   "transport": 0,
   "utilities": 0
}
for i in range(len(monthly_expenses)):
   for j in range(len(monthly_expenses[i])):
      if i == 0:
         weeks[0] += monthly_expenses[i][j] 
      elif i == 1:
         weeks[1] += monthly_expenses[i][j]
      elif i == 2:
         weeks[2] += monthly_expenses[i][j]
      else:
         weeks[3] += monthly_expenses[i][j]

for item in weeks:
   total+=item

for i in range(len(monthly_expenses)):
   for j in range(len(monthly_expenses[i])):
      if j == 0:
         different['food'] += monthly_expenses[i][j]
      elif j == 1:
         different['transport'] += monthly_expenses[i][j]
      else:
         different['utilities'] += monthly_expenses[i][j]
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',different['food'])
print('Transport:',different['transport'])
print('Utilities:',different['utilities'])
print('Week 1:',weeks[0])
print('Week 2:',weeks[1])
print('Week 3:',weeks[2])
print('Week 4:',weeks[3])
print('---------------')
print('TOTAL:', total)