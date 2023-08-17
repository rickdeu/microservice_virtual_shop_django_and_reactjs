from .user_auth import UserAuth

def userAuth(request):
    return {'user_auth': UserAuth(request)}