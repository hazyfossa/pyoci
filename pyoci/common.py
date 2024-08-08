from collections.abc import Sequence
from typing import Mapping

from msgspec import Struct

from pyoci.int_types import Uint32

UID = Uint32

GID = Uint32

Env = Sequence[str]


class IDMapping(Struct):
    containerID: Uint32
    hostID: Uint32
    size: Uint32


Annotations = Mapping[str, str]
