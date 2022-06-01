from masonite.routes import Route

ROUTES = [
    Route.get("/@id", "WelcomeController@show"),
    Route.resource("user", "UserController"),
]
