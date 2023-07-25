import constants


class Checker:
    @staticmethod
    def reg_num_is_valid(reg_num: str) -> bool:
        return reg_num in constants.TYPES 