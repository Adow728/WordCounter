# WordCounter

### This Program finds the books, chapters, or verses with the most or least chapters, verses, words, or characters.

It uses five files:

main.py: starts the program gui
gui.py: creates a gui and handles user input, calling algorithom.py for result handling
algorithom.py: takes the mode and handles the results
files.py: generates a data structure of blocks(Verses, Chapters, and Books, and one general Bible, all inheriting from the general Block Class) from files
blocks.py: a set of nesting block classes for segmenting the data into titled chunks
