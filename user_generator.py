from faker import Faker
from random import randint

class User:

    def __init__(self):
        self.fname = ''
        self.lname = ''
        self.email = ''

    def fake_user(self, catchall):
        fake = Faker()
        name = fake.name()
        self.fname = name.split(' ')[0].lower()
        self.lname = name.split(' ')[1].lower()
        email_name = name.replace(' ', '').lower()
        self.email = email_name+str(randint(1980, 2020))+'@'+catchall

    def email_user(self, text):
        user = text.split(':')
        self.fname = user[1]
        self.lname = user[2]
        self.email = user[0]

