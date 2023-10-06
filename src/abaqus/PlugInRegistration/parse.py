from __future__ import annotations

import re
from pathlib import Path

from pydantic import BaseModel


class Argument(BaseModel):
    name: str
    type: str
    required: bool
    default: str | None = None


class Method(BaseModel):
    name: str
    description: str
    arguments: list[Argument]


class Flag(BaseModel):
    pass


class Class(BaseModel):
    description: str
    methods: list[Method]
    flags: list[Flag] = []


for md in Path(".").glob("*.md"):
    with md.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    sections, current_section = [], []
    for line in lines:
        line = re.sub(r"!\[.*]\(.*\)", "", line)
        if not line.strip():
            continue
        if line.startswith("#"):
            sections.append(current_section)
            current_section = [line.lstrip("#").strip()]
        else:
            current_section.append(line.strip())
    sections.append(current_section)

    data = {"description": sections[0][0]}
    heading: list[str]
    paragraphs: list[list[str]]
    for heading, *paragraphs in sections[1:]:
        pass

    break
