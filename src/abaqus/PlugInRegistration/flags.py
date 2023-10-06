import re
import textwrap
from pathlib import Path

flag_pattern = r"\|\s*\*\*(\w+)\*\*\s*\|\s*(\w.+?)\s*\|"
flag_template = """\
#: {description}
{flag}: {type} = {value}
"""
class_flags, global_flags = {}, {}
for file in Path(".").glob("*.md"):
    class_flags[file.stem], global_flags[file.stem] = {}, {}
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    class_flags_start = content.find("## Class flags")
    global_flags_start = content.find("## Global flags")
    if class_flags_start != -1:
        if global_flags_start != -1:
            class_flags_content = content[class_flags_start:global_flags_start]
            global_flags_content = content[global_flags_start:]
        else:
            class_flags_content = content[class_flags_start:]
            global_flags_content = ""
    else:
        class_flags_content = ""
        global_flags_content = content[global_flags_start:] if global_flags_start != -1 else ""

    # Find all class and global flags
    for match in re.finditer(flag_pattern, class_flags_content):
        class_flags[file.stem][match.group(1)] = match.group(2)
    if not class_flags[file.stem]:
        del class_flags[file.stem]
    for match in re.finditer(flag_pattern, global_flags_content):
        global_flags[file.stem][match.group(1)] = match.group(2)
    if not global_flags[file.stem]:
        del global_flags[file.stem]
    # break

for class_name, flags in class_flags.items():
    with open(f"{class_name}.py", "r", encoding="utf-8") as f:
        content = f.read()

    # Format flags
    class_flags_formatted = textwrap.indent(
        "\n".join(
            [
                flag_template.format(description=description, flag=flag, type="int", value=f'hash("{flag}")')
                for flag, description in flags.items()
            ]
        ),
        " " * 4,
    )
    content = content.replace("    def __init__(", f"{class_flags_formatted}\n    def __init__(")
    with open(f"{class_name}.py", "w", encoding="utf-8") as f:
        f.write(content)

for class_name, flags in global_flags.items():
    with open(f"{class_name}.py", "r", encoding="utf-8") as f:
        content = f.read()
    global_flags_formatted = "\n".join(
        [
            flag_template.format(description=description, flag=flag, type="int", value=f'hash("{flag}")')
            for flag, description in global_flags[class_name].items()
        ]
    )
    content = content.replace(f"class {class_name}", f"{global_flags_formatted}\n\nclass {class_name}")
    with open(f"{class_name}.py", "w", encoding="utf-8") as f:
        f.write(content)
