from selenium import webdriver
from selenium.webdriver.common.by import By
import random


def generate_random_name(minimum=2, maximum=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    name = "".join(random.choice(characters) for _ in range(minimum, maximum))
    return name


def generate_random_email(minimum=3, maximum=15):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    email = "".join(random.choice(characters) for _ in range(minimum, maximum)) + f'@mail.ru'
    return email


def generate_random_password(minimum=6, maximum=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!№;%:?"
    password = "".join(random.choice(characters) for _ in range(minimum, maximum))
    return password

