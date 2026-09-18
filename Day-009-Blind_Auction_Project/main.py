from art import logo
print(logo)



print("Welcome to Very Very I Mean Very Secret Auction (Only you knows about it! 😉) ")
auction = {}
max_key = ""
max_value = 0
go_on = True
while  go_on:
    # TODO-1: Ask the user for input
    # TODO-2: Save data into dictionary {name: price}

    name = input("Enter your name : ")
    amount = int(input("Enter your bid amount $"))

    auction[name] = amount

    # TODO-3: Whether if new bids need to be added

    new_bidder = input("Is there any other bidder? 'yes' or 'no' ").lower()

    print("\n" * 100)

    if new_bidder == "no":
        go_on = False
        # TODO-4: Compare bids in dictionary
        for key,value in auction.items():
            if value > max_value:
                max_key = key
                max_value = value

        print(f"The winner is {max_key} with a bid of ${max_value}")



