# This program is to split the bill among friends using Python

# get input value for total number of friends 
total_friends=float(input())

# get input value for bill 
bill=int(input())

# calculate the tax amount
tax=(20/100)*bill

# divide the total bill among friends
total_bill=bill+tax

# print the split amount
split_amount=total_bill/total_friends
print(split_amount)