import calendar
import datetime
import jwt

from const import SECRET, ALGO
from service.user import UserService
from flask import abort


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, usernsme, password):
        user = self.user_service.get_by_name(usernsme)
        if not user:
            abort(400)
        if not self.user_service.compsre_password(user.password, password):
            abort(400)
        data = {
            'username' : user.username,
            'role' : user.role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        return {'access_token': access_token, 'refresh_token': refresh_token}