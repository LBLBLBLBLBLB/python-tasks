auction_info = {}

bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


while not bidding_finished:
    name = input("Enter your name: ")

    while True:
        bid_input = input("Enter your price: ")
        try:
            bid_price = int(bid_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    auction_info[name] = bid_price
    should_continue = input("Are there other bidders? 'yes' or 'no'. ")
    if should_continue.lower() == "no":
        bidding_finished = True
        find_highest_bidder(auction_info)
