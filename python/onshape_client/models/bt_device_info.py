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


class BTDeviceInfo(object):
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
        'description': 'str',
        'version': 'BTUserAgentVersion',
        'client_type': 'str',
        'device_name': 'str',
        'operating_system': 'str',
        'device_type': 'str',
        'browser': 'str',
        'manufacturer': 'str',
        'mobile': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'version': 'version',
        'client_type': 'clientType',
        'device_name': 'deviceName',
        'operating_system': 'operatingSystem',
        'device_type': 'deviceType',
        'browser': 'browser',
        'manufacturer': 'manufacturer',
        'mobile': 'mobile'
    }

    def __init__(self, description=None, version=None, client_type=None, device_name=None, operating_system=None, device_type=None, browser=None, manufacturer=None, mobile=None):  # noqa: E501
        """BTDeviceInfo - a model defined in OpenAPI"""  # noqa: E501

        self._description = None
        self._version = None
        self._client_type = None
        self._device_name = None
        self._operating_system = None
        self._device_type = None
        self._browser = None
        self._manufacturer = None
        self._mobile = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if client_type is not None:
            self.client_type = client_type
        if device_name is not None:
            self.device_name = device_name
        if operating_system is not None:
            self.operating_system = operating_system
        if device_type is not None:
            self.device_type = device_type
        if browser is not None:
            self.browser = browser
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if mobile is not None:
            self.mobile = mobile

    @property
    def description(self):
        """Gets the description of this BTDeviceInfo.  # noqa: E501


        :return: The description of this BTDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTDeviceInfo.


        :param description: The description of this BTDeviceInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """Gets the version of this BTDeviceInfo.  # noqa: E501


        :return: The version of this BTDeviceInfo.  # noqa: E501
        :rtype: BTUserAgentVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BTDeviceInfo.


        :param version: The version of this BTDeviceInfo.  # noqa: E501
        :type: BTUserAgentVersion
        """

        self._version = version

    @property
    def client_type(self):
        """Gets the client_type of this BTDeviceInfo.  # noqa: E501


        :return: The client_type of this BTDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this BTDeviceInfo.


        :param client_type: The client_type of this BTDeviceInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "BROWSER", "IOS", "ANDROID", "MAGIC_LEAP"]  # noqa: E501
        if client_type not in allowed_values:
            raise ValueError(
                "Invalid value for `client_type` ({0}), must be one of {1}"  # noqa: E501
                .format(client_type, allowed_values)
            )

        self._client_type = client_type

    @property
    def device_name(self):
        """Gets the device_name of this BTDeviceInfo.  # noqa: E501


        :return: The device_name of this BTDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this BTDeviceInfo.


        :param device_name: The device_name of this BTDeviceInfo.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def operating_system(self):
        """Gets the operating_system of this BTDeviceInfo.  # noqa: E501


        :return: The operating_system of this BTDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this BTDeviceInfo.


        :param operating_system: The operating_system of this BTDeviceInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["WINDOWS", "WINDOWS_10", "WINDOWS_81", "WINDOWS_8", "WINDOWS_7", "WINDOWS_VISTA", "WINDOWS_2000", "WINDOWS_XP", "WINDOWS_10_MOBILE", "WINDOWS_PHONE8_1", "WINDOWS_PHONE8", "WINDOWS_MOBILE7", "WINDOWS_MOBILE", "WINDOWS_98", "XBOX_OS", "ONSHAPE", "ONSHAPE_ANDROID", "ONSHAPE_ANDROID_7", "ONSHAPE_ANDROID_6", "ONSHAPE_ANDROID_5", "ONSHAPE_ANDROID_4", "ONSHAPE_ANDROID_TABLET", "ONSHAPE_ANDROID_7_TABLET", "ONSHAPE_ANDROID_6_TABLET", "ONSHAPE_ANDROID_5_TABLET", "ONSHAPE_ANDROID_4_TABLET", "ONSHAPE_IPHONE", "ONSHAPE_IPHONE_10", "ONSHAPE_IPHONE_9", "ONSHAPE_IPHONE_8_4", "ONSHAPE_IPHONE_8_3", "ONSHAPE_IPHONE_8_2", "ONSHAPE_IPHONE_8_1", "ONSHAPE_IPHONE_8", "ONSHAPE_IPHONE_7", "ONSHAPE_IPAD", "ONSHAPE_IPAD_10", "ONSHAPE_IPAD_9", "ONSHAPE_IPAD_8_4", "ONSHAPE_IPAD_8_3", "ONSHAPE_IPAD_8_2", "ONSHAPE_IPAD_8_1", "ONSHAPE_IPAD_8", "ONSHAPE_IPAD_7", "ONSHAPE_IPOD", "ONSHAPE_IPOD_10", "ONSHAPE_IPOD_9", "ONSHAPE_IPOD_8_4", "ONSHAPE_IPOD_8_3", "ONSHAPE_IPOD_8_2", "ONSHAPE_IPOD_8_1", "ONSHAPE_IPOD_8", "ONSHAPE_IPOD_7", "ANDROID", "ANDROID7", "ANDROID7_TABLET", "ANDROID6", "ANDROID6_TABLET", "ANDROID5", "ANDROID5_TABLET", "ANDROID4", "ANDROID4_TABLET", "ANDROID4_WEARABLE", "ANDROID3_TABLET", "ANDROID2", "ANDROID2_TABLET", "ANDROID1", "ANDROID_MOBILE", "ANDROID_TABLET", "CHROME_OS", "WEBOS", "PALM", "MEEGO", "IOS", "iOS10_IPHONE", "iOS9_IPHONE", "iOS8_4_IPHONE", "iOS8_3_IPHONE", "iOS8_2_IPHONE", "iOS8_1_IPHONE", "iOS8_IPHONE", "iOS7_IPHONE", "iOS6_IPHONE", "iOS5_IPHONE", "iOS4_IPHONE", "MAC_OS_X_IPAD", "iOS10_IPAD", "iOS9_IPAD", "iOS8_4_IPAD", "iOS8_3_IPAD", "iOS8_2_IPAD", "iOS8_1_IPAD", "iOS8_IPAD", "iOS7_IPAD", "iOS6_IPAD", "MAC_OS_X_IPHONE", "MAC_OS_X_IPOD", "MAC_OS_X", "MAC_OS", "MAEMO", "BADA", "GOOGLE_TV", "KINDLE", "KINDLE3", "KINDLE2", "LINUX", "UBUNTU", "UBUNTU_TOUCH_MOBILE", "SYMBIAN", "SYMBIAN9", "SYMBIAN8", "SYMBIAN7", "SYMBIAN6", "SERIES40", "SONY_ERICSSON", "SUN_OS", "PSP", "WII", "BLACKBERRY", "BLACKBERRY7", "BLACKBERRY6", "BLACKBERRY_TABLET", "ROKU", "PROXY", "UNKNOWN_MOBILE", "UNKNOWN_TABLET", "UNKNOWN"]  # noqa: E501
        if operating_system not in allowed_values:
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

    @property
    def device_type(self):
        """Gets the device_type of this BTDeviceInfo.  # noqa: E501


        :return: The device_type of this BTDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this BTDeviceInfo.


        :param device_type: The device_type of this BTDeviceInfo.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def browser(self):
        """Gets the browser of this BTDeviceInfo.  # noqa: E501


        :return: The browser of this BTDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this BTDeviceInfo.


        :param browser: The browser of this BTDeviceInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["OUTLOOK", "OUTLOOK2007", "OUTLOOK2013", "OUTLOOK2010", "IE", "OUTLOOK_EXPRESS7", "IEMOBILE11", "IEMOBILE10", "IEMOBILE9", "IEMOBILE7", "IEMOBILE6", "IE_XBOX", "IE11", "IE10", "IE9", "IE8", "IE7", "IE6", "IE5_5", "IE5", "EDGE", "EDGE12", "EDGE_MOBILE12", "CHROME", "CHROME_MOBILE", "CHROME46", "CHROME45", "CHROME44", "CHROME43", "CHROME42", "CHROME41", "CHROME40", "CHROME39", "CHROME38", "CHROME37", "CHROME36", "CHROME35", "CHROME34", "CHROME33", "CHROME32", "CHROME31", "CHROME30", "CHROME29", "CHROME28", "CHROME27", "CHROME26", "CHROME25", "CHROME24", "CHROME23", "CHROME22", "CHROME21", "CHROME20", "CHROME19", "CHROME18", "CHROME17", "CHROME16", "CHROME15", "CHROME14", "CHROME13", "CHROME12", "CHROME11", "CHROME10", "CHROME9", "CHROME8", "OMNIWEB", "SAFARI", "BLACKBERRY10", "MOBILE_SAFARI", "SILK", "SAFARI9", "SAFARI8", "SAFARI7", "SAFARI6", "SAFARI5", "SAFARI4", "COAST", "COAST1", "OPERA", "OPERA_MOBILE", "OPERA_MINI", "OPERA34", "OPERA33", "OPERA32", "OPERA31", "OPERA30", "OPERA29", "OPERA28", "OPERA27", "OPERA26", "OPERA25", "OPERA24", "OPERA23", "OPERA20", "OPERA19", "OPERA18", "OPERA17", "OPERA16", "OPERA15", "OPERA12", "OPERA11", "OPERA10", "OPERA9", "KONQUEROR", "DOLFIN2", "APPLE_WEB_KIT", "APPLE_ITUNES", "APPLE_APPSTORE", "ADOBE_AIR", "LOTUS_NOTES", "CAMINO", "CAMINO2", "FLOCK", "FIREFOX", "FIREFOX3MOBILE", "FIREFOX_MOBILE", "FIREFOX_MOBILE23", "FIREFOX42", "FIREFOX41", "FIREFOX40", "FIREFOX39", "FIREFOX38", "FIREFOX37", "FIREFOX36", "FIREFOX35", "FIREFOX34", "FIREFOX33", "FIREFOX32", "FIREFOX31", "FIREFOX30", "FIREFOX29", "FIREFOX28", "FIREFOX27", "FIREFOX26", "FIREFOX25", "FIREFOX24", "FIREFOX23", "FIREFOX22", "FIREFOX21", "FIREFOX20", "FIREFOX19", "FIREFOX18", "FIREFOX17", "FIREFOX16", "FIREFOX15", "FIREFOX14", "FIREFOX13", "FIREFOX12", "FIREFOX11", "FIREFOX10", "FIREFOX9", "FIREFOX8", "FIREFOX7", "FIREFOX6", "FIREFOX5", "FIREFOX4", "FIREFOX3", "FIREFOX2", "FIREFOX1_5", "THUNDERBIRD", "THUNDERBIRD12", "THUNDERBIRD11", "THUNDERBIRD10", "THUNDERBIRD8", "THUNDERBIRD7", "THUNDERBIRD6", "THUNDERBIRD3", "THUNDERBIRD2", "VIVALDI", "ONSHAPE", "ONSHAPE_IPAD", "ONSHAPE_IPHONE", "ONSHAPE_ANDROID", "SEAMONKEY", "BOT", "BOT_MOBILE", "MOZILLA", "CFNETWORK", "EUDORA", "POCOMAIL", "THEBAT", "NETFRONT", "EVOLUTION", "LYNX", "DOWNLOAD", "UNKNOWN", "APPLE_MAIL"]  # noqa: E501
        if browser not in allowed_values:
            raise ValueError(
                "Invalid value for `browser` ({0}), must be one of {1}"  # noqa: E501
                .format(browser, allowed_values)
            )

        self._browser = browser

    @property
    def manufacturer(self):
        """Gets the manufacturer of this BTDeviceInfo.  # noqa: E501


        :return: The manufacturer of this BTDeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this BTDeviceInfo.


        :param manufacturer: The manufacturer of this BTDeviceInfo.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def mobile(self):
        """Gets the mobile of this BTDeviceInfo.  # noqa: E501


        :return: The mobile of this BTDeviceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this BTDeviceInfo.


        :param mobile: The mobile of this BTDeviceInfo.  # noqa: E501
        :type: bool
        """

        self._mobile = mobile

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
        if not isinstance(other, BTDeviceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other