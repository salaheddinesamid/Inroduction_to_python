def interest_rate(amount,p,n):
    total_amount = amount * ((1 + (p/100)) ** n)
    interest = total_amount - amount

    print("Total interest:", interest)

interest_rate(1000,5,3)
