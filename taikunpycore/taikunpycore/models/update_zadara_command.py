# coding: utf-8

"""
    Taikun - WebApi

    This Api will be responsible for overall data distribution and authorization.

    The version of the OpenAPI document: v1
    Contact: noreply@taikun.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UpdateZadaraCommand(BaseModel):
    """
    UpdateZadaraCommand
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    zadara_secret_access_key: Optional[StrictStr] = Field(default=None, alias="zadaraSecretAccessKey")
    zadara_access_key_id: Optional[StrictStr] = Field(default=None, alias="zadaraAccessKeyId")
    __properties: ClassVar[List[str]] = ["id", "name", "zadaraSecretAccessKey", "zadaraAccessKeyId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UpdateZadaraCommand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if zadara_secret_access_key (nullable) is None
        # and model_fields_set contains the field
        if self.zadara_secret_access_key is None and "zadara_secret_access_key" in self.model_fields_set:
            _dict['zadaraSecretAccessKey'] = None

        # set to None if zadara_access_key_id (nullable) is None
        # and model_fields_set contains the field
        if self.zadara_access_key_id is None and "zadara_access_key_id" in self.model_fields_set:
            _dict['zadaraAccessKeyId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateZadaraCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "zadaraSecretAccessKey": obj.get("zadaraSecretAccessKey"),
            "zadaraAccessKeyId": obj.get("zadaraAccessKeyId")
        })
        return _obj


