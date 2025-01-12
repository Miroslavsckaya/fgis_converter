import arshin
import exceptions
import config
from data_sources.interface import VerificationData
from datetime import datetime, date, timedelta
from typing import Generator
from xsdata.models.datatype import XmlDate


LAST_VALID_DAY_INTERVAL = 1


class ApplicationFactory:
    @staticmethod
    def create_application(verifications_data: Generator[VerificationData, None, None]) -> arshin.Application:
        application = arshin.Application()
        for verification_data in verifications_data:
            application.result.append(RecInfoFactory.create_from_verification_data(verification_data))
        return application


class RecInfoFactory:
    @staticmethod
    def create_from_verification_data(verification_data: VerificationData) -> arshin.RecInfo:
        verification = RecInfoFactory.__create_default()
        verification.mi_info = MiInfoFactory.create_from_verification_data(verification_data)
        verification.vrf_date = RecInfoFactory.__create_xmldate_from_string(verification_data.ver_date, config.company_config['date_formats'])
        verification.sign_cipher = config.company_config['sign_cipher']
        verification.doc_title = config.valid_regnums[verification_data.reg_num]

        try:
            verification.valid_date = RecInfoFactory.__create_xmldate_from_string(verification_data.valid_date, config.company_config['date_formats'])
        except exceptions.DateError:
            verification.inapplicable = verification.Inapplicable()
            verification.inapplicable.reasons = 'Не соответствует требованиям МП'
        else:
            verification.valid_date = RecInfoFactory.__last_valid_day(verification.vrf_date, verification.valid_date)
            verification.applicable = verification.Applicable()
            verification.applicable.sign_pass = verification.applicable.sign_mi = False

        verification.metrologist = verification_data.metrologist
        verification.means = MeansFactory.create_test(verification_data.test_dev_num)
        verification.conditions = ConditionsFactory.create_from_verification_data(verification_data)

        return verification
    
    @staticmethod
    def __create_default() -> arshin.RecInfo:
        verification = arshin.RecInfo()
        verification.mi_owner = 'ФИЗИЧЕСКОЕ ЛИЦО'
        verification.type = arshin.RecInfoType.VALUE_2
        verification.calibration = False
        return verification

    @staticmethod
    def __create_xmldate_from_string(string: str, date_formats: list[str]) -> XmlDate:
        for date_format in date_formats:
            try:
                meter_date = datetime.strptime(string, date_format).date()
                return XmlDate.from_date(meter_date)
            except ValueError:
                continue

        raise exceptions.DateError('Неверный формат даты:', string,
                                    'Допустимые форматы: ДД.ММ.ГГГГ, ДД/ММ/ГГГГ')

    @staticmethod
    def __last_valid_day(vrf_date: XmlDate, valid_date: XmlDate) -> XmlDate:
        valid_date = date(valid_date.year, vrf_date.month, vrf_date.day)
        delta = timedelta(days=LAST_VALID_DAY_INTERVAL)
        return XmlDate.from_date(valid_date - delta)


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
    def create_from_verification_data(verification_data: VerificationData) -> arshin.RecInfo.Conditions:
        conditions = arshin.RecInfo.Conditions()
        conditions.temperature = verification_data.temperature
        conditions.hymidity = verification_data.humidity
        conditions.pressure = verification_data.pressure
        return conditions
