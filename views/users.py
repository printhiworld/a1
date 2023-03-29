from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service
from dao.model.user import User

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}

#,