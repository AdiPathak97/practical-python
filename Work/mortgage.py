# mortgage.py
#
# Exercise 1.7

extra_payment_start_month = int(input('Enter start month of extra payment: '))
extra_payment_end_month = int(input('Enter end month of extra payment: '))
extra_payment = float(input('Enter extra payment amount: '))

principal = 500000
interest_rate = 0.05
monthly_payment = 2684.11
period_in_years = 30
total_paid = 0
total_months = 0

while principal > 0:
    total_months += 1
    if extra_payment_start_month <= total_months <= extra_payment_end_month:
        principal += (principal * interest_rate)/12 - (monthly_payment + extra_payment)
        total_paid += monthly_payment + extra_payment
    else:
        principal += (principal*interest_rate)/12 - monthly_payment
        total_paid += monthly_payment

print('Total paid:', total_paid, 'total months', total_months)