#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import *

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6
    cheater3 = Cheat_Mulligan()
    cheater4 = Cheat_Additional_Die()
    cheater5 = Cheat_Weighted_Dice()
    cheater6 = Cheat_Sabotage()

    # both players take turns
    cheater1.roll()
    cheater2.roll()
    cheater3.roll()
    cheater4.roll()
    cheater5.roll()
    cheater6.roll()

    # both players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()
    cheater3.cheat()
    cheater4.cheat()
    cheater5.cheat()
    cheater6.cheat(cheater1)

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")
    print(f"Cheater 3 rolled {cheater3.get_dice()}")
    print(f"Cheater 4 rolled {cheater4.get_dice()}")
    print(f"Cheater 5 rolled {cheater5.get_dice()}")
    print(f"Cheater 6 rolled {cheater6.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    main()

