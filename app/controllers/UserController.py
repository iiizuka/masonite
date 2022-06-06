from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from app.models.User import User


class UserController(Controller):
    def index(self, view: View):
        """ユーザ一覧."""
        return view.render("user.index", {
            "users" : User.all()
        })

    def create(self, view: View):
        """ユーザ登録画面."""
        return view.render("user.create")

    def store(self, view: View, request: Request):
        """ユーザ登録."""
        User.create(
            name=request.input('name'),
            email=request.input('email'),
        )

        return view.render("user.index", {
            "users" : User.all()
        })

    def show(self, view: View, request: Request):
        """ユーザ詳細."""
        return view.render("user.show", {
            "user": User.find(request.param("id"))
        })

    def edit(self, view: View, request: Request):
        """ユーザ編集画面."""
        return view.render("user.edit", {
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
