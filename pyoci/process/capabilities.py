from msgspec import Struct

from collections.abc import Sequence


class Capabilities(Struct, omit_defaults=True):
    bounding: Sequence[str] | None = None
    permitted: Sequence[str] | None = None
    effective: Sequence[str] | None = None
    inheritable: Sequence[str] | None = None
    ambient: Sequence[str] | None = None
