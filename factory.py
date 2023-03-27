import models.arshin as arshin
from xsdata.models.datatype import XmlDate


class RecInfoFactory:
    def __init__(self, meter: list):
        self.meter = meter

    def SerializeVerification(self):
        verification = arshin.RecInfo()
        verification = self.__FillDefault(verification)
        verification.mi_info = MiInfoFactory(self.meter).SerializeMeterInfo()
        verification.vrf_date = XmlDate.from_string(self.__FormatDate(self.meter[3]))

        if self.meter[4] != '':
            verification.valid_date = XmlDate.from_string(self.__FormatDate(self.meter[4]))
            verification.applicable = verification.Applicable()
            verification.applicable.sign_pass = verification.applicable.sign_mi = False
        else:
            verification.inapplicable = verification.Inapplicable()
            verification.inapplicable.reasons = 'Не соответствует требованиям МП'

        verification.metrologist = self.meter[5]
        verification.means = MeansFactory(self.meter).SerializeTest()
        verification.conditions = ConditionsFactory(self.meter).SerializeConditions()

        return verification
    
    def __FillDefault(self, verification):
        verification.sign_cipher = 'ДГХ'
        verification.mi_owner = 'ФИЗИЧЕСКОЕ ЛИЦО'
        verification.type = arshin.RecInfoType.VALUE_2
        verification.calibration = False
        verification.doc_title = 'МИ 1592-2015'
        return verification
    
    @staticmethod
    def __FormatDate(string):
        date = string.split('.')[::-1]
        return '-'.join(date)
    
class MiInfoFactory:
    def __init__(self, meter):
        self.mitype_number = meter[0]
        self.manufacture_num = meter[1]
        self.modification = meter[2]

    def SerializeMeterInfo(self):
        info = arshin.RecInfo.MiInfo()
        info.single_mi = info.SingleMi()
        info.single_mi.mitype_number = self.mitype_number
        info.single_mi.manufacture_num = self.manufacture_num
        info.single_mi.modification = self.modification
        return info
    
class MeansFactory:
    def __init__(self, meter):
        self.number = meter[6]

    def SerializeTest(self):
        test = arshin.RecInfo.Means()
        test.mieta = test.Mieta()
        test.mieta.number = self.number
        return test
    
class ConditionsFactory:
    def __init__(self, meter):
        self.temperature = meter[7]
        self.hymidity =  meter[8]
        self.pressure = meter[9]

    def SerializeConditions(self):
        conditions = arshin.RecInfo.Conditions()
        conditions.temperature =  self.temperature
        conditions.hymidity =  self.hymidity
        conditions.pressure =  self.pressure
        return conditions