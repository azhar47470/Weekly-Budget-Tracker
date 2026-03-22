days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 

weekly_expense = []

for day in days:
    daily_expense = int(input(f"Spending on {day} : "))
    weekly_expense.append(daily_expense)

days_under_50 = []

for i in range(len(weekly_expense)):
    if weekly_expense[i] <= 50:
        days_under_50.append(days[i])

total_expense = sum(weekly_expense)
average_expense = round(total_expense/len(weekly_expense),2)
highest_spending = max(weekly_expense)

highest_spending_days = []
for d in range(len(weekly_expense)):
    if weekly_expense[d] == highest_spending:
        highest_spending_days.append(days[d])

print(f"Total spending of this week is {total_expense}$")
print(f"Average spending of this week is {average_expense}$")
print(f"Highest spending of this week was on {'-'.join(highest_spending_days)}")
if days_under_50 :
 print(f"Stayed Under 50$ on {'-'.join(days_under_50)}")