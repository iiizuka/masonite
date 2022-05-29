from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.resource("book", "BookController"),
]
