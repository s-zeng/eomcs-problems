# This is the core business logic
# `coin_value_list` is the list of available coins, in order
# `change` is the value to make with the coins
def make_change(coin_value_list, change):
    # First make a list to store the minimum number of coins needed to make a particular value
    # For example, at the end of the method, the list should be arranged such that
    # min_coins[n] will be the min coins needed to make value n 
    min_coins = [0] * (change + coin_value_list[0])

    # make sure that the list knows what coins we have (aka which values only need 1 coin)
    for coin in coin_value_list: min_coins[coin] = 1

    # Now, we iterate through every value between 1 to the value we want to make
    # The goal is to find the minimum number of coins required to make each value less than
    # the one we want, in hopes that we can use these subvalue solutions to make our main value
    for cents in range(1, change + 1):
        # variable to store current working solution for best way to make the value from coins
        # we start it high so that we know if theres no solution.
        coin_count = 2**31 - 1

        # variable to store current coin to try making the value with
        new_coin = coin_value_list[0]

        # Now we iterate through every available coin less than the value we're trying to find...
        for j in [c for c in coin_value_list if c <= cents]:
            # ... and if the solution to our value minus that coin is less than what our
            # best current solution (in coin_count), we replace it
            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j

        # after that loop, we should have the minimum coins for that value and we can store it
        min_coins[cents] = coin_count

    # once we're done the big loop, we should have the value we want now
    return min_coins[change]

# Some one liners to take input from the question
amnt = int(float(input().split()[1])*100)
clist = [int(float(x)*100) for x in input().split()]

# Do the thing
out = make_change(clist, amnt)

# Print out 0 if the solution isn't possible
if out*clist[0] > amnt:
    print(0)
else:
    print(out)

