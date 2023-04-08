from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlPeriod

__NAMESPACE__ = "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19"


class MeansOMethod(Enum):
    """
    :cvar VALUE_1: «поверка имитационным методом»
    :cvar VALUE_2: «самоповерка»
    :cvar VALUE_3: «поверка расчетным методом»
    :cvar VALUE_4: «поверка с использованием первичной референтной
        методики измерений»
    """
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class ProtocolMimetype(Enum):
    APPLICATION_PDF = "application/pdf"
    APPLICATION_MSWORD = "application/msword"
    APPLICATION_ZIP = "application/zip"
    IMAGE_VND_DJVU = "image/vnd.djvu"


class RecInfoType(Enum):
    """
    :cvar VALUE_1: Первичная поверка
    :cvar VALUE_2: Периодическая поверка
    """
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class RecInfo:
    """
    Тип данных: запись о результатах поверки СИ.

    :ivar mi_info: Сведения о СИ, применяемом в качестве эталона / СИ /
        Партии СИ
    :ivar sign_cipher: Условный шифр знака поверки
    :ivar mi_owner: Владелец СИ
    :ivar vrf_date: Дата поверки СИ
    :ivar valid_date: Поверка действительна до Не указывается в случае,
        когда предусмотрена только первичная поверка
    :ivar type: Признак первичной или периодической поверки
    :ivar calibration: Признак поверки средства измерений с
        использованием результатов калибровки
    :ivar applicable: СИ пригодно
    :ivar inapplicable: СИ не пригодно
    :ivar doc_title: Наименование документа, на основании которого
        выполнена поверка
    :ivar metrologist: Ф.И.О. поверителя
    :ivar means: Средства поверки
    :ivar conditions: Условия проведения поверки
    :ivar structure: Состав СИ, представленного на поверку
    :ivar brief_procedure: Поверка в сокращенном объеме
    :ivar additional_info: Прочие сведения
    :ivar protocol: Протокол поверки
    """
    class Meta:
        name = "recInfo"

    mi_info: Optional["RecInfo.MiInfo"] = field(
        default=None,
        metadata={
            "name": "miInfo",
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "required": True,
        }
    )
    sign_cipher: Optional[str] = field(
        default=None,
        metadata={
            "name": "signCipher",
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "required": True,
            "pattern": r"[А-Я]{1,3}",
        }
    )
    mi_owner: Optional[str] = field(
        default=None,
        metadata={
            "name": "miOwner",
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "min_length": 1,
            "max_length": 512,
        }
    )
    vrf_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "vrfDate",
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "required": True,
        }
    )
    valid_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "validDate",
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
        }
    )
    type: Optional[RecInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "required": True,
        }
    )
    calibration: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "required": True,
        }
    )
    applicable: Optional["RecInfo.Applicable"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
        }
    )
    inapplicable: Optional["RecInfo.Inapplicable"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
        }
    )
    doc_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "docTitle",
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    metrologist: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "min_length": 1,
            "max_length": 128,
        }
    )
    means: Optional["RecInfo.Means"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "required": True,
        }
    )
    conditions: Optional["RecInfo.Conditions"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "required": True,
        }
    )
    structure: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "min_length": 1,
            "max_length": 1024,
        }
    )
    brief_procedure: Optional["RecInfo.BriefProcedure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
        }
    )
    additional_info: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            "min_length": 1,
            "max_length": 1024,
        }
    )
    protocol: Optional["RecInfo.Protocol"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
        }
    )

    @dataclass
    class MiInfo:
        """
        :ivar eta_mi: СИ, применяемое в качестве эталона
        :ivar single_mi: Сведения о единичном СИ
        """
        eta_mi: Optional["RecInfo.MiInfo.EtaMi"] = field(
            default=None,
            metadata={
                "name": "etaMI",
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            }
        )
        single_mi: Optional["RecInfo.MiInfo.SingleMi"] = field(
            default=None,
            metadata={
                "name": "singleMI",
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            }
        )

        @dataclass
        class EtaMi:
            """
            :ivar primary_rec: Первая поверка СИ, применяемого в
                качестве эталона Раздел заполняется, если СИ отсутствует
                в реестре ФИФ ОЕИ
            :ivar reg_number: Повторная поверка СИ, применяемого в
                качестве эталона Регистрационный номер СИ в реестре ФИФ
                ОЕИ
            """
            primary_rec: Optional["RecInfo.MiInfo.EtaMi.PrimaryRec"] = field(
                default=None,
                metadata={
                    "name": "primaryRec",
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                }
            )
            reg_number: Optional[str] = field(
                default=None,
                metadata={
                    "name": "regNumber",
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_length": 1,
                    "max_length": 32,
                }
            )

            @dataclass
            class PrimaryRec:
                """
                :ivar mitype_number: Номер в Госреестре утвержденного
                    типа СИ
                :ivar modification: Модификация СИ
                :ivar manufacture_num: Заводской номер СИ
                :ivar manufacture_year: Год выпуска СИ
                :ivar is_owner: Поверитель является владельцем СИ,
                    применяемого в качестве эталона
                :ivar gps: Государственная поверочная схема
                :ivar lps: Локальная поверочная схема
                :ivar mp: Методики поверки
                """
                mitype_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "mitypeNumber",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "required": True,
                        "min_length": 1,
                        "max_length": 32,
                    }
                )
                modification: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "required": True,
                        "min_length": 1,
                        "max_length": 128,
                    }
                )
                manufacture_num: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "manufactureNum",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "required": True,
                        "min_length": 1,
                        "max_length": 128,
                    }
                )
                manufacture_year: Optional[XmlPeriod] = field(
                    default=None,
                    metadata={
                        "name": "manufactureYear",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "required": True,
                    }
                )
                is_owner: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "isOwner",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "required": True,
                    }
                )
                gps: Optional["RecInfo.MiInfo.EtaMi.PrimaryRec.Gps"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    }
                )
                lps: Optional["RecInfo.MiInfo.EtaMi.PrimaryRec.Lps"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    }
                )
                mp: Optional["RecInfo.MiInfo.EtaMi.PrimaryRec.Mp"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    }
                )

                @dataclass
                class Gps:
                    """
                    :ivar title: Наименование Государственной поверочной
                        схемы
                    :ivar npe_number: Регистрационный номер ГПЭ, к
                        которому прослеживается СИ, применяемое в
                        качестве эталона
                    :ivar rank: Разряд в поверочной схеме
                    """
                    title: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                            "required": True,
                            "min_length": 1,
                            "max_length": 128,
                        }
                    )
                    npe_number: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "npeNumber",
                            "type": "Element",
                            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                            "required": True,
                            "min_length": 1,
                            "max_length": 32,
                        }
                    )
                    rank: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                            "required": True,
                            "min_length": 1,
                            "max_length": 32,
                        }
                    )

                @dataclass
                class Lps:
                    """
                    :ivar title: Наименование локальной поверочной схемы
                    :ivar npe_number: Регистрационный номер ГПЭ, к
                        которому прослеживается СИ, применяемое в
                        качестве эталона
                    :ivar rank: Разряд в поверочной схеме
                    """
                    title: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                            "required": True,
                            "min_length": 1,
                            "max_length": 128,
                        }
                    )
                    npe_number: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "npeNumber",
                            "type": "Element",
                            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                            "required": True,
                            "min_length": 1,
                            "max_length": 32,
                        }
                    )
                    rank: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                            "required": True,
                            "min_length": 1,
                            "max_length": 32,
                        }
                    )

                @dataclass
                class Mp:
                    """
                    :ivar title: Наименования методик поверки
                    """
                    title: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                            "min_length": 1,
                            "max_length": 128,
                        }
                    )

        @dataclass
        class SingleMi:
            """
            :ivar mitype_number: Номер в Госреестре утвержденного типа
                СИ
            :ivar crtmitype_title: Метрологическая аттестация:
                наименование типа СИ
            :ivar milmitype_title: СИ, поступившее в эксплуатацию до
                01.06.1993 г.
            :ivar manufacture_num: Заводской номер СИ
            :ivar inventory_num: Инвентарный номер СИ
            :ivar manufacture_year: Год выпуска СИ
            :ivar modification: Модификация СИ
            """
            mitype_number: Optional[str] = field(
                default=None,
                metadata={
                    "name": "mitypeNumber",
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_length": 1,
                    "max_length": 32,
                }
            )
            crtmitype_title: Optional[str] = field(
                default=None,
                metadata={
                    "name": "crtmitypeTitle",
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_length": 1,
                    "max_length": 512,
                }
            )
            milmitype_title: Optional[str] = field(
                default=None,
                metadata={
                    "name": "milmitypeTitle",
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_length": 1,
                    "max_length": 512,
                }
            )
            manufacture_num: Optional[str] = field(
                default=None,
                metadata={
                    "name": "manufactureNum",
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_length": 1,
                    "max_length": 128,
                }
            )
            inventory_num: Optional[str] = field(
                default=None,
                metadata={
                    "name": "inventoryNum",
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_length": 1,
                    "max_length": 128,
                }
            )
            manufacture_year: Optional[XmlPeriod] = field(
                default=None,
                metadata={
                    "name": "manufactureYear",
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                }
            )
            modification: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "required": True,
                    "min_length": 1,
                    "max_length": 128,
                }
            )

    @dataclass
    class Means:
        """
        :ivar npe: Государственные первичные эталоны
        :ivar uve: Эталоны единицы величины
        :ivar ses: Стандартные образцы
        :ivar mieta: Средство измерения, применяемое в качестве эталона
        :ivar mis: Средства измерения, применяемые при поверке
        :ivar reagent: Вещество (материал), применяемый при поверке
        :ivar o_method: Доп. методы, использованные при поверке
        """
        npe: List["RecInfo.Means.Npe"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            }
        )
        uve: List["RecInfo.Means.Uve"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            }
        )
        ses: List["RecInfo.Means.Ses"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            }
        )
        mieta: List["RecInfo.Means.Mieta"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            }
        )
        mis: List["RecInfo.Means.Mis"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            }
        )
        reagent: List["RecInfo.Means.Reagent"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            }
        )
        o_method: List[MeansOMethod] = field(
            default_factory=list,
            metadata={
                "name": "oMethod",
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
            }
        )

        @dataclass
        class Npe:
            """
            :ivar number: Номер ГПЭ по реестру
            """
            number: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_occurs": 1,
                    "min_length": 1,
                    "max_length": 32,
                }
            )

        @dataclass
        class Uve:
            """
            :ivar number: Номер эталона по реестру
            """
            number: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_occurs": 1,
                    "min_length": 1,
                    "max_length": 32,
                }
            )

        @dataclass
        class Ses:
            """
            :ivar se: Стандартный образец
            """
            se: List["RecInfo.Means.Ses.Se"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class Se:
                """
                :ivar type_num: Номер типа СО по реестру
                :ivar manufacture_year: Год выпуска
                :ivar manufacture_num: Заводские номера / Номера партии
                :ivar metro_chars: Метрологические характеристики СО
                """
                type_num: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "typeNum",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "required": True,
                        "min_length": 1,
                        "max_length": 128,
                    }
                )
                manufacture_year: Optional[XmlPeriod] = field(
                    default=None,
                    metadata={
                        "name": "manufactureYear",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "required": True,
                    }
                )
                manufacture_num: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "manufactureNum",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "min_length": 1,
                        "max_length": 128,
                    }
                )
                metro_chars: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "metroChars",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "min_length": 1,
                        "max_length": 1024,
                    }
                )

        @dataclass
        class Mieta:
            """
            :ivar number: Номер СИ по реестру
            """
            number: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_occurs": 1,
                    "min_length": 1,
                    "max_length": 32,
                }
            )

        @dataclass
        class Mis:
            """
            :ivar mi: Средство измерения, применяемое при поверке
            """
            mi: List["RecInfo.Means.Mis.Mi"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class Mi:
                """
                :ivar type_num: Регистрационный номер типа СИ
                :ivar manufacture_num: Заводской номер СИ
                :ivar inventory_num: Инвентарный номер СИ
                """
                type_num: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "typeNum",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "required": True,
                        "min_length": 1,
                        "max_length": 32,
                    }
                )
                manufacture_num: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "manufactureNum",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "min_length": 1,
                        "max_length": 128,
                    }
                )
                inventory_num: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "inventoryNum",
                        "type": "Element",
                        "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                        "min_length": 1,
                        "max_length": 128,
                    }
                )

        @dataclass
        class Reagent:
            """
            :ivar number: Номер вещества (материала) по реестру
            """
            number: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                    "min_occurs": 1,
                    "min_length": 1,
                    "max_length": 32,
                }
            )

    @dataclass
    class Conditions:
        """
        :ivar temperature: Температура
        :ivar pressure: Атмосферное давление
        :ivar hymidity: Относительная влажность
        :ivar other: Другие влияющие факторы
        """
        temperature: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
                "min_length": 1,
                "max_length": 128,
            }
        )
        pressure: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
                "min_length": 1,
                "max_length": 128,
            }
        )
        hymidity: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
                "min_length": 1,
                "max_length": 128,
            }
        )
        other: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "min_length": 1,
                "max_length": 128,
            }
        )

    @dataclass
    class BriefProcedure:
        """
        :ivar characteristics: Краткая характеристика объема поверки
        """
        characteristics: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
                "min_length": 1,
                "max_length": 1024,
            }
        )

    @dataclass
    class Protocol:
        """
        :ivar content: Содержимое файла протокола поверки
        :ivar mimetype: Тип файла
        :ivar filename: Наименование файла
        """
        content: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
                "format": "base64",
            }
        )
        mimetype: Optional[ProtocolMimetype] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
            }
        )
        filename: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
                "min_length": 1,
                "max_length": 128,
            }
        )

    @dataclass
    class Applicable:
        """
        :ivar sticker_num: Номер наклейки
        :ivar sign_pass: Знак поверки в паспорте
        :ivar sign_mi: Знак поверки на СИ
        """
        sticker_num: Optional[str] = field(
            default=None,
            metadata={
                "name": "stickerNum",
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
                "pattern": r"[0-9]{11}",
            }
        )
        sign_pass: Optional[bool] = field(
            default=None,
            metadata={
                "name": "signPass",
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
            }
        )
        sign_mi: Optional[bool] = field(
            default=None,
            metadata={
                "name": "signMi",
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
            }
        )

    @dataclass
    class Inapplicable:
        """
        :ivar reasons: Причины непригодности
        """
        reasons: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19",
                "required": True,
                "min_length": 1,
                "max_length": 1024,
            }
        )


@dataclass
class Application:
    """
    Заявка на публикацию сведений о результатах поверки СИ.

    :ivar result: Сведения о результатах поверки СИ
    """
    class Meta:
        name = "application"
        namespace = "urn://fgis-arshin.gost.ru/module-verifications/import/2020-06-19"

    result: List[RecInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
