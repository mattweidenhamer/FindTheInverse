# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from inverse_finder.inverter import find_inverse

affirmative_words = ("y", "yes", "yeah", "ye")
negatory_words = ("n", "no", "nah", "nope")


def main_function():
    remainder = "T"
    while not str.isdigit(remainder):
        remainder = input("Enter the remainder that you'd like to get an inverse for. ")
        if not str.isdigit(remainder):
            print("That's not a valid integer.")
    remainder = int(remainder)

    mod = "F"
    while not str.isdigit(mod):
        mod = input("Enter the value of the mod. ")
        if not str.isdigit(mod):
            print("That's not a valid integer.")
    mod = int(mod)

    if remainder > mod:
        answer = None
        new_remainder = remainder % mod
        while answer not in affirmative_words and answer not in negatory_words:
            answer = input(
                f"It looks like your remainder, {remainder}, is higher than your actual mod, {mod}."
                + f"\nWould you like to use the adjusted remainder of {new_remainder}? Y/N "
            ).lower()
        if answer in negatory_words:
            print("Well, I can't really help you then.")
            return
        if answer in affirmative_words:
            print(
                "Okay, setting remainder to be equal to the modularly-reduced remainder."
            )
            remainder = new_remainder
        else:
            print(
                "You somehow managed to escape the while loop without an affirmation.\n"
                + "Either that, or I didn't properly understand and flow with your answer.\n"
                + "Either way, this is a glitch, and you should report it."
            )
            return

    inverse = find_inverse((remainder), (mod))
    if inverse is None:
        print(f"There is no valid inverse for {remainder} mod {mod}")
        return
    print(
        f"The inverse of {remainder} mod {mod} is any number congruent to {inverse} mod {mod}."
    )
    if inverse < 0:
        print(
            f"Converted to a non-negative number, that is the same as {mod + inverse} mod {mod}"
        )


main_function()
input("Press enter to exit.")
