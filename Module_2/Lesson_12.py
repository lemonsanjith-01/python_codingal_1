def total_calc(bill_amount,tip_perc):
    total = bill_amount * (1 + 0.01 * tip_perc)
    print(total)
    total = round(total, 2)
    print(f'Pleas pay £{total}')
total_calc(150,20)

#Activity_2
def cube(number):
    return number*number*number 

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print(by_three(9))
print(by_three(4))