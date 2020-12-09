import json
from pathlib import Path
import re


def saveToJsonFile(data, dir_Path):
    # create new json File and Write data on it
    with open(Path(dir_Path).absolute(), 'w', encoding='utf-8') as jsonFile:
        # make it more readable and pretty
        jsonFile.write(json.dumps(data, indent=4, ensure_ascii=False))


def loadFromJsonFile(file_Path):
    data = []
    with open(Path(file_Path).absolute()) as f:
        data = json.load(f)
    return data


def removeTabAndLineCharacter():
    pass


# it removes \t and \n and spaces
def removeTabAndLineCharacterAndSpaces(input):
    return re.sub(r'\s+', '', input)


def removeHTMLTags(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def persianCharacterResolver(per_string):
    switcher = {
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9"}

    resolved_string = ""
    for per_char in per_string:
        resolved_string += switcher.get(per_char, "")

    return int(resolved_string)


def checkForNone(input):
    if (input is None):
        return NoneVal()
    else:
        return input


class NoneVal:
    def get_text(self):
        return "None"


def convertToArrayDictionary(jsonPath):
    data = []
    with open(jsonPath.absolute()) as f:
        data = json.load(f)
    return data
