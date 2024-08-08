from collections.abc import Sequence

from msgspec import Struct

from pyoci.platform.linux.devices import Device


class Zos(Struct, omit_defaults=True):
    """
    z/OS platform-specific configurations
    """

    devices: Sequence[Device] | None = None
