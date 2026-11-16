from __future__ import annotations

from enum import Enum


class Event(str, Enum):
    """Names of the events emitted by observables (Observer pattern).

    Being a ``str`` subclass, each member compares equal to its string value,
    so observers that receive an ``Event`` behave exactly as with plain strings.
    """

    MESSAGES_UPDATED = "messages_updated"
    GENERATING_START = "generating_start"
    GENERATING_DONE = "generating_done"
    GENERATING_ERROR = "generating_error"
    CONFIG_CHANGED = "config_changed"
    EXPORT_DONE = "export_done"
