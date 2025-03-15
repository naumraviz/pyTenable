from typing import Any, Optional
from enum import Enum
from pydantic import BaseModel


class AssetClass(Enum):
    IAC = "IAC"
    STORAGE = "STORAGE"
    DEVICE = "DEVICE"
    APPLICATION = "APPLICATION"
    GENERAL = "GENERAL"
    CONTAINER = "CONTAINER"
    ACCOUNT = "ACCOUNT"
    RESOURCE = "RESOURCE"
    IDENTITY = "IDENTITY"
    ROLE = "ROLE"
    GROUP = "GROUP"
    UNKNOWN = "UNKNOWN"


class Operators(Enum):
    EQUAL = "="
    NOT_EQUAL = "!="
    CONTAINS = "contains"
    NOT_CONTAINS = "not contains"
    EXISTS = "exists"
    NOT_EXISTS = "not exists"
    LOWER_THAN = "<"
    LOWER_OR_EQUALS = "<="
    GREATER_THAN = ">"
    GREATER_OR_EQUALS = ">="
    OLDER_THAN = "older than"
    NEWER_THAN = "newer than"
    WITHIN_LAST = "within last"
    BETWEEN = "between"


class ControlType(Enum):
    STRING = "STRING"
    NUMBER = "NUMBER"
    DATE = "DATE"
    BOOLEAN = "BOOLEAN"
    ARRAY = "ARRAY"
    OBJECT = "OBJECT"


class SelectionControl(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None
    deprecated: Optional[bool] = None
    third_party: Optional[bool] = None


class Control(BaseModel):
    type: ControlType
    multiple_allowed: bool
    regex: Optional[dict[str, Any]] = None
    selection: Optional[list[SelectionControl]] = None


class AssetField(BaseModel):
    key: str
    readable_name: str
    control: Control
    operators: list[Operators]
    sortable: bool
    filterable: bool
    weight: float
    object_types: list[AssetClass]
    description: str


class AssetProperties(BaseModel):
    properties: list[AssetField]


class Asset(BaseModel):
    id: str
    asset_class: AssetClass
    name: str
    aes: int
    acr: int
    additional_properties: dict[str, Any]  # Supports arbitrary key-value pairs


class Assets(BaseModel):
    values: list[Asset]
    total_count: int
