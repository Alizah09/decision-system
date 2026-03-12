import random


def fetch_credit_score():

    # simulate failure
    if random.random() < 0.3:
        raise Exception("Credit API unavailable")

    return random.randint(500, 800)