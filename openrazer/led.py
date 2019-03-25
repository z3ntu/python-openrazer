from typing import List, Tuple

from openrazer.common import BUS, BUS_NAME


class Led:
    """
    CLass representing an Led on a device. You can set the brightness or effects here, get the currently active
    effect and the curent colors
    """

    def __init__(self, led_path: str):
        self._led_dbus = BUS.get(BUS_NAME, led_path)

    @property
    def current_colors(self) -> List[Tuple[int, int, int]]:
        """
        Get the colors that were previously set.

        :return: A list of color tuples, like ``[(255, 0, 0), (0, 255, 0), (0, 0, 255)]``
        """
        return self._led_dbus.CurrentColors

    @property
    def current_effect(self) -> int:
        """
        Get the effect that is currently active.

        :return: An integer representing the current effect.
        """
        return self._led_dbus.CurrentEffect

    @property
    def led_id(self) -> int:
        """
        Get the Led ID of this Led.

        :return: An integer representing the Led ID of this Led.
        """
        return self._led_dbus.LedId[0]

    @property
    def brightness(self) -> float:
        """
        Get the brightness of the Led.

        :return: The brightness as a float value between ``0`` and ``100``
        """
        return self._led_dbus.getBrightness() / 255 * 100

    @brightness.setter
    def brightness(self, brightness: float) -> None:
        """
        Set the brightness of the Led.

        :param brightness: The brightness as a float value between ``0`` and ``100``
        """
        self._led_dbus.setBrightness(brightness / 100 * 255)

    def blinking(self, color: Tuple[int, int, int]) -> bool:
        """
        Set the Led to the Blinking effect.

        :param color: The color in which the Led should blink.
        """
        return self._led_dbus.setBlinking(color)

    def breathing(self, color: Tuple[int, int, int]) -> bool:
        """
        Set the Led to the Breathing (single color) effect.

        :param color: The color in which the Led should be breathing.
        """
        return self._led_dbus.setBreathing(color)

    def breathing_dual(self, color: Tuple[int, int, int], color2: Tuple[int, int, int]) -> bool:
        """
        Set the Led to the Breathing (dual color) effect.

        :param color: The first color in which the Led should be breathing.
        :param color2: The second color in which the Led should be breathing.
        """
        return self._led_dbus.setBreathingDual(color, color2)

    def breathing_random(self) -> bool:
        """
        Set the Led to the Breathing (random) effect.
        """
        return self._led_dbus.setBreathingRandom()

    def off(self) -> bool:
        """
        Set the Led to Off.
        """
        return self._led_dbus.setOff()

    def reactive(self, speed: int, color: Tuple[int, int, int]) -> bool:
        """
        Set the Led to the Reactive effect.

        :param speed: An integer representing the Speed in which the effect should last.
        :param color: The color in which the pressed keys should light up.
        """
        return self._led_dbus.setReactive((speed,), color)

    def spectrum(self) -> bool:
        """
        Set the Led to the Spectrum effect.
        """
        return self._led_dbus.setSpectrum()

    def static(self, color: Tuple[int, int, int]) -> bool:
        """
        Set the Led to the Static effect.

        :param color: The color in which the Led should be lighting up.
        """
        return self._led_dbus.setStatic(color)

    def wave(self, direction: int) -> bool:
        """
        Set the Led to the Wave effect.

        :param direction: An integer representing the direction the Wave effect should be played at.
        """
        return self._led_dbus.setWave((direction,))
