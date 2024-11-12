from Day_9.art import logo
print(logo)
bid_not_finish=True
auction={}
def highest_bider(biding):
    highest_bid=0
    winner=''
    for i in biding:
        if biding[i]>highest_bid:
            highest_bid=biding[i]
            winner=i
    print(f"The winner is {i} with a bid of ${highest_bid}")

while bid_not_finish:
    print()
    name=input('What is your name? :')
    bid=int(input("What is your bid ? :$"))
    auction[name]=bid
    continues=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if continues =="no":
        bid_not_finish=False
        highest_bider(auction)
    if continues=='yes':
        print('\n'*20)



