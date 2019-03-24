import sys

if sys.platform == 'linux' or sys.platform.startswith('freebsd'):
    from pydbus import SystemBus  # type: ignore

    BUS = SystemBus()
elif sys.platform == 'darwin' or sys.platform == 'win32' or sys.platform == 'cygwin':
    from pydbus import SessionBus  # type: ignore

    BUS = SessionBus()
else:
    raise RuntimeError('Please add support for your OS ({}) in common.py'.format(sys.platform))

BUS_NAME = "io.github.openrazer1"

RLED_ID_SCROLL = 0x01
RLED_ID_LOGO = 0x04
RLED_ID_BACKLIGHT = 0x05
