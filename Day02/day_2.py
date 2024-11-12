print("Welcome to the tip Calcuator!")
bill=float(input("What was the total bills ? $"))
tip=int(input("How Much tips Would like to give ? 10,12 or 15 "))
split_bill=int(input("How many people to split the bill ?"))
bill_withtip=tip/100*bill+bill
print(f"Each Person Should Pay :{round(bill_withtip/split_bill,2)}")


