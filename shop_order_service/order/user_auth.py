from django.conf import settings


class UserAuth:

    def __init__(self, request) -> None:
        """
        Initialize the user_session
        """
        self.session = request.session
        user = self.session.get(settings.USER_SESSION_ID)
        if not user:
            # save an empty user in the session
            user = self.session[settings.USER_SESSION_ID] = []
        self.user = user
    
    def addUser(self, data=[]):

        if data not in self.user:
            self.user = data

    def getUser(self):
        return self.user
