from typing import Tuple, List

from openrazer.common import BUS, BUS_NAME
from openrazer.led import Led


class Device:
    """
    Class representing a device managed by OpenRazer. You can do device-specific actions, like getting the firmware
    version, name or getting and setting the DPI.

    You can also get a list of LEDs available on that device where lighting effects can be adjusted.

    Remember to check if the device actually supports a feature (supported_features) before using it!
    """

    def __init__(self, device_path: str):
        self._device_dbus = BUS.get(BUS_NAME, device_path)

        self._leds: List[Led] = []
        # Initialize the LEDs
        for led_path in self._device_dbus.Leds:
            led = Led(led_path)
            self._leds.append(led)

    @property
    def dpi(self) -> Tuple[int, int]:
        """
        Get the DPI of the device.

        :return: A tuple of 2 integers containing the current DPI, like ``(500, 500)``
        """
        return self._device_dbus.getDPI()

    @dpi.setter
    def dpi(self, dpi: Tuple[int, int]) -> None:
        """
        Set the DPI of the device.

        :param dpi: A tuple of 2 integers containing the DPI to be set, like ``(500, 500)``
        """
        self._device_dbus.setDPI(dpi)

    @property
    def firmware_version(self) -> str:
        """
        Get the firmware version of the device.

        :return: A string containing the firmware version as reported by the device, like ``v1.0``
        """
        return self._device_dbus.getFirmwareVersion()

    @property
    def keyboard_layout(self) -> str:
        """
        Get the keyboard layout of the device.

        :return: A string containing the keyboard layout, like ``US`` or ``German``
        """
        return self._device_dbus.getKeyboardLayout()

    @property
    def max_dpi(self) -> int:
        """
        Get the maximum value possible for the DPI.

        :return: An integer containing the maximum value possible for the DPI
        """
        return self._device_dbus.getMaxDPI()

    @property
    def name(self) -> str:
        """
        Get the device name.

        :return: A string containing the device name, like ``Razer BlackWidow Chroma``
        """
        return self._device_dbus.Name

    @property
    def poll_rate(self) -> int:
        """
        Get the polling rate of the device.

        :return: An integer containing the current poll rate.
        """
        return self._device_dbus.getPollRate()

    @poll_rate.setter
    def poll_rate(self, poll_rate: int) -> None:
        """
        Set the polling rate of the device.

        :param poll_rate: An integer containing the polling rate to be set
        """
        self._device_dbus.setPollRate(poll_rate)

    @property
    def serial(self) -> str:
        """
        Get the serial of the device.

        :return: A string describing the serial number of the device, like ``PM123456789``
        """
        return self._device_dbus.getSerial()

    @property
    def type(self) -> str:
        """
        Get the type of the device.

        :return: A string describing the type of the device, like ``keyboard`` or ``mouse``
        """
        return self._device_dbus.Type

    @property
    def supported_features(self) -> List[str]:
        """
        Get the supported features of the device.

        :return: A list of strings containing the supported features, like ``[dpi, poll_rate]``
        """
        return self._device_dbus.SupportedFeatures

    @property
    def supported_fx(self) -> List[str]:
        """
        Get the supported effects of the LEDs on the device.

        :return: A list of strings containing the supported effects on the LEDs, like ``[off, static]``
        """
        return self._device_dbus.SupportedFx

    @property
    def leds(self) -> List[Led]:
        """
        Get a list of LEDs on the device.

        :return: A list of Led objects
        """
        return self._leds
