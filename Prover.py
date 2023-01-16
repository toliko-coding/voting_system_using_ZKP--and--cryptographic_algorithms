


class prover:
    confidence = 80
    def __init__(self,val):
        self.confidence = val

    #Create List of all the rows
    def rowsCollector(self,sodoku):
        rows = {}
        for i in range(9):
            rows[i] = sodoku[i]
        return rows



    #Function that take imput from text and Build a list size 9 to org
    def buildTable(self,text,org):
        while len(text) > 0:
            l = []

            # Get a row of numbers
            while len(l) < 9:
                if text[0].isdigit():
                    l.append(int(text[0]))
                text = text[1:]

            # Insert that row into the Sudoku grid
            org.append(l)
            if len(org) == 9:
                break    




    #Create List of all the colums
    def colCollector(self,sodoku):
        cols = ""
        colsList = []
        for i in range(9):
            for j in range(9):
                cols += str(sodoku[j][i])
        
        self.buildTable(cols , colsList)
        return colsList



    #Create List of all the grids[3x3] inside the table
    def gridCollector(self,sodoku):
        gridList = []
        g1 = []
        g2 = []
        g3 = []

        #grids 1 to 3
        for i in range(9):
            if i == 3 or i == 6:

                gridList.append(g1)
                gridList.append(g2)
                gridList.append(g3)

                g1 = []
                g2 = []
                g3 = []
                
            for j in range(9):
                if j < 3:
                    g1.append(sodoku[i][j])

                if j > 2 and j < 6:
                    g2.append(sodoku[i][j])

                if j > 5 :
                    g3.append(sodoku[i][j])


        gridList.append(g1)
        gridList.append(g2)
        gridList.append(g3)

        return gridList            

            


        