from faker import Faker
from app import db, User

fake = Faker()

def seed_users(count=10):
    for _ in range(count):
        username = fake.user_name()
        password = fake.password()
        email = fake.email()

        user = User(username, password, email)
        db.session.add(user)
    
    db.session.commit()

if __name__ == '__main__':
    seed_users()
    print('Seed data inserted successfully.')
