import os
import re
from typing import List


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
                strings: List[str] = re.findall(r'An? \w+ object', text)
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


# replaceUserType('abaqus')

def addAttributes(searchDir: str):
    print(f'# Processing dir: {searchDir}')
    if not os.path.isdir(searchDir):
        return ''

    files = os.listdir(searchDir)
    for file in files:
        if os.path.isdir(os.path.join(searchDir, file)):
            addAttributes(os.path.join(searchDir, file))
        elif os.path.isfile(os.path.join(searchDir, file)) and file.endswith('.md'):
            print(f'    # Processing file: {file}')
            filePath = os.path.join(searchDir, file)
            with open(filePath, 'r+', encoding='utf-8') as f:
                text = f.read()
                strings: List[str] = re.findall(
                    r'The \w+ object has members with the same names and descriptions as the arguments to the ', text)

            if len(strings) > 0:
                pyFilePath = filePath.replace('markdown', 'abaqus').replace('.md', '.py')
                if not os.path.exists(pyFilePath):
                    continue
                with open(pyFilePath, 'r+', encoding='utf-8') as f:
                    text = f.read()
                    strings = re.findall(r'def __init__[\w\W]+?Parameters\s+-+\s+([\w\W]+?)\s+Returns', text)

                if len(strings) > 0:
                    signatures = re.findall(r'def __init__\(([\w\W]+?)\):', text)
                    if len(signatures) == 0:
                        continue

                    signatureString = signatures[0].lstrip().rstrip().replace('\n', ' ')
                    signatureString = re.sub(r'\n\s+', r'\n', signatureString)
                    # signatures = signatures.split(', ')[1:]

                    argStrings = strings[0].replace('\n        ', '\n')
                    lines = argStrings.splitlines()
                    keys, docs = [], []
                    doc = ''
                    for line in lines:
                        if not line.startswith('    '):
                            keys.append(line.lstrip().rstrip().split(': ')[0])
                            if not doc == '':
                                docs.append(doc.rstrip())
                            doc = ''
                        else:
                            doc += line.lstrip().rstrip() + '\n'
                    docs.append(doc)
                    attr_docstring = '    Attributes\n    ----------'
                    atts = ''
                    for key, doc in zip(keys, docs):
                        doc = doc.rstrip()
                        att_doc = doc.replace('\n', '\n        ')
                        attr_docstring += f'\n    {key}\n        {att_doc}'

                        index = signatureString.index(key + ': ')
                        if key == keys[-1]:
                            signature = signatureString[index:]
                        else:
                            next_index = signatureString.index(keys[keys.index(key) + 1] + ': ')
                            signature = signatureString[index:next_index]

                        signature = signature.lstrip().rstrip()
                        if signature.endswith(','):
                            signature = signature[:-1]
                        att_doc = '# ' + doc.replace('\n', '\n    # ')
                        atts += f'\n\n    {att_doc}\n    {signature}'
                    atts = atts.lstrip()
                    new_text = text.replace('    Notes\n    -----',
                                            f'{attr_docstring}\n\n    Notes\n    -----') \
                        .replace('def __init__(', f'{atts}\n\n    def __init__(')
                    if '\\' in atts:
                        new_text = re.sub(r'(class \w+[\w\W]+?:\n\s+)"""', r'\g<1>r"""', new_text)
                    with open(pyFilePath, 'w+', encoding='utf-8') as f:
                        f.write(new_text)


# addAttributes('markdown')

def replaceNotes(searchDir: str):
    print(f'# Processing dir: {searchDir}')
    if not os.path.isdir(searchDir):
        return ''

    files = os.listdir(searchDir)
    for file in files:
        if os.path.isdir(os.path.join(searchDir, file)):
            replaceNotes(os.path.join(searchDir, file))
        elif os.path.isfile(os.path.join(searchDir, file)) and file.endswith('.py'):
            print(f'    # Processing file: {file}')
            filePath = os.path.join(searchDir, file)
            with open(filePath, 'r+', encoding='utf-8') as f:
                text = f.read()

            # Replace Class Notes
            class_notes = re.findall(r'(Notes\s+-----\s+This object can be accessed by:\s+\.\. code-block:: python\s+)'
                                     r'([\w\W]+?)\n\s+"""', text)
            for head, code in class_notes:
                new_head = '.. note:: \n        This object can be accessed by:\n\n        '\
                           '.. code-block:: python\n\n        '
                new_code = '    ' + code.replace('\n    ', '\n        ')
                string = head + code
                new_string = new_head + new_code
                text = text.replace(string, new_string)

            # Replace Method Notes
            method_notes = re.findall(r'(Notes\s+-----\s+This function can be accessed by:\s+\.\. code-block:: python\s+)'
                                      r'([\w\W]+?)\n\n', text)
            for head, code in method_notes:
                new_head = '.. note:: \n            This function can be accessed by:\n\n'\
                           '            .. code-block:: python\n\n            '
                new_code = '    ' + code.replace('\n    ', '\n        ')
                string = head + code
                new_string = new_head + new_code
                text = text.replace(string, new_string)

            if len(class_notes) + len(method_notes) > 0:
                with open(filePath, 'r+', encoding='utf-8') as f:
                    f.write(text)


replaceNotes('abaqus')
