from typing import Tuple, List

from openrazer.common import BUS, BUS_NAME
from openrazer.led import Led


class Device:
    def __init__(self, device_path: str):
        self._device_dbus = BUS.get(BUS_NAME, device_path)

        self._leds: List[Led] = []
        # Initialize the LEDs
        for led_path in self._device_dbus.Leds:
            led = Led(led_path)
            self._leds.append(led)

    @property
    def dpi(self) -> Tuple[int, int]:
        return self._device_dbus.getDPI()

    @dpi.setter
    def dpi(self, value: Tuple[int, int]) -> None:
        self._device_dbus.setDPI(value)

    @property
    def firmware_version(self) -> str:
        return self._device_dbus.getFirmwareVersion()

    @property
    def keyboard_layout(self) -> str:
        return self._device_dbus.getKeyboardLayout()

    @property
    def max_dpi(self) -> int:
        return self._device_dbus.getMaxDPI()

    @property
    def name(self) -> str:
        return self._device_dbus.Name

    @property
    def poll_rate(self) -> int:
        return self._device_dbus.getPollRate()

    @poll_rate.setter
    def poll_rate(self, poll_rate: int) -> None:
        self._device_dbus.setPollRate(poll_rate)

    @property
    def serial(self) -> str:
        return self._device_dbus.getSerial()

    @property
    def type(self) -> str:
        return self._device_dbus.Type

    @property
    def supported_features(self) -> List[str]:
        return self._device_dbus.SupportedFeatures

    @property
    def supported_fx(self) -> List[str]:
        return self._device_dbus.SupportedFx

    @property
    def leds(self) -> List[Led]:
        return self._leds
