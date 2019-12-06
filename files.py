import blocks, os

def buildBible(dataDir):
	print("Building Bible")
	books = []
	for book in os.listdir(dataDir):
		print("Building", book)
		books.append(buildBook(dataDir + "/" + book))

	return blocks.Bible("Bible", books)

def buildBook(bookDir):
	
	chapters = []
	for chapter in os.listdir(bookDir):
		chapters.append(buildChapter(bookDir + "/" + chapter))

	bookName = bookDir.split("/")[-1]
	
	return blocks.Book(bookName, chapters)

def buildChapter(chapterFile):
	# Creating "Genesis 3 from $PATH/Genesis3.txt"
	chapterName = buildName(chapterFile)
	print("Building", chapterName)
	with open(chapterFile) as chapter:
		content = chapter.readlines()
	verses = splitVerses(chapterName, content)
	return blocks.Chapter(chapterName, verses)

def buildName(chapterFile):
	pathList = chapterFile.split("/")
	bookName = pathList[-2]
	chapterName = pathList[-1][:-4]
	chapterName = list(chapterName)
	chapterName.insert(len(bookName), " ")
	return "".join(chapterName)
	
def splitVerses(chapter, content):
	verses = []
	for line in content:
		verseTitle = chapter + ":" + line.split()[0]
		text = " ".join(line.split()[1:])
		verses.append(blocks.Verse(verseTitle, text))
	return verses

BIBLE = buildBible("/home/aidenrd/Desktop/Coding/Python/WordCounter/data")