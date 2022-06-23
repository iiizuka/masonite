""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class Post(Model):
    """Post Model"""

    __fillable__ = [
        "user_id",
        "body",
        "is_show",
    ]

    @has_one('id')
    def user(self):
        from app.models.User import User

        return User
