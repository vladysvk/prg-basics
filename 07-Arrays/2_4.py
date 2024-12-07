# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
    string = ""
    for i in range(len(meal_plan[day_number])):
        if i == 0:
            string += meal_plan[day_number][i]
        else:
            string += f", {meal_plan[day_number][i]}"
    return string


# Prints weekly meal plan
print("WEEKLY MEAL PLAN\n(Breakfast, Lunch, Dinner\n==========================)")
for i in range(len(meal_plan)):
    print(f"{weekday(i + 1)}: {day_meal_plan(meal_plan, i)}")