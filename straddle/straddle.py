
# Identify the straddle value

# Identify the cmp

# Identify the straddle away +ve value and -ve value

#step1
# find the % difference from +ve to -ve when price is straddle value away 
# and find the closest difference in above or below which is away in either side.

    #iteration 1
    # when the price/premium moves x points/percentage up/down,
    # validate the price on opposite side if that requires steup/down to the closest

    #iteration 2
    # when the price/premium moves x points/percentage up/down [same as iteration1],
    # validate the price on oppoiste side if that requires steup/down to the closest
    # repeat this till the strikes are (x srikes away) on both sides.

    #iteration n
    # when the price/premium moves x points/percentage up/down [opposite as iteration(n-1)],
    # validate the price on same direction if that requires steup/down to the closest,
    # repeat this step till (x srikes away) on both sides.

    # when both strikes reaches (x strikes away) closest to the current market price
    # close the trade. Repeat the step1