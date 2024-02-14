#Code to compute the sum of the digits of a given number

number = 167

computed = lambda x: sum(map(int,str(x)))

print(computed(number))