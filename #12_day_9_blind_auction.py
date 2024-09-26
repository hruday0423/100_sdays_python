
bid_dit={}
def highest_bidder(dict):
    winner =""
    max_bid = 0
    for bids in dict:
        bid_amount = dict[bids]
        if max_bid< bid_amount:
            max_bid = bid_amount
            winner = bids
    print(f"the winner is {winner}, with bid of {max_bid}")

bid_open = True
while bid_open:
    name = input('enter name :')
    price = float(input('enter your bid $:'))
    bid_dit[name]=price
    cont_bid= input('are there more bids? enter "y" or "n" : ')
    if cont_bid =="n":
        bid_open= False
        highest_bidder(bid_dit)
    else:
        print("\n"*20)





