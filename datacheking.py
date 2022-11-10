from services import LoginData, RegistrData
from bd_work import DataBaseManager


class LoginChecker:
    """Validates data upon login"""

    def __init__(self, data: LoginData):
        self.data = data
        self.bd_manager = DataBaseManager()
        self.is_correct = True if self.check_data() else False

    def check_data(self) -> bool:
        if self.search_login() and self.check_password():
            return True
        return False

    def search_login(self) -> bool:
        """Looks for a login if it does not find it, then the user needs to register"""

        logins = self.bd_manager.get_all_logins()
        if self.data.login in logins:
            return True
        return False

    def check_password(self) -> bool:
        """Checks if the user's password is correct"""

        if self.data.password == self.bd_manager.get_password(self.data.login):
            return True
        return False


class RegistrChecker:
    """Checks the correctness of data during registration"""

    def __init__(self, data: RegistrData):
        self.bd_manager = DataBaseManager()
        self.data = data
        self.is_correct = True if self.check_data() else False

    def check_data(self) -> bool:
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

        logins = self.bd_manager.get_all_logins()
        if self.data.login not in logins:
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
            raise True
        return False

    def check_school_and_building_num(self) -> bool:
        """Checks if the school and building number is a number"""

        if self.data.school_num.isdigit() and self.data.building_num.isdigit():
            return True
        return False

    def check_phone_number(self) -> bool:
        """Checks if the phone number is correct"""

        self.data.phone_num.replace('-', '')
        self.data.phone_num.replace(')', '')
        self.data.phone_num.replace('(', '')
        if self._len() and self._only_digits():
            return True
        return False

    def _len(self) -> bool:
        """Checks the length of a phone number"""

        if len(self.data.phone_num) == 10:
            return True
        return False

    def _only_digits(self) -> bool:
        """Checks for extraneous characters"""

        for i in self.data.phone_num:
            if i.isalpha():
                return False
        return True
