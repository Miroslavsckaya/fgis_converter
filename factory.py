import exceptions
import arshin
from datetime import datetime
from data_sources.interface import VerificationData
from typing import Generator
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


class ApplicationFactory:
    @staticmethod
    def create_application(verifications_data: Generator[VerificationData, None, None]) -> arshin.Application:
        application = arshin.Application()
        for verification_data in verifications_data:
            if verification_data is None:
                continue
            application.result.append(RecInfoFactory(verification_data))
        return application


class RecInfoFactory:
    @staticmethod
    def create_verification_from_csv_row(verification_data: VerificationData) -> arshin.RecInfo:
        verification = RecInfoFactory.__create_default()
        verification.mi_info = MiInfoFactory.create_from_verification_data(verification_data)
        verification.vrf_date = RecInfoFactory.__create_xmldate_from_string(verification_data)

        try:
            verification.valid_date = RecInfoFactory.__create_xmldate_from_string(verification_data.valid_date)
        except:
            verification.inapplicable = verification.Inapplicable()
            verification.inapplicable.reasons = 'Не соответствует требованиям МП'
        else:
            verification.applicable = verification.Applicable()
            verification.applicable.sign_pass = verification.applicable.sign_mi = False

        verification.metrologist = verification_data.metrologist
        verification.means = MeansFactory.create_test(verification_data.test_dev_num)
        verification.conditions = ConditionsFactory.create_conditions_from_verification_data(verification_data)

        return verification
    
    @staticmethod
    def __create_default() -> arshin.RecInfo:
        verification = arshin.RecInfo()
        verification.sign_cipher = 'ДГХ'
        verification.mi_owner = 'ФИЗИЧЕСКОЕ ЛИЦО'
        verification.type = arshin.RecInfoType.VALUE_2
        verification.calibration = False
        verification.doc_title = 'МИ 1592-2015'
        return verification
    
    @staticmethod
    def __create_xmldate_from_string(string: str) -> XmlDate:
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
    def create_from_verification_data(verification_data: VerificationData) -> arshin.RecInfo.MiInfo:
        info = arshin.RecInfo.MiInfo()
        info.single_mi = info.SingleMi()
        info.single_mi.mitype_number = verification_data.reg_num
        info.single_mi.manufacture_num = verification_data.factory_num
        info.single_mi.modification = verification_data.modification
        return info


class MeansFactory:
    @staticmethod
    def create_test(number: str) -> arshin.RecInfo.Means:
        test = arshin.RecInfo.Means()
        test.mieta = test.Mieta()
        test.mieta.number = number
        return test


class ConditionsFactory:
    @staticmethod
    def create_conditions_from_verification_data(verification_data: VerificationData) -> arshin.RecInfo.Conditions:
        conditions = arshin.RecInfo.Conditions()
        conditions.temperature = verification_data.temperature
        conditions.hymidity = verification_data.humidity
        conditions.pressure = verification_data.pressure
        return conditions
