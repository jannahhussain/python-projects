balance = 25
percentage_val = 66
percentage_divider = 100
def intrest_rate_calculator_for_any_percentage(balance, denominator, percentage_val, add_more_money, divider):
    cal_interest = (percentage_val/denominator) * balance
    cal_interest = cal_interest + add_more_money
    cal_interest = cal_interest/divider
    return cal_interest


interest_outcome = intrest_rate_calculator_for_any_percentage(balance, percentage_divider, percentage_val, 20, 50)

print(interest_outcome)
