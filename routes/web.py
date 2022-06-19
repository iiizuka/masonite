from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.resource("user", "UserController"),
]

ROUTES += Auth.routes()
