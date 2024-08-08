from collections.abc import Sequence

from msgspec import Struct

from pyoci.common import IDMapping

FilePath = str


class Root(Struct):
    """
    Configures the container's root filesystem.
    """

    path: FilePath
    readonly: bool | None = None


class Mount(Struct):
    destination: FilePath
    source: FilePath | None = None
    options: Sequence[str] | None = None
    type: str | None = None
    uidMappings: Sequence[IDMapping] | None = None
    gidMappings: Sequence[IDMapping] | None = None
