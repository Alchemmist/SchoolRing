from services import LoginData, RegistrData
from base_of_data import DataBaseManager


class LoginChecker:
    """Validates data upon login"""

    def __init__(self, data: LoginData):
        self.data = data
        self.bd_manager = DataBaseManager()
        self.is_correct = self._check_data()

    def _check_data(self) -> bool:
        if self._search_login() and self._check_password():
            return True
        return False

    def _search_login(self) -> bool:
        """Looks for a login if it does not find it, then the user needs to register"""

        login_after_serch = self.bd_manager.serch_logins(self.data.login)
        if len(login_after_serch) > 0:
            return True
        return False

    def _check_password(self) -> bool:
        """Checks if the user's password is correct"""

        password_after_serch = self.bd_manager.get_password(self.data.login)
        if self.data.password == password_after_serch[0][0]:
            return True
        return False


class RegistrChecker:
    """Checks the correctness of data during registration"""

    def __init__(self, data: RegistrData):
        self.bd_manager = DataBaseManager()
        self.data = data
        self.is_correct = self._check_data()

    def _check_data(self) -> bool:
        """Checks all param data during registration"""
        if (
                self.check_login() and
                self.check_password() and
                self.check_FIO() and
                self.check_school_and_building_num() and
                self.check_phone_number() and
                self.check_login()
        ):
            return True
        return False

    def check_FIO(self) -> bool:
        """Checks the correctness of the FIO"""

        if len(self.data.FIO.strip().split()) == 3:
            return True
        return False

    def check_login(self) -> bool:
        """Checks the uniqueness of the login"""

        logins = self.bd_manager.serch_logins(self.data.login)
        if not logins:
            return True
        return False

    def check_password(self) -> bool:
        if self._repeat_password() and self._savity_password():
            return True
        return False

    def _repeat_password(self) -> bool:
        """Checks if the user entered the same password"""

        if self.data.concoct_password == self.data.repeat_password:
            return True
        return False

    def _savity_password(self) -> bool:
        """Checks password strength"""

        check_lower = 0
        check_upper = 0
        check_num = 0
        for i in range(len(self.data.concoct_password)):
            # up/low
            if self.data.concoct_password[i].islower():
                check_lower += 1
            elif self.data.concoct_password[i].isupper():
                check_upper += 1
            # num
            if self.data.concoct_password[i].isnumeric():
                check_num += 1

        if (
                check_lower and check_upper and
                check_num and
                len(self.data.concoct_password) > 8
        ):
            return True
        return False

    def check_school_and_building_num(self) -> bool:
        """Checks if the school and building number is a number"""

        if self.data.school_num.isdigit() and self.data.building_num.isdigit():
            return True
        return False

    def check_phone_number(self) -> bool:
        """Checks if the phone number is correct"""

        a = self.data.phone_num.replace('-', '')
        a = a.replace(')', '')
        a = a.replace('(', '')
        a = a.replace('+', '')

        if self._len(a) and self._only_digits(a):
            return True
        return False

    def _len(self, a) -> bool:
        """Checks the length of a phone number"""

        if len(a) == 11:
            return True
        return False

    def _only_digits(self, a) -> bool:
        """Checks for extraneous characters"""

        for i in a:
            if i.isalpha():
                return False
        return True
