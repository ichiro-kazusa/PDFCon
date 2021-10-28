

from ..command.encrypt import EncryptionCommand


class Encryption:
    def __init__(self, owner: str = '', user: str = '') -> None:
        self.__owner = owner
        self.__user = user
        self.__verify_entries()

    @property
    def owner(self):
        return self.__owner

    @property
    def user(self):
        return self.__user

    def __verify_entries(self):
        # ## verify encryption rules

        # when user password is given, empty owner password is not allowed .
        # -> use user password as owner password
        if self.__owner == '' and self.__user != '':
            self.__owner = self.__user

    @staticmethod
    def create_encryption_from_CMD(cmd: EncryptionCommand) -> 'Encryption':
        raise NotImplementedError()
