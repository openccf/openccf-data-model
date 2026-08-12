# Auto generated from openccf.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-08-12T09:12:16
# Schema: openccf
#
# id: https://w3id.org/openccf
# description: An open, interoperable data model for exchanging GHG Protocol-aligned corporate carbon footprints between systems. Released under CC0-1.0.
# license: CC0-1.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Date, Float, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.11.0"
version = "1.0.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OPENCCF = CurieNamespace('openccf', 'https://w3id.org/openccf/')
DEFAULT_ = OPENCCF


# Types

# Class references
class EmissionsReportReportID(extended_str):
    pass


@dataclass(repr=False)
class EmissionsReport(YAMLRoot):
    """
    A company's greenhouse gas footprint for a defined reporting period. Acts as the container for one or more
    Emissions Lines. The location-based net total is always present; the market-based total is present only where the
    report contains market-based electricity lines. The derivation of each total from its lines is a semantic
    constraint, verified by the conformance tests rather than by schema validation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["EmissionsReport"]
    class_class_curie: ClassVar[str] = "openccf:EmissionsReport"
    class_name: ClassVar[str] = "EmissionsReport"
    class_model_uri: ClassVar[URIRef] = OPENCCF.EmissionsReport

    reportID: Union[str, EmissionsReportReportID] = None
    schemaVersion: str = None
    companyName: str = None
    primaryRegion: str = None
    reportingPeriodStart: Union[str, XSDDate] = None
    reportingPeriodEnd: Union[str, XSDDate] = None
    totalNetEmissionsLocationBasedKgCO2e: float = None
    gwpHorizon: Union[str, "GwpHorizonEnum"] = None
    reportStatus: Union[str, "ReportStatusEnum"] = None
    emissionsLines: Union[Union[dict, "EmissionsLine"], list[Union[dict, "EmissionsLine"]]] = None
    totalNetEmissionsMarketBasedKgCO2e: Optional[float] = None
    sectors: Optional[Union[Union[dict, "Sector"], list[Union[dict, "Sector"]]]] = empty_list()
    companyIdentifiers: Optional[Union[Union[dict, "CompanyIdentifier"], list[Union[dict, "CompanyIdentifier"]]]] = empty_list()
    intensityDenominators: Optional[Union[Union[dict, "IntensityDenominator"], list[Union[dict, "IntensityDenominator"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reportID):
            self.MissingRequiredField("reportID")
        if not isinstance(self.reportID, EmissionsReportReportID):
            self.reportID = EmissionsReportReportID(self.reportID)

        if self._is_empty(self.schemaVersion):
            self.MissingRequiredField("schemaVersion")
        if not isinstance(self.schemaVersion, str):
            self.schemaVersion = str(self.schemaVersion)

        if self._is_empty(self.companyName):
            self.MissingRequiredField("companyName")
        if not isinstance(self.companyName, str):
            self.companyName = str(self.companyName)

        if self._is_empty(self.primaryRegion):
            self.MissingRequiredField("primaryRegion")
        if not isinstance(self.primaryRegion, str):
            self.primaryRegion = str(self.primaryRegion)

        if self._is_empty(self.reportingPeriodStart):
            self.MissingRequiredField("reportingPeriodStart")
        if not isinstance(self.reportingPeriodStart, XSDDate):
            self.reportingPeriodStart = XSDDate(self.reportingPeriodStart)

        if self._is_empty(self.reportingPeriodEnd):
            self.MissingRequiredField("reportingPeriodEnd")
        if not isinstance(self.reportingPeriodEnd, XSDDate):
            self.reportingPeriodEnd = XSDDate(self.reportingPeriodEnd)

        if self._is_empty(self.totalNetEmissionsLocationBasedKgCO2e):
            self.MissingRequiredField("totalNetEmissionsLocationBasedKgCO2e")
        if not isinstance(self.totalNetEmissionsLocationBasedKgCO2e, float):
            self.totalNetEmissionsLocationBasedKgCO2e = float(self.totalNetEmissionsLocationBasedKgCO2e)

        if self._is_empty(self.gwpHorizon):
            self.MissingRequiredField("gwpHorizon")
        if not isinstance(self.gwpHorizon, GwpHorizonEnum):
            self.gwpHorizon = GwpHorizonEnum(self.gwpHorizon)

        if self._is_empty(self.reportStatus):
            self.MissingRequiredField("reportStatus")
        if not isinstance(self.reportStatus, ReportStatusEnum):
            self.reportStatus = ReportStatusEnum(self.reportStatus)

        if self._is_empty(self.emissionsLines):
            self.MissingRequiredField("emissionsLines")
        self._normalize_inlined_as_list(slot_name="emissionsLines", slot_type=EmissionsLine, key_name="scope", keyed=False)

        if self.totalNetEmissionsMarketBasedKgCO2e is not None and not isinstance(self.totalNetEmissionsMarketBasedKgCO2e, float):
            self.totalNetEmissionsMarketBasedKgCO2e = float(self.totalNetEmissionsMarketBasedKgCO2e)

        if not isinstance(self.sectors, list):
            self.sectors = [self.sectors] if self.sectors is not None else []
        self.sectors = [v if isinstance(v, Sector) else Sector(**as_dict(v)) for v in self.sectors]

        if not isinstance(self.companyIdentifiers, list):
            self.companyIdentifiers = [self.companyIdentifiers] if self.companyIdentifiers is not None else []
        self.companyIdentifiers = [v if isinstance(v, CompanyIdentifier) else CompanyIdentifier(**as_dict(v)) for v in self.companyIdentifiers]

        if not isinstance(self.intensityDenominators, list):
            self.intensityDenominators = [self.intensityDenominators] if self.intensityDenominators is not None else []
        self.intensityDenominators = [v if isinstance(v, IntensityDenominator) else IntensityDenominator(**as_dict(v)) for v in self.intensityDenominators]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmissionsLine(YAMLRoot):
    """
    A single quantified source or category of emissions within a report. Lines are flat; totals and subtotals are
    derived by grouping, not nesting.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["EmissionsLine"]
    class_class_curie: ClassVar[str] = "openccf:EmissionsLine"
    class_name: ClassVar[str] = "EmissionsLine"
    class_model_uri: ClassVar[URIRef] = OPENCCF.EmissionsLine

    scope: Union[str, "ScopeEnum"] = None
    category: Union[str, "EmissionCategoryEnum"] = None
    lineStatus: Union[str, "LineStatusEnum"] = None
    emissionsQuantityKgCO2e: float = None
    emissionOrigin: Union[str, "EmissionOriginEnum"] = None
    region: str = None
    subcategory: Optional[str] = None
    accountingType: Optional[Union[str, "AccountingTypeEnum"]] = 'EMISSION'
    companyFacilityIdentifier: Optional[str] = None
    emissionFactor: Optional[Union[dict, "EmissionFactor"]] = None
    dataQuality: Optional[Union[dict, "DataQuality"]] = None
    dataQualityInformation: Optional[str] = None
    gasBreakdown: Optional[Union[Union[dict, "GasBreakdown"], list[Union[dict, "GasBreakdown"]]]] = empty_list()
    activityData: Optional[Union[dict, "ActivityData"]] = None
    landSectorData: Optional[Union[dict, "LandSectorData"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scope):
            self.MissingRequiredField("scope")
        if not isinstance(self.scope, ScopeEnum):
            self.scope = ScopeEnum(self.scope)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, EmissionCategoryEnum):
            self.category = EmissionCategoryEnum(self.category)

        if self._is_empty(self.lineStatus):
            self.MissingRequiredField("lineStatus")
        if not isinstance(self.lineStatus, LineStatusEnum):
            self.lineStatus = LineStatusEnum(self.lineStatus)

        if self._is_empty(self.emissionsQuantityKgCO2e):
            self.MissingRequiredField("emissionsQuantityKgCO2e")
        if not isinstance(self.emissionsQuantityKgCO2e, float):
            self.emissionsQuantityKgCO2e = float(self.emissionsQuantityKgCO2e)

        if self._is_empty(self.emissionOrigin):
            self.MissingRequiredField("emissionOrigin")
        if not isinstance(self.emissionOrigin, EmissionOriginEnum):
            self.emissionOrigin = EmissionOriginEnum(self.emissionOrigin)

        if self._is_empty(self.region):
            self.MissingRequiredField("region")
        if not isinstance(self.region, str):
            self.region = str(self.region)

        if self.subcategory is not None and not isinstance(self.subcategory, str):
            self.subcategory = str(self.subcategory)

        if self.accountingType is not None and not isinstance(self.accountingType, AccountingTypeEnum):
            self.accountingType = AccountingTypeEnum(self.accountingType)

        if self.companyFacilityIdentifier is not None and not isinstance(self.companyFacilityIdentifier, str):
            self.companyFacilityIdentifier = str(self.companyFacilityIdentifier)

        if self.emissionFactor is not None and not isinstance(self.emissionFactor, EmissionFactor):
            self.emissionFactor = EmissionFactor(**as_dict(self.emissionFactor))

        if self.dataQuality is not None and not isinstance(self.dataQuality, DataQuality):
            self.dataQuality = DataQuality(**as_dict(self.dataQuality))

        if self.dataQualityInformation is not None and not isinstance(self.dataQualityInformation, str):
            self.dataQualityInformation = str(self.dataQualityInformation)

        self._normalize_inlined_as_list(slot_name="gasBreakdown", slot_type=GasBreakdown, key_name="gas", keyed=False)

        if self.activityData is not None and not isinstance(self.activityData, ActivityData):
            self.activityData = ActivityData(**as_dict(self.activityData))

        if self.landSectorData is not None and not isinstance(self.landSectorData, LandSectorData):
            self.landSectorData = LandSectorData(**as_dict(self.landSectorData))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sector(YAMLRoot):
    """
    Standardised sector classification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["Sector"]
    class_class_curie: ClassVar[str] = "openccf:Sector"
    class_name: ClassVar[str] = "Sector"
    class_model_uri: ClassVar[URIRef] = OPENCCF.Sector

    scheme: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.scheme is not None and not isinstance(self.scheme, str):
            self.scheme = str(self.scheme)

        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompanyIdentifier(YAMLRoot):
    """
    Standardised company identifier.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["CompanyIdentifier"]
    class_class_curie: ClassVar[str] = "openccf:CompanyIdentifier"
    class_name: ClassVar[str] = "CompanyIdentifier"
    class_model_uri: ClassVar[URIRef] = OPENCCF.CompanyIdentifier

    scheme: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.scheme is not None and not isinstance(self.scheme, str):
            self.scheme = str(self.scheme)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntensityDenominator(YAMLRoot):
    """
    A denominator for calculating intensity values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["IntensityDenominator"]
    class_class_curie: ClassVar[str] = "openccf:IntensityDenominator"
    class_name: ClassVar[str] = "IntensityDenominator"
    class_model_uri: ClassVar[URIRef] = OPENCCF.IntensityDenominator

    type: Optional[str] = None
    value: Optional[float] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmissionFactor(YAMLRoot):
    """
    Metadata describing the emission factor applied to a line.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["EmissionFactor"]
    class_class_curie: ClassVar[str] = "openccf:EmissionFactor"
    class_name: ClassVar[str] = "EmissionFactor"
    class_model_uri: ClassVar[URIRef] = OPENCCF.EmissionFactor

    source: str = None
    dataYear: int = None
    ipccBasis: Union[str, "IpccBasisEnum"] = None
    value: Optional[float] = None
    valueUnit: Optional[str] = None
    dataset: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.dataYear):
            self.MissingRequiredField("dataYear")
        if not isinstance(self.dataYear, int):
            self.dataYear = int(self.dataYear)

        if self._is_empty(self.ipccBasis):
            self.MissingRequiredField("ipccBasis")
        if not isinstance(self.ipccBasis, IpccBasisEnum):
            self.ipccBasis = IpccBasisEnum(self.ipccBasis)

        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.valueUnit is not None and not isinstance(self.valueUnit, str):
            self.valueUnit = str(self.valueUnit)

        if self.dataset is not None and not isinstance(self.dataset, str):
            self.dataset = str(self.dataset)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GasBreakdown(YAMLRoot):
    """
    Constituent gas-level resolution of a line's emissions. Where a breakdown is provided it must be complete: the sum
    of gasCO2eContribution across entries equals the line's emissionsQuantityKgCO2e, within a small rounding tolerance
    (relative 0.1% with an absolute floor for near-zero lines). Any portion not attributable to a named gas is carried
    as an explicit OTHER entry rather than left implicit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["GasBreakdown"]
    class_class_curie: ClassVar[str] = "openccf:GasBreakdown"
    class_name: ClassVar[str] = "GasBreakdown"
    class_model_uri: ClassVar[URIRef] = OPENCCF.GasBreakdown

    gas: Union[str, "GasEnum"] = None
    gasQuantity: Optional[float] = None
    gasCO2eContribution: Optional[float] = None
    emissionOrigin: Optional[Union[str, "EmissionOriginEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gas):
            self.MissingRequiredField("gas")
        if not isinstance(self.gas, GasEnum):
            self.gas = GasEnum(self.gas)

        if self.gasQuantity is not None and not isinstance(self.gasQuantity, float):
            self.gasQuantity = float(self.gasQuantity)

        if self.gasCO2eContribution is not None and not isinstance(self.gasCO2eContribution, float):
            self.gasCO2eContribution = float(self.gasCO2eContribution)

        if self.emissionOrigin is not None and not isinstance(self.emissionOrigin, EmissionOriginEnum):
            self.emissionOrigin = EmissionOriginEnum(self.emissionOrigin)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityData(YAMLRoot):
    """
    Optional activity information underlying the emissions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["ActivityData"]
    class_class_curie: ClassVar[str] = "openccf:ActivityData"
    class_name: ClassVar[str] = "ActivityData"
    class_model_uri: ClassVar[URIRef] = OPENCCF.ActivityData

    description: Optional[str] = None
    lifecycleStage: Optional[str] = None
    value: Optional[float] = None
    unit: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.lifecycleStage is not None and not isinstance(self.lifecycleStage, str):
            self.lifecycleStage = str(self.lifecycleStage)

        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.unit is not None and not isinstance(self.unit, str):
            self.unit = str(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataQuality(YAMLRoot):
    """
    Data quality of an emissions line, aligned to the GHG Protocol Scope 3 Standard's five data quality indicators.
    The assessment reflects both the activity data and the emission factor used: the representativeness axes describe
    how well the inputs match this line's technology, period and geography, while completeness and reliability
    describe the underlying data and its sources. Each axis is rated Poor to Very good. (A GHG Protocol revision
    toward a data-specificity framework is in progress; this structure will track it in a future version.)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["DataQuality"]
    class_class_curie: ClassVar[str] = "openccf:DataQuality"
    class_name: ClassVar[str] = "DataQuality"
    class_model_uri: ClassVar[URIRef] = OPENCCF.DataQuality

    technologicalRepresentativeness: Optional[Union[str, "DataQualityRatingEnum"]] = None
    temporalRepresentativeness: Optional[Union[str, "DataQualityRatingEnum"]] = None
    geographicalRepresentativeness: Optional[Union[str, "DataQualityRatingEnum"]] = None
    completeness: Optional[Union[str, "DataQualityRatingEnum"]] = None
    reliability: Optional[Union[str, "DataQualityRatingEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.technologicalRepresentativeness is not None and not isinstance(self.technologicalRepresentativeness, DataQualityRatingEnum):
            self.technologicalRepresentativeness = DataQualityRatingEnum(self.technologicalRepresentativeness)

        if self.temporalRepresentativeness is not None and not isinstance(self.temporalRepresentativeness, DataQualityRatingEnum):
            self.temporalRepresentativeness = DataQualityRatingEnum(self.temporalRepresentativeness)

        if self.geographicalRepresentativeness is not None and not isinstance(self.geographicalRepresentativeness, DataQualityRatingEnum):
            self.geographicalRepresentativeness = DataQualityRatingEnum(self.geographicalRepresentativeness)

        if self.completeness is not None and not isinstance(self.completeness, DataQualityRatingEnum):
            self.completeness = DataQualityRatingEnum(self.completeness)

        if self.reliability is not None and not isinstance(self.reliability, DataQualityRatingEnum):
            self.reliability = DataQualityRatingEnum(self.reliability)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LandSectorData(YAMLRoot):
    """
    Optional land sector and removals metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OPENCCF["LandSectorData"]
    class_class_curie: ClassVar[str] = "openccf:LandSectorData"
    class_name: ClassVar[str] = "LandSectorData"
    class_model_uri: ClassVar[URIRef] = OPENCCF.LandSectorData

    boundary: Optional[str] = None
    storageDuration: Optional[str] = None
    monitoringApproach: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.boundary is not None and not isinstance(self.boundary, str):
            self.boundary = str(self.boundary)

        if self.storageDuration is not None and not isinstance(self.storageDuration, str):
            self.storageDuration = str(self.storageDuration)

        if self.monitoringApproach is not None and not isinstance(self.monitoringApproach, str):
            self.monitoringApproach = str(self.monitoringApproach)

        super().__post_init__(**kwargs)


# Enumerations
class ScopeEnum(EnumDefinitionImpl):

    SCOPE_1 = PermissibleValue(
        text="SCOPE_1",
        description="Direct emissions from owned or controlled sources.")
    SCOPE_2 = PermissibleValue(
        text="SCOPE_2",
        description="Indirect emissions from purchased energy.")
    SCOPE_3 = PermissibleValue(
        text="SCOPE_3",
        description="All other indirect value-chain emissions.")

    _defn = EnumDefinition(
        name="ScopeEnum",
    )

class EmissionCategoryEnum(EnumDefinitionImpl):
    """
    Source classification. Valid values are scope-dependent; the scope-to-category validity constraint is enforced by
    rules on EmissionsLine.
    """
    STATIONARY_COMBUSTION = PermissibleValue(
        text="STATIONARY_COMBUSTION",
        description="Scope 1: Stationary combustion.")
    MOBILE_COMBUSTION = PermissibleValue(
        text="MOBILE_COMBUSTION",
        description="Scope 1: Mobile combustion.")
    PROCESS_EMISSIONS = PermissibleValue(
        text="PROCESS_EMISSIONS",
        description="Scope 1: Process emissions from physical or chemical processes.")
    FUGITIVE = PermissibleValue(
        text="FUGITIVE",
        description="Scope 1: Fugitive emissions.")
    ELECTRICITY_MARKET_BASED = PermissibleValue(
        text="ELECTRICITY_MARKET_BASED",
        description="Scope 2: Purchased electricity (market-based method).")
    ELECTRICITY_LOCATION_BASED = PermissibleValue(
        text="ELECTRICITY_LOCATION_BASED",
        description="Scope 2: Purchased electricity (location-based method).")
    HEAT_STEAM_COOLING = PermissibleValue(
        text="HEAT_STEAM_COOLING",
        description="Scope 2: Purchased heat, steam and cooling.")
    S3_01_PURCHASED_GOODS_SERVICES = PermissibleValue(
        text="S3_01_PURCHASED_GOODS_SERVICES",
        description="Category 1: Purchased goods and services.")
    S3_02_CAPITAL_GOODS = PermissibleValue(
        text="S3_02_CAPITAL_GOODS",
        description="Category 2: Capital goods.")
    S3_03_FUEL_ENERGY_RELATED = PermissibleValue(
        text="S3_03_FUEL_ENERGY_RELATED",
        description="Category 3: Fuel- and energy-related activities (not included in Scope 1 or Scope 2).")
    S3_04_UPSTREAM_TRANSPORT = PermissibleValue(
        text="S3_04_UPSTREAM_TRANSPORT",
        description="Category 4: Upstream transportation and distribution.")
    S3_05_WASTE_IN_OPERATIONS = PermissibleValue(
        text="S3_05_WASTE_IN_OPERATIONS",
        description="Category 5: Waste generated in operations.")
    S3_06_BUSINESS_TRAVEL = PermissibleValue(
        text="S3_06_BUSINESS_TRAVEL",
        description="Category 6: Business travel.")
    S3_07_EMPLOYEE_COMMUTING = PermissibleValue(
        text="S3_07_EMPLOYEE_COMMUTING",
        description="Category 7: Employee commuting.")
    S3_08_UPSTREAM_LEASED_ASSETS = PermissibleValue(
        text="S3_08_UPSTREAM_LEASED_ASSETS",
        description="Category 8: Upstream leased assets.")
    S3_09_DOWNSTREAM_TRANSPORT = PermissibleValue(
        text="S3_09_DOWNSTREAM_TRANSPORT",
        description="Category 9: Downstream transportation and distribution.")
    S3_10_PROCESSING_SOLD_PRODUCTS = PermissibleValue(
        text="S3_10_PROCESSING_SOLD_PRODUCTS",
        description="Category 10: Processing of sold products.")
    S3_11_USE_OF_SOLD_PRODUCTS = PermissibleValue(
        text="S3_11_USE_OF_SOLD_PRODUCTS",
        description="Category 11: Use of sold products.")
    S3_12_EOL_SOLD_PRODUCTS = PermissibleValue(
        text="S3_12_EOL_SOLD_PRODUCTS",
        description="Category 12: End-of-life treatment of sold products.")
    S3_13_DOWNSTREAM_LEASED_ASSETS = PermissibleValue(
        text="S3_13_DOWNSTREAM_LEASED_ASSETS",
        description="Category 13: Downstream leased assets.")
    S3_14_FRANCHISES = PermissibleValue(
        text="S3_14_FRANCHISES",
        description="Category 14: Franchises.")
    S3_15_INVESTMENTS = PermissibleValue(
        text="S3_15_INVESTMENTS",
        description="Category 15: Investments.")
    NOT_SPECIFIED = PermissibleValue(
        text="NOT_SPECIFIED",
        description="Category not specified or not disclosed by the source.")

    _defn = EnumDefinition(
        name="EmissionCategoryEnum",
        description="""Source classification. Valid values are scope-dependent; the scope-to-category validity constraint is enforced by rules on EmissionsLine.""",
    )

class LineStatusEnum(EnumDefinitionImpl):
    """
    Completeness of this line. Assurance status is recorded at report level.
    """
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="Fully measured or calculated for the reporting period.")
    INCOMPLETE = PermissibleValue(
        text="INCOMPLETE",
        description="Partially measured; known to under-represent the total for this line.")
    EXCLUDED = PermissibleValue(
        text="EXCLUDED",
        description="Explicitly excluded from the report.")

    _defn = EnumDefinition(
        name="LineStatusEnum",
        description="Completeness of this line. Assurance status is recorded at report level.",
    )

class ReportStatusEnum(EnumDefinitionImpl):

    INCOMPLETE = PermissibleValue(
        text="INCOMPLETE",
        description="Not for utilisation as a full company report.")
    SELF_COMPLETED = PermissibleValue(text="SELF_COMPLETED")
    THIRD_PARTY_COMPLETED = PermissibleValue(text="THIRD_PARTY_COMPLETED")
    THIRD_PARTY_AUDITED = PermissibleValue(text="THIRD_PARTY_AUDITED")

    _defn = EnumDefinition(
        name="ReportStatusEnum",
    )

class EmissionOriginEnum(EnumDefinitionImpl):

    FOSSIL = PermissibleValue(text="FOSSIL")
    BIOGENIC = PermissibleValue(text="BIOGENIC")
    MIXED = PermissibleValue(
        text="MIXED",
        description="Origin cannot be disaggregated in the source data.")
    NOT_SPECIFIED = PermissibleValue(
        text="NOT_SPECIFIED",
        description="Underlying data does not distinguish origin.")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        description="Origin concept not relevant for this gas.")

    _defn = EnumDefinition(
        name="EmissionOriginEnum",
    )

class AccountingTypeEnum(EnumDefinitionImpl):

    EMISSION = PermissibleValue(text="EMISSION")
    REMOVAL = PermissibleValue(text="REMOVAL")
    GROSS_CO2_FLUX = PermissibleValue(
        text="GROSS_CO2_FLUX",
        description="Additional disclosure.")
    REVERSAL = PermissibleValue(text="REVERSAL")
    OTHER_LAND_SECTOR_DISCLOSURE = PermissibleValue(
        text="OTHER_LAND_SECTOR_DISCLOSURE",
        description="Reserved for future expansion.")

    _defn = EnumDefinition(
        name="AccountingTypeEnum",
    )

class GwpHorizonEnum(EnumDefinitionImpl):

    GWP20 = PermissibleValue(text="GWP20")
    GWP100 = PermissibleValue(text="GWP100")
    GWP500 = PermissibleValue(text="GWP500")

    _defn = EnumDefinition(
        name="GwpHorizonEnum",
    )

class IpccBasisEnum(EnumDefinitionImpl):

    AR4 = PermissibleValue(text="AR4")
    AR5 = PermissibleValue(text="AR5")
    AR6 = PermissibleValue(text="AR6")
    NOT_SPECIFIED = PermissibleValue(text="NOT_SPECIFIED")

    _defn = EnumDefinition(
        name="IpccBasisEnum",
    )

class GasEnum(EnumDefinitionImpl):

    CO2 = PermissibleValue(text="CO2")
    CH4 = PermissibleValue(text="CH4")
    N2O = PermissibleValue(text="N2O")
    HFC = PermissibleValue(
        text="HFC",
        description="With subtype to be specified.")
    PFC = PermissibleValue(text="PFC")
    SF6 = PermissibleValue(text="SF6")
    NF3 = PermissibleValue(text="NF3")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Specified separately.")

    _defn = EnumDefinition(
        name="GasEnum",
    )

class DataQualityRatingEnum(EnumDefinitionImpl):
    """
    GHG Protocol data quality indicator rating (Poor to Very good).
    """
    VERY_GOOD = PermissibleValue(text="VERY_GOOD")
    GOOD = PermissibleValue(text="GOOD")
    FAIR = PermissibleValue(text="FAIR")
    POOR = PermissibleValue(text="POOR")

    _defn = EnumDefinition(
        name="DataQualityRatingEnum",
        description="GHG Protocol data quality indicator rating (Poor to Very good).",
    )

# Slots
class slots:
    pass

slots.emissionsReport__reportID = Slot(uri=OPENCCF.reportID, name="emissionsReport__reportID", curie=OPENCCF.curie('reportID'),
                   model_uri=OPENCCF.emissionsReport__reportID, domain=None, range=URIRef)

slots.emissionsReport__schemaVersion = Slot(uri=OPENCCF.schemaVersion, name="emissionsReport__schemaVersion", curie=OPENCCF.curie('schemaVersion'),
                   model_uri=OPENCCF.emissionsReport__schemaVersion, domain=None, range=str,
                   pattern=re.compile(r'^\d+\.\d+\.\d+$'))

slots.emissionsReport__companyName = Slot(uri=OPENCCF.companyName, name="emissionsReport__companyName", curie=OPENCCF.curie('companyName'),
                   model_uri=OPENCCF.emissionsReport__companyName, domain=None, range=str)

slots.emissionsReport__primaryRegion = Slot(uri=OPENCCF.primaryRegion, name="emissionsReport__primaryRegion", curie=OPENCCF.curie('primaryRegion'),
                   model_uri=OPENCCF.emissionsReport__primaryRegion, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z]{2}(-[A-Za-z0-9]{1,3})?$'))

slots.emissionsReport__reportingPeriodStart = Slot(uri=OPENCCF.reportingPeriodStart, name="emissionsReport__reportingPeriodStart", curie=OPENCCF.curie('reportingPeriodStart'),
                   model_uri=OPENCCF.emissionsReport__reportingPeriodStart, domain=None, range=Union[str, XSDDate])

slots.emissionsReport__reportingPeriodEnd = Slot(uri=OPENCCF.reportingPeriodEnd, name="emissionsReport__reportingPeriodEnd", curie=OPENCCF.curie('reportingPeriodEnd'),
                   model_uri=OPENCCF.emissionsReport__reportingPeriodEnd, domain=None, range=Union[str, XSDDate])

slots.emissionsReport__totalNetEmissionsLocationBasedKgCO2e = Slot(uri=OPENCCF.totalNetEmissionsLocationBasedKgCO2e, name="emissionsReport__totalNetEmissionsLocationBasedKgCO2e", curie=OPENCCF.curie('totalNetEmissionsLocationBasedKgCO2e'),
                   model_uri=OPENCCF.emissionsReport__totalNetEmissionsLocationBasedKgCO2e, domain=None, range=float)

slots.emissionsReport__totalNetEmissionsMarketBasedKgCO2e = Slot(uri=OPENCCF.totalNetEmissionsMarketBasedKgCO2e, name="emissionsReport__totalNetEmissionsMarketBasedKgCO2e", curie=OPENCCF.curie('totalNetEmissionsMarketBasedKgCO2e'),
                   model_uri=OPENCCF.emissionsReport__totalNetEmissionsMarketBasedKgCO2e, domain=None, range=Optional[float])

slots.emissionsReport__gwpHorizon = Slot(uri=OPENCCF.gwpHorizon, name="emissionsReport__gwpHorizon", curie=OPENCCF.curie('gwpHorizon'),
                   model_uri=OPENCCF.emissionsReport__gwpHorizon, domain=None, range=Union[str, "GwpHorizonEnum"])

slots.emissionsReport__reportStatus = Slot(uri=OPENCCF.reportStatus, name="emissionsReport__reportStatus", curie=OPENCCF.curie('reportStatus'),
                   model_uri=OPENCCF.emissionsReport__reportStatus, domain=None, range=Union[str, "ReportStatusEnum"])

slots.emissionsReport__emissionsLines = Slot(uri=OPENCCF.emissionsLines, name="emissionsReport__emissionsLines", curie=OPENCCF.curie('emissionsLines'),
                   model_uri=OPENCCF.emissionsReport__emissionsLines, domain=None, range=Union[Union[dict, EmissionsLine], list[Union[dict, EmissionsLine]]])

slots.emissionsReport__sectors = Slot(uri=OPENCCF.sectors, name="emissionsReport__sectors", curie=OPENCCF.curie('sectors'),
                   model_uri=OPENCCF.emissionsReport__sectors, domain=None, range=Optional[Union[Union[dict, Sector], list[Union[dict, Sector]]]])

slots.emissionsReport__companyIdentifiers = Slot(uri=OPENCCF.companyIdentifiers, name="emissionsReport__companyIdentifiers", curie=OPENCCF.curie('companyIdentifiers'),
                   model_uri=OPENCCF.emissionsReport__companyIdentifiers, domain=None, range=Optional[Union[Union[dict, CompanyIdentifier], list[Union[dict, CompanyIdentifier]]]])

slots.emissionsReport__intensityDenominators = Slot(uri=OPENCCF.intensityDenominators, name="emissionsReport__intensityDenominators", curie=OPENCCF.curie('intensityDenominators'),
                   model_uri=OPENCCF.emissionsReport__intensityDenominators, domain=None, range=Optional[Union[Union[dict, IntensityDenominator], list[Union[dict, IntensityDenominator]]]])

slots.emissionsLine__scope = Slot(uri=OPENCCF.scope, name="emissionsLine__scope", curie=OPENCCF.curie('scope'),
                   model_uri=OPENCCF.emissionsLine__scope, domain=None, range=Union[str, "ScopeEnum"])

slots.emissionsLine__category = Slot(uri=OPENCCF.category, name="emissionsLine__category", curie=OPENCCF.curie('category'),
                   model_uri=OPENCCF.emissionsLine__category, domain=None, range=Union[str, "EmissionCategoryEnum"])

slots.emissionsLine__subcategory = Slot(uri=OPENCCF.subcategory, name="emissionsLine__subcategory", curie=OPENCCF.curie('subcategory'),
                   model_uri=OPENCCF.emissionsLine__subcategory, domain=None, range=Optional[str])

slots.emissionsLine__lineStatus = Slot(uri=OPENCCF.lineStatus, name="emissionsLine__lineStatus", curie=OPENCCF.curie('lineStatus'),
                   model_uri=OPENCCF.emissionsLine__lineStatus, domain=None, range=Union[str, "LineStatusEnum"])

slots.emissionsLine__emissionsQuantityKgCO2e = Slot(uri=OPENCCF.emissionsQuantityKgCO2e, name="emissionsLine__emissionsQuantityKgCO2e", curie=OPENCCF.curie('emissionsQuantityKgCO2e'),
                   model_uri=OPENCCF.emissionsLine__emissionsQuantityKgCO2e, domain=None, range=float)

slots.emissionsLine__emissionOrigin = Slot(uri=OPENCCF.emissionOrigin, name="emissionsLine__emissionOrigin", curie=OPENCCF.curie('emissionOrigin'),
                   model_uri=OPENCCF.emissionsLine__emissionOrigin, domain=None, range=Union[str, "EmissionOriginEnum"])

slots.emissionsLine__accountingType = Slot(uri=OPENCCF.accountingType, name="emissionsLine__accountingType", curie=OPENCCF.curie('accountingType'),
                   model_uri=OPENCCF.emissionsLine__accountingType, domain=None, range=Optional[Union[str, "AccountingTypeEnum"]])

slots.emissionsLine__region = Slot(uri=OPENCCF.region, name="emissionsLine__region", curie=OPENCCF.curie('region'),
                   model_uri=OPENCCF.emissionsLine__region, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z]{2}(-[A-Za-z0-9]{1,3})?$'))

slots.emissionsLine__companyFacilityIdentifier = Slot(uri=OPENCCF.companyFacilityIdentifier, name="emissionsLine__companyFacilityIdentifier", curie=OPENCCF.curie('companyFacilityIdentifier'),
                   model_uri=OPENCCF.emissionsLine__companyFacilityIdentifier, domain=None, range=Optional[str])

slots.emissionsLine__emissionFactor = Slot(uri=OPENCCF.emissionFactor, name="emissionsLine__emissionFactor", curie=OPENCCF.curie('emissionFactor'),
                   model_uri=OPENCCF.emissionsLine__emissionFactor, domain=None, range=Optional[Union[dict, EmissionFactor]])

slots.emissionsLine__dataQuality = Slot(uri=OPENCCF.dataQuality, name="emissionsLine__dataQuality", curie=OPENCCF.curie('dataQuality'),
                   model_uri=OPENCCF.emissionsLine__dataQuality, domain=None, range=Optional[Union[dict, DataQuality]])

slots.emissionsLine__dataQualityInformation = Slot(uri=OPENCCF.dataQualityInformation, name="emissionsLine__dataQualityInformation", curie=OPENCCF.curie('dataQualityInformation'),
                   model_uri=OPENCCF.emissionsLine__dataQualityInformation, domain=None, range=Optional[str])

slots.emissionsLine__gasBreakdown = Slot(uri=OPENCCF.gasBreakdown, name="emissionsLine__gasBreakdown", curie=OPENCCF.curie('gasBreakdown'),
                   model_uri=OPENCCF.emissionsLine__gasBreakdown, domain=None, range=Optional[Union[Union[dict, GasBreakdown], list[Union[dict, GasBreakdown]]]])

slots.emissionsLine__activityData = Slot(uri=OPENCCF.activityData, name="emissionsLine__activityData", curie=OPENCCF.curie('activityData'),
                   model_uri=OPENCCF.emissionsLine__activityData, domain=None, range=Optional[Union[dict, ActivityData]])

slots.emissionsLine__landSectorData = Slot(uri=OPENCCF.landSectorData, name="emissionsLine__landSectorData", curie=OPENCCF.curie('landSectorData'),
                   model_uri=OPENCCF.emissionsLine__landSectorData, domain=None, range=Optional[Union[dict, LandSectorData]])

slots.sector__scheme = Slot(uri=OPENCCF.scheme, name="sector__scheme", curie=OPENCCF.curie('scheme'),
                   model_uri=OPENCCF.sector__scheme, domain=None, range=Optional[str])

slots.sector__code = Slot(uri=OPENCCF.code, name="sector__code", curie=OPENCCF.curie('code'),
                   model_uri=OPENCCF.sector__code, domain=None, range=Optional[str])

slots.sector__name = Slot(uri=OPENCCF.name, name="sector__name", curie=OPENCCF.curie('name'),
                   model_uri=OPENCCF.sector__name, domain=None, range=Optional[str])

slots.companyIdentifier__scheme = Slot(uri=OPENCCF.scheme, name="companyIdentifier__scheme", curie=OPENCCF.curie('scheme'),
                   model_uri=OPENCCF.companyIdentifier__scheme, domain=None, range=Optional[str])

slots.companyIdentifier__value = Slot(uri=OPENCCF.value, name="companyIdentifier__value", curie=OPENCCF.curie('value'),
                   model_uri=OPENCCF.companyIdentifier__value, domain=None, range=Optional[str])

slots.intensityDenominator__type = Slot(uri=OPENCCF.type, name="intensityDenominator__type", curie=OPENCCF.curie('type'),
                   model_uri=OPENCCF.intensityDenominator__type, domain=None, range=Optional[str])

slots.intensityDenominator__value = Slot(uri=OPENCCF.value, name="intensityDenominator__value", curie=OPENCCF.curie('value'),
                   model_uri=OPENCCF.intensityDenominator__value, domain=None, range=Optional[float])

slots.intensityDenominator__unit = Slot(uri=OPENCCF.unit, name="intensityDenominator__unit", curie=OPENCCF.curie('unit'),
                   model_uri=OPENCCF.intensityDenominator__unit, domain=None, range=Optional[str])

slots.emissionFactor__value = Slot(uri=OPENCCF.value, name="emissionFactor__value", curie=OPENCCF.curie('value'),
                   model_uri=OPENCCF.emissionFactor__value, domain=None, range=Optional[float])

slots.emissionFactor__valueUnit = Slot(uri=OPENCCF.valueUnit, name="emissionFactor__valueUnit", curie=OPENCCF.curie('valueUnit'),
                   model_uri=OPENCCF.emissionFactor__valueUnit, domain=None, range=Optional[str])

slots.emissionFactor__source = Slot(uri=OPENCCF.source, name="emissionFactor__source", curie=OPENCCF.curie('source'),
                   model_uri=OPENCCF.emissionFactor__source, domain=None, range=str)

slots.emissionFactor__dataset = Slot(uri=OPENCCF.dataset, name="emissionFactor__dataset", curie=OPENCCF.curie('dataset'),
                   model_uri=OPENCCF.emissionFactor__dataset, domain=None, range=Optional[str])

slots.emissionFactor__dataYear = Slot(uri=OPENCCF.dataYear, name="emissionFactor__dataYear", curie=OPENCCF.curie('dataYear'),
                   model_uri=OPENCCF.emissionFactor__dataYear, domain=None, range=int)

slots.emissionFactor__ipccBasis = Slot(uri=OPENCCF.ipccBasis, name="emissionFactor__ipccBasis", curie=OPENCCF.curie('ipccBasis'),
                   model_uri=OPENCCF.emissionFactor__ipccBasis, domain=None, range=Union[str, "IpccBasisEnum"])

slots.gasBreakdown__gas = Slot(uri=OPENCCF.gas, name="gasBreakdown__gas", curie=OPENCCF.curie('gas'),
                   model_uri=OPENCCF.gasBreakdown__gas, domain=None, range=Union[str, "GasEnum"])

slots.gasBreakdown__gasQuantity = Slot(uri=OPENCCF.gasQuantity, name="gasBreakdown__gasQuantity", curie=OPENCCF.curie('gasQuantity'),
                   model_uri=OPENCCF.gasBreakdown__gasQuantity, domain=None, range=Optional[float])

slots.gasBreakdown__gasCO2eContribution = Slot(uri=OPENCCF.gasCO2eContribution, name="gasBreakdown__gasCO2eContribution", curie=OPENCCF.curie('gasCO2eContribution'),
                   model_uri=OPENCCF.gasBreakdown__gasCO2eContribution, domain=None, range=Optional[float])

slots.gasBreakdown__emissionOrigin = Slot(uri=OPENCCF.emissionOrigin, name="gasBreakdown__emissionOrigin", curie=OPENCCF.curie('emissionOrigin'),
                   model_uri=OPENCCF.gasBreakdown__emissionOrigin, domain=None, range=Optional[Union[str, "EmissionOriginEnum"]])

slots.activityData__description = Slot(uri=OPENCCF.description, name="activityData__description", curie=OPENCCF.curie('description'),
                   model_uri=OPENCCF.activityData__description, domain=None, range=Optional[str])

slots.activityData__lifecycleStage = Slot(uri=OPENCCF.lifecycleStage, name="activityData__lifecycleStage", curie=OPENCCF.curie('lifecycleStage'),
                   model_uri=OPENCCF.activityData__lifecycleStage, domain=None, range=Optional[str])

slots.activityData__value = Slot(uri=OPENCCF.value, name="activityData__value", curie=OPENCCF.curie('value'),
                   model_uri=OPENCCF.activityData__value, domain=None, range=Optional[float])

slots.activityData__unit = Slot(uri=OPENCCF.unit, name="activityData__unit", curie=OPENCCF.curie('unit'),
                   model_uri=OPENCCF.activityData__unit, domain=None, range=Optional[str])

slots.dataQuality__technologicalRepresentativeness = Slot(uri=OPENCCF.technologicalRepresentativeness, name="dataQuality__technologicalRepresentativeness", curie=OPENCCF.curie('technologicalRepresentativeness'),
                   model_uri=OPENCCF.dataQuality__technologicalRepresentativeness, domain=None, range=Optional[Union[str, "DataQualityRatingEnum"]])

slots.dataQuality__temporalRepresentativeness = Slot(uri=OPENCCF.temporalRepresentativeness, name="dataQuality__temporalRepresentativeness", curie=OPENCCF.curie('temporalRepresentativeness'),
                   model_uri=OPENCCF.dataQuality__temporalRepresentativeness, domain=None, range=Optional[Union[str, "DataQualityRatingEnum"]])

slots.dataQuality__geographicalRepresentativeness = Slot(uri=OPENCCF.geographicalRepresentativeness, name="dataQuality__geographicalRepresentativeness", curie=OPENCCF.curie('geographicalRepresentativeness'),
                   model_uri=OPENCCF.dataQuality__geographicalRepresentativeness, domain=None, range=Optional[Union[str, "DataQualityRatingEnum"]])

slots.dataQuality__completeness = Slot(uri=OPENCCF.completeness, name="dataQuality__completeness", curie=OPENCCF.curie('completeness'),
                   model_uri=OPENCCF.dataQuality__completeness, domain=None, range=Optional[Union[str, "DataQualityRatingEnum"]])

slots.dataQuality__reliability = Slot(uri=OPENCCF.reliability, name="dataQuality__reliability", curie=OPENCCF.curie('reliability'),
                   model_uri=OPENCCF.dataQuality__reliability, domain=None, range=Optional[Union[str, "DataQualityRatingEnum"]])

slots.landSectorData__boundary = Slot(uri=OPENCCF.boundary, name="landSectorData__boundary", curie=OPENCCF.curie('boundary'),
                   model_uri=OPENCCF.landSectorData__boundary, domain=None, range=Optional[str])

slots.landSectorData__storageDuration = Slot(uri=OPENCCF.storageDuration, name="landSectorData__storageDuration", curie=OPENCCF.curie('storageDuration'),
                   model_uri=OPENCCF.landSectorData__storageDuration, domain=None, range=Optional[str])

slots.landSectorData__monitoringApproach = Slot(uri=OPENCCF.monitoringApproach, name="landSectorData__monitoringApproach", curie=OPENCCF.curie('monitoringApproach'),
                   model_uri=OPENCCF.landSectorData__monitoringApproach, domain=None, range=Optional[str])
