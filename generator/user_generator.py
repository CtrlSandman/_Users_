from random import Random
from time import sleep
from typing import List

from entities.user import User


class UserGenerator(object):

    @staticmethod
    def generate(amount_of_batches: int = 10, batch_size_min: int = 50, batch_size_max: int = 100) -> list:
        for i in range(0, amount_of_batches):
            users: List[User] = list()
            batch_size = Random().randint(batch_size_min, batch_size_max)
            print(f"Batch {i} size is {batch_size}")
            for k in range(0, batch_size):
                users.append(User.generate_rand_user())
            yield users
            sleep(5)
