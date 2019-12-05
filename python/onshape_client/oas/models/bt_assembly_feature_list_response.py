# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.106
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTAssemblyFeatureListResponse(object):
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
        'features': 'list[BTMAssemblyFeature]',
        'is_complete': 'bool',
        'feature_states': 'dict(str, BTFeatureState)'
    }

    attribute_map = {
        'features': 'features',
        'is_complete': 'isComplete',
        'feature_states': 'featureStates'
    }

    def __init__(self, features=None, is_complete=None, feature_states=None):  # noqa: E501
        """BTAssemblyFeatureListResponse - a model defined in OpenAPI"""  # noqa: E501

        self._features = None
        self._is_complete = None
        self._feature_states = None
        self.discriminator = None

        if features is not None:
            self.features = features
        if is_complete is not None:
            self.is_complete = is_complete
        if feature_states is not None:
            self.feature_states = feature_states

    @property
    def features(self):
        """Gets the features of this BTAssemblyFeatureListResponse.  # noqa: E501


        :return: The features of this BTAssemblyFeatureListResponse.  # noqa: E501
        :rtype: list[BTMAssemblyFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this BTAssemblyFeatureListResponse.


        :param features: The features of this BTAssemblyFeatureListResponse.  # noqa: E501
        :type: list[BTMAssemblyFeature]
        """

        self._features = features

    @property
    def is_complete(self):
        """Gets the is_complete of this BTAssemblyFeatureListResponse.  # noqa: E501


        :return: The is_complete of this BTAssemblyFeatureListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this BTAssemblyFeatureListResponse.


        :param is_complete: The is_complete of this BTAssemblyFeatureListResponse.  # noqa: E501
        :type: bool
        """

        self._is_complete = is_complete

    @property
    def feature_states(self):
        """Gets the feature_states of this BTAssemblyFeatureListResponse.  # noqa: E501


        :return: The feature_states of this BTAssemblyFeatureListResponse.  # noqa: E501
        :rtype: dict(str, BTFeatureState)
        """
        return self._feature_states

    @feature_states.setter
    def feature_states(self, feature_states):
        """Sets the feature_states of this BTAssemblyFeatureListResponse.


        :param feature_states: The feature_states of this BTAssemblyFeatureListResponse.  # noqa: E501
        :type: dict(str, BTFeatureState)
        """

        self._feature_states = feature_states

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
        if not isinstance(other, BTAssemblyFeatureListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other