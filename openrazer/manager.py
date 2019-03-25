from typing import List

from openrazer.common import BUS, BUS_NAME
from openrazer.device import Device


class Manager:
    """
    Class representing the main body managing all devices connected to a system. You can get the available devices
    and do actions that are not device-specific (such as toggling the 'Sync Effects' state)
    """
    def __init__(self) -> None:
        self._manager_dbus = BUS.get(BUS_NAME)

        self._devices: List[Device] = []
        # Initialize the devices
        for device_path in self._manager_dbus.Devices:
            device = Device(device_path)
            self._devices.append(device)

    @property
    def version(self) -> str:
        """
        Get the version of OpenRazer that is running

        :return: A string describing the version, like ``1.0.0``
        """
        return self._manager_dbus.Version

    @property
    def devices(self) -> List[Device]:
        """
        Get a list of devices available.

        :return: A list of Device objects
        """
        return self._devices

    @property
    def sync_effects(self) -> bool:
        # TODO Stub
        return True

    @sync_effects.setter
    def sync_effects(self, sync: bool) -> None:
        # TODO Stub
        pass

    # TODO devicesChanged / ondevicesChanged
