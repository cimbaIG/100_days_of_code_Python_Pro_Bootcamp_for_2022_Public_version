import os
import art

# Lambda function to clear console screen
clear = lambda: os.system("clear")

# Function to get a max bid from dictionary
def max_bid(bidders):
    keyList = []
    bidList = []
    for key in bidders:
        keyList.append(key)
        bidList.append(bidders[key])
    maxBid = max(bidList)
    maxBidder = keyList[bidList.index(maxBid)]
    return maxBidder, maxBid #Function return a tuple of values maxBidder and maxBid

print(art.logo)
print("Welcome to the secret auction program.")

bidders = {}

stopAuction = False
while stopAuction == False: 
    bidder_name = input("What is your name? ")
    bid = int(input("What's your bid?: $"))
    bidders[bidder_name] = bid
    moreBidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear()
    if moreBidders == "no":
        clear()
        print(f"The winner is {max_bid(bidders)[0]} with a bid of ${max_bid(bidders)[1]}.")
        stopAuction = True

# Their solution
""" from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear() """