import os
import re


def findUserTypePath(type: str, searchDir: str):
    if not os.path.isdir(searchDir):
        return ''

    files = os.listdir(searchDir)
    for file in files:

        if os.path.isdir(os.path.join(searchDir, file)):
            foundDir = findUserTypePath(type, os.path.join(searchDir, file))
            if not foundDir == '':
                return foundDir
        elif os.path.isfile(os.path.join(searchDir, file)) and file.endswith('.py'):
            filePath = os.path.join(searchDir, file)
            with open(filePath, 'r+', encoding='utf-8') as f:
                text = f.read()
                if f'class {type}:\n' in text or f'class {type}(' in text:
                    return filePath
                f.close()
    return ''


def findModuleName(type: str, searchDir: str):
    filePath = findUserTypePath(type, searchDir)
    return os.path.relpath(filePath, '.').replace('.py', '') if filePath != '' else ''


def replaceUserType(searchDir: str):
    print(f'# Processing dir: {searchDir}')
    if not os.path.isdir(searchDir):
        return ''

    files = os.listdir(searchDir)
    for file in files:
        if os.path.isdir(os.path.join(searchDir, file)):
            replaceUserType(os.path.join(searchDir, file))
        elif os.path.isfile(os.path.join(searchDir, file)) and file.endswith('.py'):
            print(f'    # Processing file: {file}')
            filePath = os.path.join(searchDir, file)
            with open(filePath, 'r+', encoding='utf-8') as f:
                text = f.read()
                strings: list[str] = re.findall(r'An? \w+ object', text)
                for string in strings:
                    type = string.split(' ')[-2]
                    module = findModuleName(type, '.').replace('\\', '.')
                    if module == '':
                        continue
                    new_string = string.replace(type, f':py:class:`~{module}.{type}`')
                    text = text.replace(string, new_string)
                    print(f'        # Replaced {type} to :py:class:`~{module}.{type}`')
            if len(strings) > 0:
                with open(filePath, 'r+', encoding='utf-8') as f:
                    f.write(text)


replaceUserType('abaqus')
