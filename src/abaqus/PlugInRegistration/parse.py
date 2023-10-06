from __future__ import annotations

from pathlib import Path

import mistletoe
from mistletoe.block_token import Paragraph, Heading, BlockToken
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
        doc = mistletoe.Document(f.readlines())

    data = {}
    sections, current_section = [], []
    for child in doc.children:  # type: BlockToken
        if not isinstance(child, Heading):
            current_section.append(child)
        else:
            sections.append(current_section)
            current_section = [child]

    data["description"] = sections[0][0].children[0].content
    heading: Heading
    paragraphs: list[Paragraph]
    for heading, *paragraphs in sections[1:]:
        pass
