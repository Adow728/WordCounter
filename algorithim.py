from files import BIBLE
from blocks import *
def handleResults(findLevel, sortLevel):
    sortLevel = sortLevel.split("\n")

    do_invert = sortLevel[0]
    if do_invert == "Most":
        do_invert = True
    elif do_invert == "Least":
        do_invert = False
    else: 
        raise ValueError(f"Got {do_invert}, expected Least or Most")

    sortLevel = sortLevel[1] 
    findLevel = findLevel[:-1]

    sortClass = eval(findLevel)
    to_sort = BIBLE.getSubLevel(sortClass)
     

    if sortLevel == "Characters":
        myKey = sortClass.charCount
    elif sortLevel == "Words":
        myKey = sortClass.wordCount
    elif sortLevel == "Verses":
        myKey = mostVerses
    elif sortLevel == "Chapters":
        myKey = mostChapters
        
    to_sort.sort(key=myKey)

    if do_invert:
        to_sort.reverse()
    
    results = []
    for best in to_sort[0:5]:
        results.append(best.title + " - " + str(myKey(best)))

    return results

def mostChapters(arg):
    return len(arg.getSubLevel(Chapter))

def mostVerses(arg):
    return len(arg.getSubLevel(Verse))
    

