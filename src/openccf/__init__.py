"""openccf.

An open, interoperable data model for exchanging corporate carbon footprints (GHG Protocol-aligned) between systems.
"""

try:
    from openccf._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
