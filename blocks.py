class Block():
    def __init__(self, title, subsections):
        self.title = title
        self.subsections = subsections

    def words(self):
        words = []
        for subsection in self.subsections:
            words += subsection.words()
        
        return words

    def charCount(self):
        charCount = 0
        for subsection in self.subsections:
            charCount += subsection.charCount()
        
        return charCount

    def wordCount(self):
        wordCount = 0
        for subsection in self.subsections:
            wordCount += subsection.wordCount()
        
        return wordCount

    def getSubLevel(self, level):
        if self.__class__ == level:
            return [self]
        else:
            array = []
            for subsection in self.subsections:
                array += subsection.getSubLevel(level)
            return array
    
    def getSubNumber(self):
        return len(self.subsections)
        
    
class Bible(Block):
    pass

class Book(Block):
    pass

class Chapter(Block):
    pass

class Verse(Block):
    def words(self):
        return self.subsections.split()

    def wordCount(self):
        return len(self.subsections.split())

    def charCount(self):
        return len(self.subsections)

    def getSubNumber():
        raise NotImplementedError("Verses do not contain subblocks, only text")
    
