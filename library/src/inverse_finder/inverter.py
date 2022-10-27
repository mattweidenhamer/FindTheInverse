from math import gcd

"""
Find the modular inverse of a number.

Functions:

    find_inverse(number: int, mod: int) -> int
    euclidian_algorithm(numberToEqual: int, numberToMultiply: int) -> dict
"""


def find_inverse(number: int, mod: int) -> int:
    """
    find_inverse looks for the

    Arguments:
        number -- An integer remainder of mod.
        mod -- An integer that number is mod to.

    Raises:
        ArithmeticError: If somehow none of the returned values are equal to the modulated number, then an arithmetic error is raised.

    Returns:
        Returns the inverse of the argument number, assuming mod of the argument mod.
    """

    if gcd(number, mod) != 1:
        testVar = gcd(number, mod)
        return None
    else:
        returned_dictionary = euclidian_algorithm(mod, number)
        if returned_dictionary["firstValue"] == number:
            return returned_dictionary["firstCoeffcient"]
        elif returned_dictionary["secondValue"] == number:
            return returned_dictionary["secondCoefficient"]
        else:
            raise ArithmeticError(
                "None of the returned values equal the modulated number!"
            )


def euclidian_algorithm(numberToEqual: int, numberToMultiply: int) -> dict:
    """
    euclidian_algorithm Runs the euclidian algorithm recursively on the passed numbers and returns a dictionary of what their function would be.

    Arguments:
        numberToEqual -- What number the function needs to equal.
        numberToMultiply -- What number the function needs to multiply to be greater than or equal to numberToEqual

    Returns:
        A dictionary containing variables that equal 1 when calculated in the form:
        (firstCoefficient * firstValue) + (secondCoefficient * secondValue)
    """

    def _checkEquals1(mathDict):
        return (
            True
            if (
                (mathDict["firstCoefficient"] * mathDict["firstValue"])
                + (mathDict["secondCoefficient"] * mathDict["secondValue"])
                == 1
            )
            else False
        )

    # Multiplies numberToMultiply until we can't get a whole number any more.
    coefficientOfX = 0
    # Repeat until coefficientOfX times numberToMultiply is greater than number1
    while numberToMultiply * coefficientOfX < numberToEqual:
        coefficientOfX = coefficientOfX + 1

    coefficientOfX = coefficientOfX - 1
    remainder = numberToEqual - (coefficientOfX * numberToMultiply)
    # The end result will mimic the function, should look like:
    # NumberToEqual = coefficientOfX * numberToMultiply + remainder

    if remainder == 1:  # Start climbing back up the ladder
        # Climbing up the ladder: have a dictionary of values that we multiply and change?
        # Structure: 1 = firstCoefficient * firstValue + secondCoefficient * secondValue
        # Make secondCoefficient a negative to start with
        return {
            "firstCoefficient": 1,
            "firstValue": numberToEqual,
            "secondCoefficient": coefficientOfX * -1,
            "secondValue": numberToMultiply,
        }
    elif remainder < 1:
        raise ArithmeticError(
            "Reached a negative remainder while applying the Euclidian Algorithm."
        )
    else:
        # Call the function again, with numberToMultiply as numberToEqual and remainder as numberToMultiply
        nextIteration = euclidian_algorithm(numberToMultiply, remainder)
        # The values that it returns should then be checked against each other.
        # Each firstValue that the next function returns should be equal to the numberToMultiply, so you should just be able to add coefficientValue and coefficientOfX.
        if (
            _checkEquals1(nextIteration)
            and nextIteration["firstValue"] == numberToMultiply
        ):
            # Each level returns equal to: firstCoefficient * firstValue + secondCoefficient * secondValue
            # Each dictionary needs to reach the next level as: secondCoefficient * numberToEqual + (secondCoefficient * coefficientOfX + firstCoefficient) * firstValue
            returnDictionary = {
                "firstCoefficient": nextIteration["secondCoefficient"],
                "firstValue": numberToEqual,
                "secondCoefficient": (
                    nextIteration["secondCoefficient"] * coefficientOfX * -1
                )
                + nextIteration["firstCoefficient"],
                "secondValue": nextIteration["firstValue"],
            }
            # Each level will equal: firstCoefficient * firstValue - secondCoefficient * secondValue
            # secondCoefficient should be equal to to the current level's remainder minus (multiplyingNumber times numberToMultiply)
            return returnDictionary

        else:
            raise ArithmeticError(
                "Values of dictionary returned did not equal 1, or the firstValue didn't equal the numberToMultiply,"
                + f"\nprinting dictionary: {nextIteration}\nprinting numberToMultiply: {numberToMultiply}"
            )
