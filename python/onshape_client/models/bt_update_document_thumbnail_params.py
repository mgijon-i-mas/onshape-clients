# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.93
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTUpdateDocumentThumbnailParams(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'element_update_params': 'list[BTUpdateElementThumbnailParams]',
        'element_params_by_workspace': 'dict(str, list[BTUpdateElementThumbnailParams])',
        'element_params_by_version': 'dict(str, list[BTUpdateElementThumbnailParams])'
    }

    attribute_map = {
        'element_update_params': 'elementUpdateParams',
        'element_params_by_workspace': 'elementParamsByWorkspace',
        'element_params_by_version': 'elementParamsByVersion'
    }

    def __init__(self, element_update_params=None, element_params_by_workspace=None, element_params_by_version=None):  # noqa: E501
        """BTUpdateDocumentThumbnailParams - a model defined in OpenAPI"""  # noqa: E501

        self._element_update_params = None
        self._element_params_by_workspace = None
        self._element_params_by_version = None
        self.discriminator = None

        if element_update_params is not None:
            self.element_update_params = element_update_params
        if element_params_by_workspace is not None:
            self.element_params_by_workspace = element_params_by_workspace
        if element_params_by_version is not None:
            self.element_params_by_version = element_params_by_version

    @property
    def element_update_params(self):
        """Gets the element_update_params of this BTUpdateDocumentThumbnailParams.  # noqa: E501


        :return: The element_update_params of this BTUpdateDocumentThumbnailParams.  # noqa: E501
        :rtype: list[BTUpdateElementThumbnailParams]
        """
        return self._element_update_params

    @element_update_params.setter
    def element_update_params(self, element_update_params):
        """Sets the element_update_params of this BTUpdateDocumentThumbnailParams.


        :param element_update_params: The element_update_params of this BTUpdateDocumentThumbnailParams.  # noqa: E501
        :type: list[BTUpdateElementThumbnailParams]
        """

        self._element_update_params = element_update_params

    @property
    def element_params_by_workspace(self):
        """Gets the element_params_by_workspace of this BTUpdateDocumentThumbnailParams.  # noqa: E501


        :return: The element_params_by_workspace of this BTUpdateDocumentThumbnailParams.  # noqa: E501
        :rtype: dict(str, list[BTUpdateElementThumbnailParams])
        """
        return self._element_params_by_workspace

    @element_params_by_workspace.setter
    def element_params_by_workspace(self, element_params_by_workspace):
        """Sets the element_params_by_workspace of this BTUpdateDocumentThumbnailParams.


        :param element_params_by_workspace: The element_params_by_workspace of this BTUpdateDocumentThumbnailParams.  # noqa: E501
        :type: dict(str, list[BTUpdateElementThumbnailParams])
        """

        self._element_params_by_workspace = element_params_by_workspace

    @property
    def element_params_by_version(self):
        """Gets the element_params_by_version of this BTUpdateDocumentThumbnailParams.  # noqa: E501


        :return: The element_params_by_version of this BTUpdateDocumentThumbnailParams.  # noqa: E501
        :rtype: dict(str, list[BTUpdateElementThumbnailParams])
        """
        return self._element_params_by_version

    @element_params_by_version.setter
    def element_params_by_version(self, element_params_by_version):
        """Sets the element_params_by_version of this BTUpdateDocumentThumbnailParams.


        :param element_params_by_version: The element_params_by_version of this BTUpdateDocumentThumbnailParams.  # noqa: E501
        :type: dict(str, list[BTUpdateElementThumbnailParams])
        """

        self._element_params_by_version = element_params_by_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BTUpdateDocumentThumbnailParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other