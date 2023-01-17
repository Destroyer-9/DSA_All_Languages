# Cost Per Hub
# Expenditures:
infra_machine = 3*100000 # 3 machines cost
infra_shop = 12*20000 # Per hub INR
man_power = 12*15000 # per man
iot_integration_cost = 50000 # one time
infra_electricity_cost = 12*1*3*30*8 # Total power cost per month
infra_furniture = 20000 # one time
misc = 0

total_expenses = infra_shop + infra_machine+ man_power +iot_integration_cost + infra_electricity_cost + infra_furniture + misc 

print("Total Investment: Rs.{}".format(total_expenses))

# Revenue
# Direct Revenue
cost_per_hour = 200 # Avg cost per hour
total_working_hours = 12*30*3*12
total_direct_revenue = cost_per_hour*total_working_hours

print("Total Direct Revenue: Rs.{}".format(total_direct_revenue))
profit = total_direct_revenue-total_expenses
print("Total Profit Per Hub: Rs.{} and in form of percentage: {}%".format(profit,profit/total_expenses*100))




