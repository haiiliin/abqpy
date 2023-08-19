from __future__ import annotations

from typing import Dict

from .ReferencePoint import ReferencePoint


class ReferencePoints(Dict[str, ReferencePoint]):
    def __getitem__(self, key: str) -> ReferencePoint:
        if key in self.keys():
            return self.get(key)  # type: ignore
        else:
            return ReferencePoint(point=(0.0, 0.0, 0.0))
