from services import LoginData, RegistrData


class LoginChecker:
    """Validates data upon login"""

    def __init__(self, data: LoginData):
        self.data = data
        self.is_correct = False

    def search_login(self):
        """Looks for a login if it does not find it, t
        hen the user needs to register"""

        pass
        # self.data.login


class RegistrChecker:
    """Checks the correctness of data during registration"""

    def __init__(self, data: RegistrData):
        self.data = data
        self.is_correct = True

    def check_FIO(self):
        """Checks the correctness of the FIO"""

        pass
