import random

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from faker import Faker

fake = Faker('ru_RU')


@dataclass
class User:
    country: str
    city: str
    address_pizza: str
    name: str
    birth_day: str
    birth_month: str
    birth_year: str
    number: str
    vk_link: str

    def __hash__(self):
        return hash((
            self.country,
            self.city,
            self.address_pizza,
            self.name,
            self.birth_day,
            self.birth_month,
            self.birth_year,
            self.number,
            self.vk_link
        ))


class UserGenerator:
    @classmethod
    def generate_user(cls) -> User:
        return User(
            country='Россия',
            city='Краснодар',
            address_pizza='улица Красных Партизан, 171',
            name=fake.name(),
            birth_day=str(random.randint(a=1, b=28)),
            birth_month=str(fake.month()),
            birth_year=str(random.randint(a=1970, b=datetime.now().year)),
            number='9298505043',
            vk_link=fake.url()
        )

    @classmethod
    def generate_users(cls, count: int = 10) -> list[User]:
        return [cls.generate_user() for _ in range(count)]

    @classmethod
    def get_random_user(cls) -> User:
        return cls.generate_user()


user = UserGenerator.get_random_user()
