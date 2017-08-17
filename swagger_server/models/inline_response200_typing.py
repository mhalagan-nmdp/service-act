# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.inline_response200_related_gfe import InlineResponse200RelatedGfe
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse200Typing(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, hla: str=None, related_gfe: List[InlineResponse200RelatedGfe]=None, act_version: str=None, gfe_version: str=None, gfedb_version: str=None):
        """
        InlineResponse200Typing - a model defined in Swagger

        :param hla: The hla of this InlineResponse200Typing.
        :type hla: str
        :param related_gfe: The related_gfe of this InlineResponse200Typing.
        :type related_gfe: List[InlineResponse200RelatedGfe]
        :param act_version: The act_version of this InlineResponse200Typing.
        :type act_version: str
        :param gfe_version: The gfe_version of this InlineResponse200Typing.
        :type gfe_version: str
        :param gfedb_version: The gfedb_version of this InlineResponse200Typing.
        :type gfedb_version: str
        """
        self.swagger_types = {
            'hla': str,
            'related_gfe': List[InlineResponse200RelatedGfe],
            'act_version': str,
            'gfe_version': str,
            'gfedb_version': str
        }

        self.attribute_map = {
            'hla': 'hla',
            'related_gfe': 'related_gfe',
            'act_version': 'act_version',
            'gfe_version': 'gfe_version',
            'gfedb_version': 'gfedb_version'
        }

        self._hla = hla
        self._related_gfe = related_gfe
        self._act_version = act_version
        self._gfe_version = gfe_version
        self._gfedb_version = gfedb_version

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200Typing':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_typing of this InlineResponse200Typing.
        :rtype: InlineResponse200Typing
        """
        return deserialize_model(dikt, cls)

    @property
    def hla(self) -> str:
        """
        Gets the hla of this InlineResponse200Typing.

        :return: The hla of this InlineResponse200Typing.
        :rtype: str
        """
        return self._hla

    @hla.setter
    def hla(self, hla: str):
        """
        Sets the hla of this InlineResponse200Typing.

        :param hla: The hla of this InlineResponse200Typing.
        :type hla: str
        """

        self._hla = hla

    @property
    def related_gfe(self) -> List[InlineResponse200RelatedGfe]:
        """
        Gets the related_gfe of this InlineResponse200Typing.

        :return: The related_gfe of this InlineResponse200Typing.
        :rtype: List[InlineResponse200RelatedGfe]
        """
        return self._related_gfe

    @related_gfe.setter
    def related_gfe(self, related_gfe: List[InlineResponse200RelatedGfe]):
        """
        Sets the related_gfe of this InlineResponse200Typing.

        :param related_gfe: The related_gfe of this InlineResponse200Typing.
        :type related_gfe: List[InlineResponse200RelatedGfe]
        """

        self._related_gfe = related_gfe

    @property
    def act_version(self) -> str:
        """
        Gets the act_version of this InlineResponse200Typing.

        :return: The act_version of this InlineResponse200Typing.
        :rtype: str
        """
        return self._act_version

    @act_version.setter
    def act_version(self, act_version: str):
        """
        Sets the act_version of this InlineResponse200Typing.

        :param act_version: The act_version of this InlineResponse200Typing.
        :type act_version: str
        """

        self._act_version = act_version

    @property
    def gfe_version(self) -> str:
        """
        Gets the gfe_version of this InlineResponse200Typing.

        :return: The gfe_version of this InlineResponse200Typing.
        :rtype: str
        """
        return self._gfe_version

    @gfe_version.setter
    def gfe_version(self, gfe_version: str):
        """
        Sets the gfe_version of this InlineResponse200Typing.

        :param gfe_version: The gfe_version of this InlineResponse200Typing.
        :type gfe_version: str
        """

        self._gfe_version = gfe_version

    @property
    def gfedb_version(self) -> str:
        """
        Gets the gfedb_version of this InlineResponse200Typing.

        :return: The gfedb_version of this InlineResponse200Typing.
        :rtype: str
        """
        return self._gfedb_version

    @gfedb_version.setter
    def gfedb_version(self, gfedb_version: str):
        """
        Sets the gfedb_version of this InlineResponse200Typing.

        :param gfedb_version: The gfedb_version of this InlineResponse200Typing.
        :type gfedb_version: str
        """

        self._gfedb_version = gfedb_version

