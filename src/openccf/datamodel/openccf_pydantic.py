from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_curi_maps': ['semweb_context'],
     'default_prefix': 'openccf',
     'default_range': 'string',
     'description': 'An open, interoperable data model for exchanging GHG '
                    'Protocol-aligned corporate carbon footprints between systems. '
                    'Released under CC0-1.0.',
     'id': 'https://w3id.org/openccf',
     'id_prefixes': ['openccf'],
     'imports': ['linkml:types'],
     'license': 'CC0-1.0',
     'name': 'openccf',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'openccf': {'prefix_prefix': 'openccf',
                              'prefix_reference': 'https://w3id.org/openccf/'}},
     'see_also': ['https://openccf.org'],
     'source_file': 'src/openccf/schema/openccf.yaml',
     'title': 'OpenCCF - Open Corporate Carbon Footprint Data Model'} )

class ScopeEnum(str, Enum):
    SCOPE_1 = "SCOPE_1"
    """
    Direct emissions from owned or controlled sources.
    """
    SCOPE_2 = "SCOPE_2"
    """
    Indirect emissions from purchased energy.
    """
    SCOPE_3 = "SCOPE_3"
    """
    All other indirect value-chain emissions.
    """


class EmissionCategoryEnum(str, Enum):
    """
    Source classification. Valid values are scope-dependent; the scope-to-category validity constraint is enforced by rules on EmissionsLine.
    """
    STATIONARY_COMBUSTION = "STATIONARY_COMBUSTION"
    """
    Scope 1: Stationary combustion.
    """
    MOBILE_COMBUSTION = "MOBILE_COMBUSTION"
    """
    Scope 1: Mobile combustion.
    """
    PROCESS_EMISSIONS = "PROCESS_EMISSIONS"
    """
    Scope 1: Process emissions from physical or chemical processes.
    """
    FUGITIVE = "FUGITIVE"
    """
    Scope 1: Fugitive emissions.
    """
    ELECTRICITY_MARKET_BASED = "ELECTRICITY_MARKET_BASED"
    """
    Scope 2: Purchased electricity (market-based method).
    """
    ELECTRICITY_LOCATION_BASED = "ELECTRICITY_LOCATION_BASED"
    """
    Scope 2: Purchased electricity (location-based method).
    """
    HEAT_STEAM_COOLING = "HEAT_STEAM_COOLING"
    """
    Scope 2: Purchased heat, steam and cooling.
    """
    S3_01_PURCHASED_GOODS_SERVICES = "S3_01_PURCHASED_GOODS_SERVICES"
    """
    Category 1: Purchased goods and services.
    """
    S3_02_CAPITAL_GOODS = "S3_02_CAPITAL_GOODS"
    """
    Category 2: Capital goods.
    """
    S3_03_FUEL_ENERGY_RELATED = "S3_03_FUEL_ENERGY_RELATED"
    """
    Category 3: Fuel- and energy-related activities (not included in Scope 1 or Scope 2).
    """
    S3_04_UPSTREAM_TRANSPORT = "S3_04_UPSTREAM_TRANSPORT"
    """
    Category 4: Upstream transportation and distribution.
    """
    S3_05_WASTE_IN_OPERATIONS = "S3_05_WASTE_IN_OPERATIONS"
    """
    Category 5: Waste generated in operations.
    """
    S3_06_BUSINESS_TRAVEL = "S3_06_BUSINESS_TRAVEL"
    """
    Category 6: Business travel.
    """
    S3_07_EMPLOYEE_COMMUTING = "S3_07_EMPLOYEE_COMMUTING"
    """
    Category 7: Employee commuting.
    """
    S3_08_UPSTREAM_LEASED_ASSETS = "S3_08_UPSTREAM_LEASED_ASSETS"
    """
    Category 8: Upstream leased assets.
    """
    S3_09_DOWNSTREAM_TRANSPORT = "S3_09_DOWNSTREAM_TRANSPORT"
    """
    Category 9: Downstream transportation and distribution.
    """
    S3_10_PROCESSING_SOLD_PRODUCTS = "S3_10_PROCESSING_SOLD_PRODUCTS"
    """
    Category 10: Processing of sold products.
    """
    S3_11_USE_OF_SOLD_PRODUCTS = "S3_11_USE_OF_SOLD_PRODUCTS"
    """
    Category 11: Use of sold products.
    """
    S3_12_EOL_SOLD_PRODUCTS = "S3_12_EOL_SOLD_PRODUCTS"
    """
    Category 12: End-of-life treatment of sold products.
    """
    S3_13_DOWNSTREAM_LEASED_ASSETS = "S3_13_DOWNSTREAM_LEASED_ASSETS"
    """
    Category 13: Downstream leased assets.
    """
    S3_14_FRANCHISES = "S3_14_FRANCHISES"
    """
    Category 14: Franchises.
    """
    S3_15_INVESTMENTS = "S3_15_INVESTMENTS"
    """
    Category 15: Investments.
    """
    NOT_SPECIFIED = "NOT_SPECIFIED"
    """
    Category not specified or not disclosed by the source.
    """


class LineStatusEnum(str, Enum):
    """
    Completeness of this line. Assurance status is recorded at report level.
    """
    COMPLETE = "COMPLETE"
    """
    Fully measured or calculated for the reporting period.
    """
    INCOMPLETE = "INCOMPLETE"
    """
    Partially measured; known to under-represent the total for this line.
    """
    EXCLUDED = "EXCLUDED"
    """
    Explicitly excluded from the report.
    """


class ReportStatusEnum(str, Enum):
    INCOMPLETE = "INCOMPLETE"
    """
    Not for utilisation as a full company report.
    """
    SELF_COMPLETED = "SELF_COMPLETED"
    THIRD_PARTY_COMPLETED = "THIRD_PARTY_COMPLETED"
    THIRD_PARTY_AUDITED = "THIRD_PARTY_AUDITED"


class EmissionOriginEnum(str, Enum):
    FOSSIL = "FOSSIL"
    BIOGENIC = "BIOGENIC"
    MIXED = "MIXED"
    """
    Origin cannot be disaggregated in the source data.
    """
    NOT_SPECIFIED = "NOT_SPECIFIED"
    """
    Underlying data does not distinguish origin.
    """
    NOT_APPLICABLE = "NOT_APPLICABLE"
    """
    Origin concept not relevant for this gas.
    """


class AccountingTypeEnum(str, Enum):
    EMISSION = "EMISSION"
    REMOVAL = "REMOVAL"
    GROSS_CO2_FLUX = "GROSS_CO2_FLUX"
    """
    Additional disclosure.
    """
    REVERSAL = "REVERSAL"
    OTHER_LAND_SECTOR_DISCLOSURE = "OTHER_LAND_SECTOR_DISCLOSURE"
    """
    Reserved for future expansion.
    """


class GwpHorizonEnum(str, Enum):
    GWP20 = "GWP20"
    GWP100 = "GWP100"
    GWP500 = "GWP500"


class IpccBasisEnum(str, Enum):
    AR4 = "AR4"
    AR5 = "AR5"
    AR6 = "AR6"
    NOT_SPECIFIED = "NOT_SPECIFIED"


class GasEnum(str, Enum):
    CO2 = "CO2"
    CH4 = "CH4"
    N2O = "N2O"
    HFC = "HFC"
    """
    With subtype to be specified.
    """
    PFC = "PFC"
    SF6 = "SF6"
    NF3 = "NF3"
    OTHER = "OTHER"
    """
    Specified separately.
    """


class DataQualityRatingEnum(str, Enum):
    """
    GHG Protocol data quality indicator rating (Poor to Very good).
    """
    VERY_GOOD = "VERY_GOOD"
    GOOD = "GOOD"
    FAIR = "FAIR"
    POOR = "POOR"



class EmissionsReport(ConfiguredBaseModel):
    """
    A company's greenhouse gas footprint for a defined reporting period. Acts as the container for one or more Emissions Lines. The location-based net total is always present; the market-based total is present only where the report contains market-based electricity lines. The derivation of each total from its lines is a semantic constraint, verified by the conformance tests rather than by schema validation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf', 'tree_root': True})

    reportID: str = Field(default=..., description="""Unique identifier for this report.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport', 'EmissionsLine']} })
    companyName: str = Field(default=..., description="""Legal or trading name of the reporting entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    primaryRegion: str = Field(default=..., description="""Location of the reporting entity as a UN/LOCODE (minimum country; state/region extension supported).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    reportingPeriodStart: date = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    reportingPeriodEnd: date = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    totalNetEmissionsLocationBasedKgCO2e: float = Field(default=..., description="""Net aggregate for the reporting period on the location-based Scope 2 method: sum(EMISSION) - sum(REMOVAL) + sum(REVERSAL) over all emissionsLines, excluding GROSS_CO2_FLUX and OTHER_LAND_SECTOR_DISCLOSURE lines, and excluding ELECTRICITY_MARKET_BASED lines. Always present: location-based is the baseline method, and for reports with no market-based electricity this is simply the report total.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    totalNetEmissionsMarketBasedKgCO2e: Optional[float] = Field(default=None, description="""Net aggregate for the reporting period on the market-based Scope 2 method: as above, excluding ELECTRICITY_LOCATION_BASED lines. Present only where the report contains market-based electricity lines. Omitted (left blank, never zero) otherwise.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    gwpHorizon: GwpHorizonEnum = Field(default=..., description="""GWP time horizon applied across the whole report. Report-level to enforce consistency; IPCC AR basis is recorded per line.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    reportStatus: ReportStatusEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    emissionsLines: list[EmissionsLine] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    sectors: Optional[list[Sector]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    companyIdentifiers: Optional[list[CompanyIdentifier]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })
    intensityDenominators: Optional[list[IntensityDenominator]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport']} })


class EmissionsLine(ConfiguredBaseModel):
    """
    A single quantified source or category of emissions within a report. Lines are flat; totals and subtotals are derived by grouping, not nesting.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf',
         'rules': [{'description': 'Scope 1 lines must use a Scope 1 category, or '
                                   'NOT_SPECIFIED.',
                    'postconditions': {'slot_conditions': {'category': {'any_of': [{'equals_string': 'STATIONARY_COMBUSTION'},
                                                                                   {'equals_string': 'MOBILE_COMBUSTION'},
                                                                                   {'equals_string': 'PROCESS_EMISSIONS'},
                                                                                   {'equals_string': 'FUGITIVE'},
                                                                                   {'equals_string': 'NOT_SPECIFIED'}],
                                                                        'name': 'category'}}},
                    'preconditions': {'slot_conditions': {'scope': {'equals_string': 'SCOPE_1',
                                                                    'name': 'scope'}}}},
                   {'description': 'Scope 2 lines must use a Scope 2 category, or '
                                   'NOT_SPECIFIED.',
                    'postconditions': {'slot_conditions': {'category': {'any_of': [{'equals_string': 'ELECTRICITY_MARKET_BASED'},
                                                                                   {'equals_string': 'ELECTRICITY_LOCATION_BASED'},
                                                                                   {'equals_string': 'HEAT_STEAM_COOLING'},
                                                                                   {'equals_string': 'NOT_SPECIFIED'}],
                                                                        'name': 'category'}}},
                    'preconditions': {'slot_conditions': {'scope': {'equals_string': 'SCOPE_2',
                                                                    'name': 'scope'}}}},
                   {'description': 'Scope 3 lines must use a Scope 3 category, or '
                                   'NOT_SPECIFIED.',
                    'postconditions': {'slot_conditions': {'category': {'any_of': [{'equals_string': 'S3_01_PURCHASED_GOODS_SERVICES'},
                                                                                   {'equals_string': 'S3_02_CAPITAL_GOODS'},
                                                                                   {'equals_string': 'S3_03_FUEL_ENERGY_RELATED'},
                                                                                   {'equals_string': 'S3_04_UPSTREAM_TRANSPORT'},
                                                                                   {'equals_string': 'S3_05_WASTE_IN_OPERATIONS'},
                                                                                   {'equals_string': 'S3_06_BUSINESS_TRAVEL'},
                                                                                   {'equals_string': 'S3_07_EMPLOYEE_COMMUTING'},
                                                                                   {'equals_string': 'S3_08_UPSTREAM_LEASED_ASSETS'},
                                                                                   {'equals_string': 'S3_09_DOWNSTREAM_TRANSPORT'},
                                                                                   {'equals_string': 'S3_10_PROCESSING_SOLD_PRODUCTS'},
                                                                                   {'equals_string': 'S3_11_USE_OF_SOLD_PRODUCTS'},
                                                                                   {'equals_string': 'S3_12_EOL_SOLD_PRODUCTS'},
                                                                                   {'equals_string': 'S3_13_DOWNSTREAM_LEASED_ASSETS'},
                                                                                   {'equals_string': 'S3_14_FRANCHISES'},
                                                                                   {'equals_string': 'S3_15_INVESTMENTS'},
                                                                                   {'equals_string': 'NOT_SPECIFIED'}],
                                                                        'name': 'category'}}},
                    'preconditions': {'slot_conditions': {'scope': {'equals_string': 'SCOPE_3',
                                                                    'name': 'scope'}}}}]})

    reportID: Optional[str] = Field(default=None, description="""Optional back-reference to the owning report, for cases where a line is exchanged on its own rather than nested inside a report.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsReport', 'EmissionsLine']} })
    scope: ScopeEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    category: EmissionCategoryEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    subcategory: Optional[str] = Field(default=None, description="""Optional free-text subcategorisation of the line within its category, at the sender's discretion (e.g. \"Food and beverages\" or \"HGV fleet\"). There is no controlled vocabulary; values are descriptive and not intended to be machine-comparable. Useful for breaking a category into meaningful detail  without changing its GHG Protocol classification. It is intended as a grouping label  a sender or receiver can use to aggregate or subtotal lines (e.g. summing all  \"HGV fleet\" lines). It describes the kind of line, not the specific activity used  to calculate it (see ActivityData).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    lineStatus: LineStatusEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    emissionsQuantityKgCO2e: float = Field(default=..., description="""Total CO2-equivalent for this line, expressed as a non-negative magnitude. Direction (whether the line adds to or subtracts from the net) is determined by accountingType, not by the sign of this value - consistent with GHG Protocol gross reporting, under which gross emissions and gross removals are reported separately and not netted within a category.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    emissionOrigin: EmissionOriginEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine', 'GasBreakdown']} })
    accountingType: Optional[AccountingTypeEnum] = Field(default=AccountingTypeEnum.EMISSION, description="""Inventory treatment of this line, and its contribution to the report net total: EMISSION adds, REMOVAL subtracts, REVERSAL adds; GROSS_CO2_FLUX and OTHER_LAND_SECTOR_DISCLOSURE are disclosure-only and excluded from the net. Defaults to EMISSION where omitted.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine'], 'ifabsent': 'EMISSION'} })
    region: str = Field(default=..., description="""Country or region where emissions physically occurred, as a UN/LOCODE (minimum country; state/region extension supported).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    companyFacilityIdentifier: Optional[str] = Field(default=None, description="""Facility where emissions physically occurred (optional).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    emissionFactor: Optional[EmissionFactor] = Field(default=None, description="""Metadata on the emission factor used for this line. Optional as many exchanged figures (e.g. republished totals, or directly measured emissions) have no disclosed factor. Where provided, source and ipccBasis are required.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    dataQuality: Optional[DataQuality] = Field(default=None, description="""GHG Protocol data quality assessment for this line, spanning both the activity data and the emission factor used. Optional; most relevant where secondary, proxy or estimated inputs are applied. Use dataQualityInformation for any additional context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    dataQualityInformation: Optional[str] = Field(default=None, description="""Optional free-text data quality context not captured by the indicators above (e.g. calculation method, provenance, known limitations). Sender's discretion; not machine-comparable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    gasBreakdown: Optional[list[GasBreakdown]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    activityData: Optional[ActivityData] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })
    landSectorData: Optional[LandSectorData] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine']} })


class Sector(ConfiguredBaseModel):
    """
    Standardised sector classification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf'})

    scheme: Optional[str] = Field(default=None, description="""Classification scheme (e.g. NACE, SIC, GHG Protocol sector).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sector', 'CompanyIdentifier']} })
    code: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Sector']} })
    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Sector']} })


class CompanyIdentifier(ConfiguredBaseModel):
    """
    Standardised company identifier.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf'})

    scheme: Optional[str] = Field(default=None, description="""Identifier scheme (e.g. LEI, DUNS).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sector', 'CompanyIdentifier']} })
    value: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompanyIdentifier', 'IntensityDenominator', 'ActivityData']} })


class IntensityDenominator(ConfiguredBaseModel):
    """
    A denominator for calculating intensity values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf'})

    type: Optional[str] = Field(default=None, description="""e.g. full-time employees, revenue, facility area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['IntensityDenominator']} })
    value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompanyIdentifier', 'IntensityDenominator', 'ActivityData']} })
    unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['IntensityDenominator', 'ActivityData']} })


class EmissionFactor(ConfiguredBaseModel):
    """
    Metadata describing the emission factor applied to a line.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf'})

    source: str = Field(default=..., description="""Authority for the emission factor used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionFactor']} })
    dataset: Optional[str] = Field(default=None, description="""Specific dataset used (optional).""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionFactor']} })
    dataYear: int = Field(default=..., description="""Year the emission factor was issued.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionFactor']} })
    ipccBasis: IpccBasisEnum = Field(default=..., description="""IPCC Assessment Report basis for the GWP values used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionFactor']} })


class GasBreakdown(ConfiguredBaseModel):
    """
    Constituent gas-level resolution of a line's emissions. Where a breakdown is provided it must be complete: the sum of gasCO2eContribution across entries equals the line's emissionsQuantityKgCO2e, within a small rounding tolerance (relative 0.1% with an absolute floor for near-zero lines). Any portion not attributable to a named gas is carried as an explicit OTHER entry rather than left implicit.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf'})

    gas: GasEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['GasBreakdown']} })
    gasQuantity: Optional[float] = Field(default=None, description="""Quantity of the gas in its native unit (e.g. tonnes CH4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GasBreakdown']} })
    gasCO2eContribution: Optional[float] = Field(default=None, description="""Portion of the line's emissionsQuantityKgCO2e attributable to this gas, as a non-negative magnitude. Where a breakdown is present, contributions sum to the line total (see class-level note).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['GasBreakdown']} })
    emissionOrigin: Optional[EmissionOriginEnum] = Field(default=None, description="""Origin of this gas's emissions. Where a gas breakdown is provided, gas-level origin takes precedence over the line-level emissionOrigin.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EmissionsLine', 'GasBreakdown']} })


class ActivityData(ConfiguredBaseModel):
    """
    Optional activity information underlying the emissions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf'})

    description: Optional[str] = Field(default=None, description="""Free-text description of the specific activity quantity used to calculate this line's emissions (e.g. \"diesel purchased for site generator\"). Describes this particular measurement for provenance or recalculation, not a grouping label - use subcategory on the line for aggregation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ActivityData']} })
    lifecycleStage: Optional[str] = Field(default=None, description="""Where applicable (e.g. upstream, use phase, end-of-life).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ActivityData']} })
    value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CompanyIdentifier', 'IntensityDenominator', 'ActivityData']} })
    unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['IntensityDenominator', 'ActivityData']} })


class DataQuality(ConfiguredBaseModel):
    """
    Data quality of an emissions line, aligned to the GHG Protocol Scope 3 Standard's five data quality indicators. The assessment reflects both the activity data and the emission factor used: the representativeness axes describe how well the inputs match this line's technology, period and geography, while completeness and reliability describe the underlying data and its sources. Each axis is rated Poor to Very good. (A GHG Protocol revision toward a data-specificity framework is in progress; this structure will track it in a future version.)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf'})

    technologicalRepresentativeness: Optional[DataQualityRatingEnum] = Field(default=None, description="""Degree to which the emission estimation reflects the actual technology(ies) used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataQuality']} })
    temporalRepresentativeness: Optional[DataQualityRatingEnum] = Field(default=None, description="""Degree to which the emission estimation reflects the actual time period.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataQuality']} })
    geographicalRepresentativeness: Optional[DataQualityRatingEnum] = Field(default=None, description="""Degree to which the emission estimation reflects the actual geography.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataQuality']} })
    completeness: Optional[DataQualityRatingEnum] = Field(default=None, description="""Degree to which the emission estimation is statistically representative and complete.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataQuality']} })
    reliability: Optional[DataQualityRatingEnum] = Field(default=None, description="""Reliability of the emission estimation sources and measurement or estimation methods.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataQuality']} })


class LandSectorData(ConfiguredBaseModel):
    """
    Optional land sector and removals metadata.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/openccf'})

    boundary: Optional[str] = Field(default=None, description="""Land boundary / traceability level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LandSectorData']} })
    storageDuration: Optional[str] = Field(default=None, description="""Expected storage duration / permanence category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LandSectorData']} })
    monitoringApproach: Optional[str] = Field(default=None, description="""Monitoring approach and reversal treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LandSectorData']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
EmissionsReport.model_rebuild()
EmissionsLine.model_rebuild()
Sector.model_rebuild()
CompanyIdentifier.model_rebuild()
IntensityDenominator.model_rebuild()
EmissionFactor.model_rebuild()
GasBreakdown.model_rebuild()
ActivityData.model_rebuild()
DataQuality.model_rebuild()
LandSectorData.model_rebuild()
