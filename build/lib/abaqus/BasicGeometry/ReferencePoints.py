from typing import Dict

from .ReferencePoint import ReferencePoint


class ReferencePoints(Dict[int, ReferencePoint]):
    def __getitem__(self, key: int) -> ReferencePoint:
        if key in self.keys():
            return self.get(key)
        else:
            return ReferencePoint(point=(0.0, 0.0, 0.0))
