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
import json
from enum import Enum
from typing_extensions import Self


class SlackType(str, Enum):
    """
    SlackType
    """

    """
    allowed enum values
    """
    ALERT = 'Alert'
    GENERAL = 'General'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SlackType from a JSON string"""
        return cls(json.loads(json_str))


