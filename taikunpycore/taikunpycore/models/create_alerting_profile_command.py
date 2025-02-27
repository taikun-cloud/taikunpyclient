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
from taikunpycore.models.alerting_email_dto import AlertingEmailDto
from taikunpycore.models.alerting_integration_dto import AlertingIntegrationDto
from taikunpycore.models.alerting_reminder import AlertingReminder
from taikunpycore.models.alerting_webhook_dto import AlertingWebhookDto
from typing import Optional, Set
from typing_extensions import Self

class CreateAlertingProfileCommand(BaseModel):
    """
    CreateAlertingProfileCommand
    """ # noqa: E501
    name: Optional[StrictStr] = None
    slack_configuration_id: Optional[StrictInt] = Field(default=None, alias="slackConfigurationId")
    organization_id: Optional[StrictInt] = Field(default=None, alias="organizationId")
    emails: Optional[List[AlertingEmailDto]] = None
    webhooks: Optional[List[AlertingWebhookDto]] = None
    alerting_integrations: Optional[List[AlertingIntegrationDto]] = Field(default=None, alias="alertingIntegrations")
    reminder: Optional[AlertingReminder] = None
    __properties: ClassVar[List[str]] = ["name", "slackConfigurationId", "organizationId", "emails", "webhooks", "alertingIntegrations", "reminder"]

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
        """Create an instance of CreateAlertingProfileCommand from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in emails (list)
        _items = []
        if self.emails:
            for _item_emails in self.emails:
                if _item_emails:
                    _items.append(_item_emails.to_dict())
            _dict['emails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in webhooks (list)
        _items = []
        if self.webhooks:
            for _item_webhooks in self.webhooks:
                if _item_webhooks:
                    _items.append(_item_webhooks.to_dict())
            _dict['webhooks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in alerting_integrations (list)
        _items = []
        if self.alerting_integrations:
            for _item_alerting_integrations in self.alerting_integrations:
                if _item_alerting_integrations:
                    _items.append(_item_alerting_integrations.to_dict())
            _dict['alertingIntegrations'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if slack_configuration_id (nullable) is None
        # and model_fields_set contains the field
        if self.slack_configuration_id is None and "slack_configuration_id" in self.model_fields_set:
            _dict['slackConfigurationId'] = None

        # set to None if organization_id (nullable) is None
        # and model_fields_set contains the field
        if self.organization_id is None and "organization_id" in self.model_fields_set:
            _dict['organizationId'] = None

        # set to None if emails (nullable) is None
        # and model_fields_set contains the field
        if self.emails is None and "emails" in self.model_fields_set:
            _dict['emails'] = None

        # set to None if webhooks (nullable) is None
        # and model_fields_set contains the field
        if self.webhooks is None and "webhooks" in self.model_fields_set:
            _dict['webhooks'] = None

        # set to None if alerting_integrations (nullable) is None
        # and model_fields_set contains the field
        if self.alerting_integrations is None and "alerting_integrations" in self.model_fields_set:
            _dict['alertingIntegrations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateAlertingProfileCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "slackConfigurationId": obj.get("slackConfigurationId"),
            "organizationId": obj.get("organizationId"),
            "emails": [AlertingEmailDto.from_dict(_item) for _item in obj["emails"]] if obj.get("emails") is not None else None,
            "webhooks": [AlertingWebhookDto.from_dict(_item) for _item in obj["webhooks"]] if obj.get("webhooks") is not None else None,
            "alertingIntegrations": [AlertingIntegrationDto.from_dict(_item) for _item in obj["alertingIntegrations"]] if obj.get("alertingIntegrations") is not None else None,
            "reminder": obj.get("reminder")
        })
        return _obj


