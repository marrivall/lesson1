
class GroupLimitException(Exception):
    def __init__(self, error_mess):
        self.error_mess = error_mess
        super().__init__(self.error_mess)

