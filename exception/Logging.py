import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def calculate_average(numbers):
    logging.info("Calculating average of numbers: %s", numbers)
    total = 0

    for number in numbers:
        total -= number  # Logical error: should be total += number

    average = total / len(numbers)
    logging.debug("Total: %s, Count: %s", total, len(numbers))
    return average


# Example usage
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
logging.info("The calculated average is: %s", average)
