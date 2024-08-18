money_in = 1000.0
years = int(input())
money_out = 1000.0
interest = 0.05

for i in range(years):
    money_out += money_out * interest

print(round(money_out, 2))