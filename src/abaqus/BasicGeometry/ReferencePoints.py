from __future__ import annotations

from .ReferencePoint import ReferencePoint


class ReferencePoints(dict[str, ReferencePoint]):
    def __getitem__(self, key: str) -> ReferencePoint:
        if key in self.keys():
            return self.get(key)  # type: ignore
        else:
            return ReferencePoint(point=(0.0, 0.0, 0.0))
