charge_amount = random.randint(1, 10000)
amount_paid = random.randint(10000, 20000)
amount_2_count = amount_paid - charge_amount

print(f'the amount charged is {charge_amount}.')
print(f'The amount you paid is {amount_paid}.')
print(amount_2_count)


c=int(input('Please enter the number provided which represents cents:'))
print(c//10000, "hundreds")
c = c%10000
print(c//5000, "fifties")
c = c%5000
print(c//2000, "twenties")
c = c%2000
print(c//1000, "tens")
c = c%1000
