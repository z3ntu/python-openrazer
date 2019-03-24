from typing import List

from openrazer.common import BUS, BUS_NAME
from openrazer.device import Device


class Manager:
    def __init__(self) -> None:
        self._manager_dbus = BUS.get(BUS_NAME)

        self._devices: List[Device] = []
        # Initialize the devices
        for device_path in self._manager_dbus.Devices:
            device = Device(device_path)
            self._devices.append(device)

    @property
    def version(self) -> str:
        return self._manager_dbus.Version

    @property
    def devices(self) -> List[Device]:
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
