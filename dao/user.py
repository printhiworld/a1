from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_by_name(self, username):
        return self.session.query(User).filter(User.username == username).one()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d["id"])
        user.username = user_d["username"]
        user.password = user_d["password"]
        user.role = user_d["role"]


        self.session.add(user)
        self.session.commit()
