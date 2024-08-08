from collections.abc import Sequence

from msgspec import Struct


class AnetItem(Struct, omit_defaults=True):
    linkname: str | None = None
    lowerLink: str | None = None
    allowedAddress: str | None = None
    configureAllowedAddress: str | None = None
    defrouter: str | None = None
    macAddress: str | None = None
    linkProtection: str | None = None


class CappedMemory(Struct, omit_defaults=True):
    physical: str | None = None
    swap: str | None = None


class CappedCPU(Struct, omit_defaults=True):
    ncpus: str | None = None


class Solaris(Struct, omit_defaults=True):
    """
    Solaris platform-specific configurations
    """

    milestone: str | None = None
    limitpriv: str | None = None
    maxShmMemory: str | None = None
    cappedCPU: CappedCPU | None = None
    cappedMemory: CappedMemory | None = None
    anet: Sequence[AnetItem] | None = None
