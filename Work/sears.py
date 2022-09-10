# bill_thickness = 10**-4
# sears_tower_height = 10**4
# bill_stack_height = 0
# num_bills = 1
# day_num = 1
# while num_bills*bill_thickness <= sears_tower_height:
#     bill_stack_height += bill_thickness*num_bills
#     print(day_num, num_bills, bill_stack_height, )
#     num_bills *= 2
#     day_num += 1

# sears.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)