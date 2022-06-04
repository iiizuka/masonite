"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash

from app.models.User import User


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.truncate()

        User.create(
            {
                "name": "Joe",
                "email": "user1@example.com",
                "password": Hash.make("password"),
                "phone": "09011111111",
            }
        ).create(
            {
                "name": "Anna",
                "email": "user2@example.com",
                "password": Hash.make("password"),
                "phone": "09022222222",
            }
        )
