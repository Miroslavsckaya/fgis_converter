import models.arshin as arshin
from datetime import datetime
import exceptions
from xsdata.models.datatype import XmlDate

COL_TYPE_NUM = 0
COL_MANUFACTURE_NUM = 1
COL_MODIFICATION = 2
COL_VRF_DATE = 3
COL_VALID_DATE = 4
COL_METROLOGIST = 5
COL_TEST_DEV_NUM = 6
COL_TEMPERATURE = 7
COL_HUMIDITY = 8
COL_PRESSURE = 9


class RecInfoFactory:
    @staticmethod
    def create_verification_from_csv_row(meter: list):
        verification = RecInfoFactory.__create_default()
        verification.mi_info = MiInfoFactory.create_from_csv_row(meter)
        verification.vrf_date = RecInfoFactory.__create_xmldate_from_string(meter[COL_VRF_DATE])

        try:
            verification.valid_date = RecInfoFactory.__create_xmldate_from_string(meter[COL_VALID_DATE])
        except:
            verification.inapplicable = verification.Inapplicable()
            verification.inapplicable.reasons = 'Не соответствует требованиям МП'
        else:
            verification.applicable = verification.Applicable()
            verification.applicable.sign_pass = verification.applicable.sign_mi = False

        verification.metrologist = meter[COL_METROLOGIST]
        verification.means = MeansFactory.create_test(meter[COL_TEST_DEV_NUM])
        verification.conditions = ConditionsFactory.create_conditions_from_csv_row(meter)

        return verification
    
    @staticmethod
    def __create_default():
        verification = arshin.RecInfo()
        verification.sign_cipher = 'ДГХ'
        verification.mi_owner = 'ФИЗИЧЕСКОЕ ЛИЦО'
        verification.type = arshin.RecInfoType.VALUE_2
        verification.calibration = False
        verification.doc_title = 'МИ 1592-2015'
        return verification
    
    @staticmethod
    def __create_xmldate_from_string(string):
        try:
            date = datetime.strptime(string, '%d.%m.%Y').date()
        except:
            try:
                date = datetime.strptime(string, '%d/%m/%Y').date()
            except:
                raise exceptions.DateError('Неверный формат даты:', string,'Допустимые форматы: ДД.ММ.ГГГГ, ДД/ММ/ГГГГ')
        return XmlDate.from_string(date.isoformat())


class MiInfoFactory:
    @staticmethod
    def create_from_csv_row(meter):
        info = arshin.RecInfo.MiInfo()
        info.single_mi = info.SingleMi()
        info.single_mi.mitype_number = meter[COL_TYPE_NUM]
        info.single_mi.manufacture_num = meter[COL_MANUFACTURE_NUM]
        info.single_mi.modification = meter[COL_MODIFICATION]
        return info


class MeansFactory:
    @staticmethod
    def create_test(number):
        test = arshin.RecInfo.Means()
        test.mieta = test.Mieta()
        test.mieta.number = number
        return test


class ConditionsFactory:
    @staticmethod
    def create_conditions_from_csv_row(meter):
        conditions = arshin.RecInfo.Conditions()
        conditions.temperature = meter[COL_TEMPERATURE]
        conditions.hymidity = meter[COL_HUMIDITY]
        conditions.pressure = meter[COL_PRESSURE]
        return conditions
