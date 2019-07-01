# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 21:11:17 2019

@author: pablo
"""

import json
import time
import data

def saveReadable(fileName, string):
    
    file = open(fileName, 'w')
    
    file.write(string)
    
    file.close()

def stringifyComps(combinations):
    
    result = ''
    
    for combination in combinations:
        for champNum in range(1, len(combination)):
            result += (combination[champNum][0] + ' ')
        result += '\n'
    
    return result

def loadJson(size):
    
    file = open('TFT_' + str(size) + '.txt', 'r')
    
    result = json.loads(file.read())
    
    file.close()
    
    return result

def saveJson(combinations):
    
    file = open('TFT_' + str(len(combinations[0]) - 1) + '.txt', 'w')
    
    file.write(json.dumps(combinations))
    
    file.close()

def searchByClass():
    
    result = []
    
    
    
    return result

def searchByCost(combinations, aimOccurrences):
    
    result = []
    
    for combination in combinations:
        occurrences = [0]*5
        for champNum in range(1, len(combination)):
            occurrences[combination[champNum][1] - 1] += 1
        if occurrences == aimOccurrences:
            result.append(combination)
    
    return result

def sortResult(combinations, costMeans):
    
    result = []
    
    for combinationNum in range(len(combinations)):
        result.append([])
        for champ in combinations[combinationNum]:
            result[combinationNum].append(champ)
        result[combinationNum].sort(key = lambda x: x[1])
        result[combinationNum].insert(0, costMeans[combinationNum])
    
    return sorted(result)

def computeCostMean(combinations):
    
    result = []
    
    for combination in combinations:
        auxSum = 0
        for champ in combination:
            auxSum += champ[1]
        
        result.append(auxSum/len(combination))
    
    return result
            

def resultToName(combinations, numToName):
    
    result = []
    
    for combinationNum in range(len(combinations)):
        result.append([])
        for champ in combinations[combinationNum]:
            result[combinationNum].append([numToName[champ]['name'], numToName[champ]['cost']])
    
    return result

def checkMatch(champList, champClasses, classThresholds):
    
    result = True
    
    occurrences = {}
    
    for champ in champList:
        for champClass in champClasses[champ]:
            if champClass in occurrences.keys():
                occurrences[champClass] += 1
            else:
                occurrences[champClass] = 1
    
    for key in occurrences:
        if not(occurrences[key] in classThresholds[key]):
            result = False
    
    return result

def combine(result, prevList, nChamp, maxChamp, champClasses, classThresholds):
    
    if nChamp > maxChamp:
        if checkMatch(prevList, champClasses, classThresholds):
            result.append(prevList)
    else:
        firstChamp = 0
        if len(prevList) > 0:
            firstChamp = prevList[-1]
        for champ in range(firstChamp, len(champClasses)):
            if not(champ in prevList):
                newList = prevList.copy()
                newList.append(champ)
                result = combine(result, newList, nChamp + 1, maxChamp, champClasses, classThresholds)
    
    return result

def findComps(champCap):
    
    t = time.time()
    result = combine([], [], 1, champCap, data.champClasses, data.classThresholds)
    elapsed = time.time() - t
    print('Time elapsed: ' + str(elapsed))
    
    result = resultToName(result, data.numToName)
    costMeans = computeCostMean(result)
    result = sortResult(result, costMeans)
    
    return result