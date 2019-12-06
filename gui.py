import graphics as g
from algorithim import handleResults
import time

class MyGUI():
    def __init__(self):
        self.win = g.GraphWin("Longest and Shortest in the Bible", 600, 600)
        self.win.setCoords(1, 15, 14, 0)

        self.quitButton = g.Button("Quit", g.Point(2, 1), g.Point(7, 2))
        self.quitButton.activate()
        self.quitButton.draw(self.win)
        self.mainButton = g.Button("Main Menu", g.Point(8, 1), g.Point(13, 2))
        self.mainButton.activate()
        self.mainButton.draw(self.win)

        self.introText = g.Text(g.Point(7.5, 3), "Bible Counter")
        self.introText.setStyle("bold")
        self.introText.draw(self.win)
        text1 = g.Text(g.Point(7.5, 4), "Welcome")
        text2 = g.Text(g.Point(7.5, 5), "This program finds the chapter, book, or verse")
        text3 = g.Text(g.Point(7.5, 6), "With the most or least chapters, words, characters, or verses")
        text4 = g.Text(g.Point(7.5, 7), "")
        text5 = g.Text(g.Point(7.5, 8), "")

        self.textboxes = [text1, text2, text3, text4, text5]
        for x in self.textboxes:
            time.sleep(1)
            x.draw(self.win)
        time.sleep(1)

        self.verseButton = g.Button("Verses", g.Point(2, 9), g.Point(5, 10))
        self.verseButton.draw(self.win)

        self.chapterButton = g.Button("Chapters", g.Point(6, 9), g.Point(9, 10))
        self.chapterButton.draw(self.win)

        self.bookButton = g.Button("Books", g.Point(10, 9), g.Point(13, 10))
        self.bookButton.draw(self.win)

        opt1 = g.Button("Most\nChapters", g.Point(2, 11), g.Point(4, 12))
        opt3 = g.Button("Most\nVerses", g.Point(5, 11), g.Point(7, 12))
        opt5 = g.Button("Most\nWords", g.Point(8, 11), g.Point(10, 12))
        opt7 = g.Button("Most\nCharacters", g.Point(11, 11), g.Point(13, 12))
        opt2 = g.Button("Least\nChapters", g.Point(2, 13), g.Point(4, 14))
        opt4 = g.Button("Least\nVerses", g.Point(5, 13), g.Point(7, 14))
        opt6 = g.Button("Least\nWords", g.Point(8, 13), g.Point(10, 14))
        opt8 = g.Button("Least\nCharacters", g.Point(11, 13), g.Point(13, 14))
        self.options = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8]
        for opt in self.options:
            opt.draw(self.win)

        time.sleep(1)
        self.mainMenu()

    def eraseMessages(self):
        for message in self.textboxes:
            message.setText("")

    def displayResults(self, results):
        self.introText.setText("And the results are: ")
        for i in range(5):
            self.textboxes[i].setText(results[i])

    def beginLoop(self):
        while self.getClick():
            pass


    def getClick(self):
        click = self.win.getMouse()

        if self.mainButton.clicked(click):
            self.mainMenu()

        for x in [self.bookButton, self.chapterButton, self.verseButton]:
            if x.clicked(click):
                self.setMode(x)

        for x in self.options:
            if x.clicked(click):
                self.displayResults(handleResults(self.mode, x.getText()))


        if self.quitButton.clicked(click):
            return False
        else: return True

    def mainMenu(self):
        self.verseButton.activate()
        self.chapterButton.activate()
        self.bookButton.activate()
        self.eraseMessages()
        self.introText.setText("Choose whether you want to find a special chapter, verse or book")

        for opt in self.options:
            opt.deactivate()

    def setMode(self, modeButton):
        self.mode = modeButton.getText()
        self.introText.setText(f"Choose what criteria you want to sort the {self.mode.lower()} by")
        valid = False
        if self.mode == "Books":
            valid = True
        for opt in self.options:
            if valid and not self.mode in opt.getText():
                opt.activate()
            else:
                opt.deactivate()
                if self.mode in opt.getText():
                    valid = True


if __name__ == "__main__":
    MyGUI().beginLoop()