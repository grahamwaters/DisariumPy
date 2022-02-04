import math
import string
import icecream
from icecream import ic
import tqdm
from tqdm import tqdm


def get_sum(digits,sum=0):
    """Get the sum of the digits in digits raised to their respective cardinal positions

    Args:
        digits ([array]): [5,1,3]
        sum (int, optional): [initializer for the sum variable]. Defaults to 0.

    Returns:
        [sum: [the (int) sum of the digits in the manner shown above]
    """

    for d_tuple in enumerate(digits,start=1):
        sum += int(d_tuple[1])**int(d_tuple[0])

    return sum

def main():
    """
    this script finds disarium numbers which are defined as numbers whose values, when squared by their respective cardinal positions, add to the original number (i.e. 518 --> 5^1 + 1^2 + 8^3 = 518)
    """
    x = 1
    disarium_aquarium = [] # will hold our disarium numbers that we find
    runs = 3000
    last_found_d_number = 1 # init
    pbar = tqdm(total = runs+1)
    while int(x) < runs:
        x_string = str(x)
        digits = [] # init as empty array which will be populated with the digits from the number x like [5,1,8]
        for digit in range(0,len(x_string)):
            #cardinal positions are denoted by digit in this loop
            digits.append(int(x_string[digit]))
        # now digits contains [#,...,#] the numbers as shown here
        sum_of_digits = get_sum(digits) # leaving sum blank to allow it to default to zero as defined in the function
        #print(sum_of_digits)
        if sum_of_digits == x: # we may have already found some disariums
            print(f"found a disarium number! --> {x}")
            #print(f'{x},',end='')
            disarium_aquarium.append(x)
            last_found_d_number = int(x) # this is a dev to see if skipping forwards is useful.
            #ic(last_found_d_number)

        x = int(x)
        x += 1 # level up
        pbar.update(1)

main()