# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 00:21:24 2019

@author: pablo
"""

"""
1 -> 3, 6 Assassin
2 -> 3, 6 Blademaster
3 -> 2, 4 Brawler
4 -> 3 Elementalist
5 -> 2, Guardian
6 -> 2, 4 Gunslinger
7 -> 2, 4, 6 Knight
8 -> 2, 4 Ranger
9 -> 3 Shapeshifter
10 -> 3, 6 Sorcerer
11 -> 2, 4, 6 Demon
12 -> 2 Dragon
13 -> 2, 4, 6 Glacial
14 -> 2, 4 Imperial
15 -> 3, 6 Nobel
16 -> 1, 4 Ninja
17 -> 3 Pirate
18 -> 2 Phantom
19 -> 2, 4 Wild
20 -> 3 Void
21 -> 3, 6 Yordle
"""

champClasses = [
        [2, 11], #Aatrox 0
        [10, 19], #Ahri 1
        [1, 16], #Akali 2
        [4, 13], #Anivia 3
        [8, 13], #Ashe 4
        [10, 12], #Aurelion 5
        [3], #Blitzcrank 6
        [4, 11], #Brand 7
        [5, 13], #Braum 8
        [3, 20], #ChoGath 9
        [7, 14], #Darius 10
        [2, 14], #Draven 11
        [9, 11], #Elise 12
        [1, 11], #Evelynn 13
        [2, 15], #Fiora 14
        [2, 6, 17], #Gangplank 15
        [7, 15], #Garen 16
        [9, 19, 21], #Gnar 17
        [6, 17], #Graves 18
        [10, 18], #Karthus 19
        [10, 20], #Kassadin 20
        [1, 14], #Katarina 21
        [7, 15], #Kayle 22
        [4, 16, 21], #Kennen 23
        [1, 20], #KhaZix 24
        [8, 18], #Kindred 25
        [5, 15], #Leona 26
        [4, 13], #Lissandra 27
        [6, 15], #Lucian 28
        [10, 21], #Lulu 29
        [6, 17], #MissFortune 30
        [7, 18], #Mordekaiser 31
        [10, 11], #Morgana 32
        [9, 19], #Nidalee 33
        [7, 21], #Poppy 34
        [1, 17], #Pyke 35
        [2, 20], #RekSai 36
        [1, 19], #Rengar 37
        [7, 13], #Sejuani 38
        [2, 16], #Shen 39
        [9, 12], #Shyvana 40
        [9, 11, 14], #Swain 41
        [6, 21], #Tristana 42
        [8, 11], #Varus 43
        [8, 15], #Vayne 44
        [10, 21], #Veigar 45
        [3, 13], #Volibear 46
        [3, 19], #Warwick 47
        [2], #Yasuo 48
        [1, 16] #Zed 49
        ]

numToName = {
        0: {'name': 'Aatrox', 'cost': 3},
        1: {'name': 'Ahri', 'cost': 2},
        2: {'name': 'Akali', 'cost': 4},
        3: {'name': 'Anivia', 'cost': 5},
        4: {'name': 'Ashe', 'cost': 3},
        5: {'name': 'Aurelion', 'cost': 4},
        6: {'name': 'Blitzcrank', 'cost': 2},
        7: {'name': 'Brand', 'cost': 4},
        8: {'name': 'Braum', 'cost': 2},
        9: {'name': 'ChoGath', 'cost': 3},
        10: {'name': 'Darius', 'cost': 2},
        11: {'name': 'Draven', 'cost': 4},
        12: {'name': 'Elise', 'cost': 2},
        13: {'name': 'Evelynn', 'cost': 3},
        14: {'name': 'Fiora', 'cost': 1},
        15: {'name': 'Gangplank', 'cost': 3},
        16: {'name': 'Garen', 'cost': 1},
        17: {'name': 'Gnar', 'cost': 4},
        18: {'name': 'Graves', 'cost': 1},
        19: {'name': 'Karthus', 'cost': 5},
        20: {'name': 'Kassadin', 'cost': 1},
        21: {'name': 'Katarina', 'cost': 3},
        22: {'name': 'Kayle', 'cost': 5},
        23: {'name': 'Kennen', 'cost': 3},
        24: {'name': 'KhaZix', 'cost': 1},
        25: {'name': 'Kindred', 'cost': 4},
        26: {'name': 'Leona', 'cost': 4},
        27: {'name': 'Lissandra', 'cost': 2},
        28: {'name': 'Lucian', 'cost': 2},
        29: {'name': 'Lulu', 'cost': 2},
        30: {'name': 'MissFortune', 'cost': 5},
        31: {'name': 'Mordekaiser', 'cost': 1},
        32: {'name': 'Morgana', 'cost': 3},
        33: {'name': 'Nidalee', 'cost': 1},
        34: {'name': 'Poppy', 'cost': 3},
        35: {'name': 'Pyke', 'cost': 2},
        36: {'name': 'RekSai', 'cost': 2},
        37: {'name': 'Rengar', 'cost': 3},
        38: {'name': 'Sejuani', 'cost': 4},
        39: {'name': 'Shen', 'cost': 2},
        40: {'name': 'Shyvana', 'cost': 3},
        41: {'name': 'Swain', 'cost': 5},
        42: {'name': 'Tristana', 'cost': 1},
        43: {'name': 'Varus', 'cost': 2},
        44: {'name': 'Vayne', 'cost': 1},
        45: {'name': 'Veigar', 'cost': 3},
        46: {'name': 'Volibear', 'cost': 3},
        47: {'name': 'Warwick', 'cost': 1},
        48: {'name': 'Yasuo', 'cost': 5},
        49: {'name': 'Zed', 'cost': 2}
        }

classThresholds = {
        1: [3, 6],
        2: [3, 6],
        3: [2, 4],
        4: [3],
        5: [2],
        6: [2, 4],
        7: [2, 4, 6],
        8: [2, 4],
        9: [3],
        10: [3, 6],
        11: [2, 4, 6],
        12: [2],
        13: [2, 4, 6],
        14: [2, 4],
        15: [3, 6],
        16: [1, 4],
        17: [3],
        18: [2],
        19: [2, 4],
        20: [3],
        21: [3, 6],
        }