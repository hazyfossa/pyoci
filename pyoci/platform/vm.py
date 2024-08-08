from collections.abc import Sequence
from typing import Literal

from msgspec import Struct

from pyoci.filesystem import FilePath

RootImageFormat = Literal["raw", "qcow2", "vdi", "vmdk", "vhd"]


class Image(Struct, omit_defaults=True):
    path: FilePath
    format: RootImageFormat


class Hypervisor(Struct, omit_defaults=True):
    path: FilePath
    parameters: Sequence[str] | None = None


class Kernel(Struct, omit_defaults=True):
    path: FilePath
    parameters: Sequence[str] | None = None
    initrd: FilePath | None = None


class Vm(Struct, omit_defaults=True):
    kernel: Kernel
    hypervisor: Hypervisor | None = None
    image: Image | None = None
