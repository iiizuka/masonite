from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.User import User


class UserController(Controller):
    def index(self, view: View):
        return view.render("")

    def create(self, view: View):
        return view.render("")

    def store(self, view: View):
        return view.render("")

    def show(self, view: View, request: Request):
        User.find(request.param('user_id'))

        return view.render("")

    def edit(self, view: View):
        return view.render("")

    def update(self, view: View):
        return view.render("")

    def destroy(self, view: View):
        return view.render("")
