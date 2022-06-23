"""User Model."""
from masoniteorm.models import Model
from masoniteorm.relationships import has_many
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates


class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __fillable__ = [
        "name",
        "email",
        "phone",
        "password"
    ]

    __hidden__ = ["password"]
    __auth__ = "email"

    @has_many('id', 'user_id')
    def posts(self):
        from app.models.Post import Post

        return Post
