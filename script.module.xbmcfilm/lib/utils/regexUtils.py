# -*- coding: utf-8 -*-

import re

def findall(data,regex):
    p_reg = re.compile(regex, re.DOTALL + re.MULTILINE + re.UNICODE)
    result = p_reg.findall(data)
    return result

def parseTextToGroups(txt, regex):
    p = re.compile(regex, re.DOTALL + re.MULTILINE + re.UNICODE)
    try:
        m = p.match(txt)
        if m:
            return m.groups()
        else:
            return None
    except:
        return None

def parseText(txt, regex, variables=[]):
    groups = parseTextToGroups(txt, regex)
    print(">>>>>>parseText",txt,regex)

    if variables == []:
        if groups:
            print(">>>>>>parseText",groups[0])
            return groups[0]
        else:
            return ''
    else:
        resultArr = {}
        i = 0
        for v in variables:
            if groups:
                resultArr[v] = groups[i]
            else:
                resultArr[v] = ''
            i += 1
        return resultArr