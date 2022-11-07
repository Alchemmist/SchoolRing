from services import LoginData, RegistrData


class LoginChecker:

    def __init__(self, data: LoginData):
        self.status = False


class RegistrChecker:

    def __init__(self, data: RegistrData):
        self.status = True
