import openrazer


def test_stuff():
    manager = openrazer.Manager()
    print("Version: " + manager.version)

    for device in manager.devices:
        print("Name: " + device.name)
        print("  Type: " + device.type)
        print("  Serial: " + device.serial)
        print("  Firmware Version: " + device.firmware_version)
        if "dpi" in device.supported_features:
            print("  DPI: " + str(device.dpi))
            print("  Max DPI: " + str(device.max_dpi))
        if "keyboard_layout" in device.supported_features:
            print("  Keyboard Layout: " + device.keyboard_layout)
        if "poll_rate" in device.supported_features:
            print("  Poll rate: " + str(device.poll_rate))

        for led in device.leds:
            print("  Led: " + str(led.led_id))
            if "brightness" in device.supported_fx:
                print("    Brightness: " + str(led.brightness))
            if "off" in device.supported_fx:
                led.off()
            if "static" in device.supported_fx:
                led.static((0x00, 0xFF, 0x00))
            if "blinking" in device.supported_fx:
                led.blinking((0xFF, 0x00, 0x00))
            if "breathing" in device.supported_fx:
                led.breathing((0xFF, 0x00, 0x00))
            if "breathing_dual" in device.supported_fx:
                led.breathing_dual((0xFF, 0x00, 0x00), (0x00, 0x00, 0xFF))
            if "breathing_random" in device.supported_fx:
                led.breathing_random()
            if "spectrum" in device.supported_fx:
                led.spectrum()
            if "wave" in device.supported_fx:
                led.wave(0x01)
            if "reactive" in device.supported_fx:
                led.reactive(0x01, (0x00, 0xFF, 0x00))


if __name__ == '__main__':
    test_stuff()
