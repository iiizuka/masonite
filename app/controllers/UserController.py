from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from app.models.User import User


class UserController(Controller):
    def index(self, view: View):
        return view.render("")

    def create(self, view: View):
        return view.render("")

    def store(self, view: View):
        return view.render("")

    def show(self, view: View, request: Request):
        return view.render("welcome", {
            "user": User.find(request.param("id"))
        })

    def edit(self, view: View):
        return view.render("")

    def update(self, view: View):
        return view.render("")

    def destroy(self, view: View):
        return view.render("")
