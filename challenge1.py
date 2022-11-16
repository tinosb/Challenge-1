loan_cost = [500, 600, 200, 1000, 450]
total_number_of_loan = len(loan_cost)
total_of_all_loans = sum(loan_cost)
average_loan_price = total_of_all_loans/total_number_of_loan
print("You have total of", total_number_of_loan, "loans" )
print("all your loans sum up to $", total_of_all_loans)
print("And your avergae loan price is $", average_loan_price )
{
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval":"bullet",
    "future_value": 1000,
}
future_value = 1000
remaining_months = 9
print(future_value)
print(remaining_months)
present_value = future_value/(1+0.2/12)**9
print("The fair value of your loan is $", present_value)
loan_price = 500
if present_value >= loan_price:
        print("The loan is worth at least the cost to buy it")
else:
        print("The cost of the loan is to expensive and not worth buying")
annual_discount_rate = 0.20
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval":"bullet",
    "future_value": 1000,
}
def present_value(future_value,remaining_months,annual_discount_rate):
    present_value = future_value/(1+annual_discount_rate/12)**12
    return present_value
    print(f"The present value of the loan is: {present_value}")