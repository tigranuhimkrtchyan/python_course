num = int(input ("insert two digit number"))
last_digit = num %10
first_digit = num //10
res = last_digit == first_digit and num >0
print(res)