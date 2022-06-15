from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from masonite.essentials.helpers import hashid
from app.models.User import User
from app.validation.UserValidation import UserValidation


class UserController(Controller):
    def index(self, view: View):
        """ユーザ一覧."""
        return view.render("user.index", {
            "users" : User.all()
        })

    def create(self, view: View):
        """ユーザ登録画面."""
        return view.render("user.create")

    def store(self, view: View, request: Request, response: Response):
        """ユーザ登録."""
        errors = request.validate(UserValidation)

        if errors:
            print(response.back())
            return response.back().with_errors(errors)

        User.create(
            name=request.input('name'),
            email=request.input('email'),
            password=hashid(request.input('password')),
        )

        return view.render("user.index", {
            "users" : User.all()
        })

    def show(self, view: View, request: Request):
        """ユーザ詳細."""
        return view.render("user.show", {
            "user": User.find(request.param("id"))
            # "user": request.user()
        })

    def edit(self, view: View, request: Request):
        """ユーザ編集画面."""
        return view.render("user.create", {
            "user": User.find_or_404(request.param("id"))
        })

    def update(self, view: View, request: Request):
        """ユーザ編集."""
        user = User.find_or_404(request.param("id"))

        user.fill(request).save()

        return view.render("user.index", {
            "users" : User.all()
        })

    def destroy(self, view: View, request: Request):
        """ユーザ削除."""
        user = User.find_or_404(request.param("id"))

        user.delete()

        return view.render("user.index", {
            "users" : User.all()
        })
