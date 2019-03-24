from typing import List, Tuple

from openrazer.common import BUS, BUS_NAME


class Led:
    def __init__(self, led_path: str):
        self._led_dbus = BUS.get(BUS_NAME, led_path)

    @property
    def current_colors(self) -> List[Tuple[int]]:
        return self._led_dbus.CurrentColors

    @property
    def current_effect(self) -> int:
        return self._led_dbus.CurrentEffect

    @property
    def led_id(self) -> int:
        return self._led_dbus.LedId[0]

    @property
    def brightness(self) -> float:
        return self._led_dbus.getBrightness() / 255 * 100

    @brightness.setter
    def brightness(self, brightness: float) -> None:
        self._led_dbus.setBrightness(brightness / 100 * 255)

    def blinking(self, red: int, green: int, blue: int) -> bool:
        return self._led_dbus.setBlinking((red, green, blue))

    def breathing(self, red: int, green: int, blue: int) -> bool:
        return self._led_dbus.setBreathing((red, green, blue))

    def breathing_dual(self, red: int, green: int, blue: int, red2: int, green2: int, blue2: int) -> bool:
        return self._led_dbus.setBreathingDual((red, green, blue), (red2, green2, blue2))

    def breathing_random(self) -> bool:
        return self._led_dbus.setBreathingRandom()

    def off(self) -> bool:
        return self._led_dbus.setOff()

    def reactive(self, speed: int, red: int, green: int, blue: int) -> bool:
        return self._led_dbus.setReactive((speed,), (red, green, blue))

    def spectrum(self) -> bool:
        return self._led_dbus.setSpectrum()

    def static(self, red: int, green: int, blue: int) -> bool:
        return self._led_dbus.setStatic((red, green, blue))

    def wave(self, direction: int) -> bool:
        return self._led_dbus.setWave((direction,))
