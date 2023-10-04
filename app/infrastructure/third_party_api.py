"""REST API using numbersapi in Python

    Returns:
        str: number fact of a number
"""

import requests

def get_number_fact(number) -> str:
    """Get a fact of a requested number

    Args:
        number (int): a number to get information

    Returns:
        str: a fact of the requested number
    """
    url = "http://numbersapi.com/" + str(number)
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        fact = response.text
        return fact
    return "There was an error."
