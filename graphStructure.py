from tkinter import Tk, Canvas, Frame, Button, Label, Entry, END, LEFT, RIGHT, SUNKEN

class KripkeFrame:

    def __init__(self, states, formulas, programs):
        #list of states(strings) in the frame
        self.states = []
        
        #dictionary, where keys are the formulas and values are lists containing states where formulas are true
        #e.g
        # {'f1' : [ 's1', 's3' ] , 'f2' : ['s2', 's4' ] , 'f3' : ['s6' ] }
        self.formulas = {}
        
        #adjacency list, with each programName as key and a list (of edges as tuples).
        #e.g
        #{ "prog1" : [(startState0, endState0), (startState1, endState1)], "prog2" : [ (startState0) , (endState0) ] } 
        self.programs = {}


    def addState(self, state):
        if state in self.states:
            raise ValueError("state is already in the frame")
        else:
            self.states.append(state)

    def addFormula(self, formulaName, statesInFormula):
        if formulaName in self.formulas:
            if statesInFormula in self.formulas[formulaName]:
                raise ValueError("These states are already in the formula")
            else:
                #add the newly entered states to previous states in the formula without duplication
                self.formulas[formulaName] = list(set().union(self.formulas[formulaName], statesInFormula))
        else:
            self.formulas[formulaName] = statesInFormula

    def addProgram(self, programName, state1 = None, state2 = None):
        if state1 is not None and state2 is not None:
            if programName not in self.programs:
                self.programs[programName] = (state1, state2)
            else:
                if (state1, state2) in self.programs[programName]:
                    raise ValueError("This edge is already in the frame")
                else:
                    self.programs[programName].append( (state1, state2))
        elif state1 is None and state2 is None:
            if programName not in self.programs:
                self.programs[programName] = []
            else:
                raise ValueError("This program is already in the frame")
        else:
            raise ValueError("Enter start state and end state (Both or None) ")


def genFrame():
    pass


def initializeNewStructure():
    pass


def createGUI():
    global rootWindow
    global canvas
    global statusLabel
    global whichHeapEntry
    global numBallsEntry
    global newHeapEntry
    global playerWin
    global computerWin
    global wonBoardLabel


    canvasHeight = 620
    canvasWidth = 750
    canvasBorderBuffer = 10
    maxBallSize = 50


    playerWin = 0
    computerWin = 0
    rootWindow = Tk()
    rootWindow.configure(background='blue')
    rootWindow.title("Build Kripke Frames")
    
    canvasAndGUI = Frame(rootWindow)
    canvasAndGUI.configure(background='green')
    canvas = Canvas(canvasAndGUI, height=canvasHeight, width=canvasWidth, relief=SUNKEN, borderwidth=2)
    canvas.pack(side=LEFT)


    guiFrame = Frame(canvasAndGUI)
    wonBoardLabel = Label(guiFrame, text='Enter Details')
    wonBoardLabel.pack()

    kripkeStatesDetails = Frame(guiFrame)
    stateLabel = Label(kripkeStatesDetails, text='States:')
    statesEntry = Entry(kripkeStatesDetails)
    stateLabel.pack(side=LEFT)
    statesEntry.pack(side=LEFT)
       
    KripkeFormulasFrame = Frame(guiFrame)
    formulaLabel = Label(KripkeFormulasFrame, text='Formulas:')
    formulaEntry = Entry(KripkeFormulasFrame)
    formulaLabel.pack(side=LEFT)
    formulaEntry.pack(side = LEFT)

    KripkeProgramsFrame = Frame(guiFrame)
    programLabel = Label(KripkeProgramsFrame, text='Programs:')
    programEntry = Entry(KripkeProgramsFrame)
    programLabel.pack(side=LEFT)
    programEntry.pack(side = LEFT)
    

    #execButton = Button(guiFrame, text='Do it!', command=executePlayerMove)


    newGameButton = Button(guiFrame, text='Create Frame', command=initializeNewStructure)

    # replace the widget below with an Entry widget
    #newHeapLabel = Label(guiFrame, text='New Frame')
    #newHeapEntry = Entry(guiFrame)


    

    kripkeStatesDetails.pack()
    KripkeFormulasFrame.pack()
    KripkeProgramsFrame.pack()
    
    #execButton.pack()
    #newHeapLabel.pack(side=LEFT)
    #newHeapEntry.pack()
    newGameButton.pack()
    guiFrame.pack(side=RIGHT)
    canvasAndGUI.pack()
    statusLabel = Label(rootWindow)
    statusLabel.pack()
