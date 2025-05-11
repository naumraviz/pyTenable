"""
Tenable Exposure Management
============================

This package covers the Tenable Exposure Management.

.. autoclass:: TenableExposureManagement
    :members:


.. toctree::
    :hidden:
    :glob:

    inventory
    apa
    tags
"""

from typing import Optional

from tenable.base.platform import APIPlatform
from .apa import TenableAPA
from .inventory import TenableInventory
from .tags.api import TagsAPI


class TenableExposureManagement(APIPlatform):
    """
    The Tenable Exposure Management object is the primary interaction
    point for users to interface with Tenable Exposure Management
    via the pyTenable library.  All the API endpoint classes that have
     been written will be grafted onto this class.

    Examples:
        Basic Example:

        >>> from tenable.exposure_management import TenableExposureManagement
        >>> tenable_exposure_management = TenableExposureManagement('ACCESS_KEY', 'SECRET_KEY')

        Example with proper identification:

        >>> tenable_exposure_management = TenableExposureManagement('ACCESS_KEY', 'SECRET_KEY',
        >>>     vendor='Company Name',
        >>>     product='My Awesome Widget',
        >>>     build='1.0.0')
    """

    _env_base = "TenableExposureManagement"
    _url = "https://cloud.tenable.com"
    _box = True

    def __init__(
            self,
            access_key: Optional[str] = None,
            secret_key: Optional[str] = None,
            **kwargs
    ):
        if access_key:
            kwargs["access_key"] = access_key
        if secret_key:
            kwargs["secret_key"] = secret_key
        super().__init__(**kwargs)

    @property
    def inventory(self):
        """
        The interface object for the
        :doc:`Tenable Inventory APIs <findings>`.
        """
        return TenableInventory()

    @property
    def apa(self):
        """
        The interface object for the
        :doc:`Tenable Attack Path Analysis APIs <findings>`.
        """
        return TenableAPA()

    @property
    def tags(self):
        """
        The interface object for the
        :doc:`Tags APIs <findings>`.
        """
        return TagsAPI(self)
