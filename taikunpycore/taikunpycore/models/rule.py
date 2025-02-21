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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from taikunpycore.models.alert import Alert
from taikunpycore.models.annotations import Annotations
from taikunpycore.models.rule_labels import RuleLabels
from typing import Optional, Set
from typing_extensions import Self

class Rule(BaseModel):
    """
    Rule
    """ # noqa: E501
    state: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    query: Optional[StrictStr] = None
    duration: Optional[StrictInt] = None
    labels: Optional[RuleLabels] = None
    annotations: Optional[Annotations] = None
    alerts: Optional[List[Alert]] = None
    health: Optional[StrictStr] = None
    evaluation_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="evaluationTime")
    last_evaluation: Optional[datetime] = Field(default=None, alias="lastEvaluation")
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["state", "name", "query", "duration", "labels", "annotations", "alerts", "health", "evaluationTime", "lastEvaluation", "type"]

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
        """Create an instance of Rule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict['labels'] = self.labels.to_dict()
        # override the default output from pydantic by calling `to_dict()` of annotations
        if self.annotations:
            _dict['annotations'] = self.annotations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in alerts (list)
        _items = []
        if self.alerts:
            for _item_alerts in self.alerts:
                if _item_alerts:
                    _items.append(_item_alerts.to_dict())
            _dict['alerts'] = _items
        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if query (nullable) is None
        # and model_fields_set contains the field
        if self.query is None and "query" in self.model_fields_set:
            _dict['query'] = None

        # set to None if alerts (nullable) is None
        # and model_fields_set contains the field
        if self.alerts is None and "alerts" in self.model_fields_set:
            _dict['alerts'] = None

        # set to None if health (nullable) is None
        # and model_fields_set contains the field
        if self.health is None and "health" in self.model_fields_set:
            _dict['health'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Rule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "state": obj.get("state"),
            "name": obj.get("name"),
            "query": obj.get("query"),
            "duration": obj.get("duration"),
            "labels": RuleLabels.from_dict(obj["labels"]) if obj.get("labels") is not None else None,
            "annotations": Annotations.from_dict(obj["annotations"]) if obj.get("annotations") is not None else None,
            "alerts": [Alert.from_dict(_item) for _item in obj["alerts"]] if obj.get("alerts") is not None else None,
            "health": obj.get("health"),
            "evaluationTime": obj.get("evaluationTime"),
            "lastEvaluation": obj.get("lastEvaluation"),
            "type": obj.get("type")
        })
        return _obj


