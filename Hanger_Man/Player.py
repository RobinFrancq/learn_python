class Player:
    
    def __init__(self, word):
        self.word = word.upper()
        self.wordLst = self.convertWordIntoLetterList(self.word)
        self.boolLst = self.makeDefaultBoolLst(self.word)
        self.state = 10
        
    def convertWordIntoLetterList(self, word):

        lst = []
        
        for char in word:
            lst.append(char)
        
        return lst
    
    def makeDefaultBoolLst(self, word):
        lst = []
        count = 0
        
        while count<len(word):
            lst.append(False)
            count += 1
        
        return lst
    
    def displayPlayerStatusAndUpdateState(self):  

        if self.state == 10:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *   ______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display
        
        elif self.state == 9:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *                   * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display
            
        elif self.state == 8:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *  -------------    * \n"
            display +=  " *  |/               * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display
        
        elif self.state == 7:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *  -------------    * \n"
            display +=  " *  |/        |      * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display
            
        elif self.state == 6:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *  -------------    * \n"
            display +=  " *  |/        |      * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |        ( )     * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display
            
        elif self.state == 5:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *  -------------    * \n"
            display +=  " *  |/        |      * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |        ( )     * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display
            
        elif self.state == 4:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *  -------------    * \n"
            display +=  " *  |/        |      * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |        ( )     * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |     \   |      * \n"
            display +=  " *  |      *--|      * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display
            
        elif self.state == 3:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *  -------------    * \n"
            display +=  " *  |/        |      * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |        ( )     * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |     \   |   /  * \n"
            display +=  " *  |      *--|--*   * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |                * \n"
            display +=  " *  |                * \n"
            display +=  " *  |______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display
            
        elif self.state == 2:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *  -------------    * \n"
            display +=  " *  |/        |      * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |        ( )     * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |     \   |   /  * \n"
            display +=  " *  |      *--|--*   * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |        /       * \n"
            display +=  " *  |       /        * \n"
            display +=  " *  |______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display
            
        elif self.state == 1:
            display =   "\n"
            display +=  " --------STATE-------- \n"
            display +=  " ********************* \n"
            display +=  " *                   * \n"
            display +=  " *  -------------    * \n"
            display +=  " *  |/        |      * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |        ( )     * \n"
            display +=  " *  |        *-*     * \n"
            display +=  " *  |     \   |   /  * \n"
            display +=  " *  |      *--|--*   * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |         |      * \n"
            display +=  " *  |        / \     * \n"
            display +=  " *  |       /   \    * \n"
            display +=  " *  |______________  * \n"
            display +=  " *                   * \n"
            display +=  " ********************* \n"
            display +=  "    " +str(self.state-1)+ " GUESSES LEFT"
            display +=  "\n"
            self.state -= 1
            return display

    def displayWordStatus(self):
    
        display = ""
        wordLen = len(self.wordLst)
        
        for i in range (0, wordLen):
            if self.boolLst[i] == True:
                display += self.wordLst[i]
            else:
                display += " "
            display += "  "
        
        display += "\n"
        
        for i in range (0, wordLen):
            display += "-  "
        
        return display            
    
    def checkIfLetterIsInWordAndUpdate(self, char):
        
        tempChar = char.upper()
        tempBool = False
        
        for i in range(0, len(self.wordLst)):
            if self.wordLst[i] == tempChar:
                self.boolLst[i] = True
                tempBool = True
        
        if tempBool == False:
            print(self.displayPlayerStatusAndUpdateState())
        
        return tempBool
    
    def checkIfWordIsFound(self):
        if False in self.boolLst:
            return False
        else: return True