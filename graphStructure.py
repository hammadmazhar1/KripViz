from tkinter import *
from tkinter import font
from graphviz import Digraph
class KripkeFrame:

    def __init__(self, states):
        #list of states(strings) in the frame
        self.states = states
        
        #dictionary, where keys are the formulas and values are lists containing states where formulas are true
        #e.g
        # {'f1' : [ 's1', 's3' ] , 'f2' : ['s2', 's4' ] , 'f3' : ['s6' ] }
        self.formulas = {}
        
        #adjacency list, with each programName as key and a list (of edges as tuples).
        #e.g
        #{ "prog1" : [(startState0, endState0), (startState1, endState1)], "prog2" : [ (startState0) , (endState0) ] } 
        self.programs = {}
        self.graph = None


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
                self.programs[programName] = [(state1, state2)]
            else:
                if (state1, state2) in self.programs[programName]:
                    return
                else:
                    self.programs[programName].append( (state1, state2))
        elif state1 is None and state2 is None:
            if programName not in self.programs:
                self.programs[programName] = []
            else:
                raise ValueError("This program is already in the frame")
        else:
            raise ValueError("Enter start state and end state (Both or None) ")
        
    def __repr__(self):
        return "<states: {}> , formulas: {} , programs: {} ".format(self.states, self.formulas, self.programs)



def genFrame(kripkeFrame):
    kripkeFrame.graph = Digraph('curGraph',format='gif')
    for state in kripkeFrame.states:
        formula_string = '';
        for formula_name in kripkeFrame.formulas.keys():
            state_list = kripkeFrame.formulas[formula_name]
            if state in state_list:
                formula_string = formula_string+formula_name+','
        kripkeFrame.graph.node(state,'%s \n %s'%(state,'{'+formula_string+'}'))
    for program in kripkeFrame.programs.keys():
        program_edges = kripkeFrame.programs[program]
        for prog_edge in program_edges:
            kripkeFrame.graph.edge(prog_edge[0],prog_edge[1], label=program)
    kripkeFrame.graph.render()



#CALLBACK FUNCTIONS

def initializeNewStructure():
    canvas.delete('all')
    #read all entry boxes
    
    states = statesEntry.get().split()

    formula1Name = formulaEntry.get().strip()
    formula1States = formulaStateEntry.get().split()

    formula2Name = formula2Entry.get().strip()
    formula2States = formula2StateEntry.get().split()

    formula3Name = formula3Entry.get().strip()
    formula3States = formula3StateEntry.get().split()

    program1Name = programNameEntry.get().strip()
    program1State1 = programState1Entry.get().strip()
    program1State2 = programState2Entry.get().strip()

    program2Name = program2NameEntry.get().strip()
    program2State1 = program2State1Entry.get().strip()
    program2State2 = program2State2Entry.get().strip()

    program3Name = program3NameEntry.get().strip()
    program3State1 = program3State1Entry.get().strip()
    program3State2 = program3State2Entry.get().strip()

    program4Name = program4NameEntry.get().strip()
    program4State1 = program4State1Entry.get().strip()
    program4State2 = program4State2Entry.get().strip()

    formed_frame = KripkeFrame(states)
    if formula1Name:
        formed_frame.addFormula(formula1Name, formula1States)
    if formula2Name:
        formed_frame.addFormula(formula2Name, formula2States)
    if formula3Name:
        formed_frame.addFormula(formula3Name, formula3States)
    if program1Name:
        formed_frame.addProgram(program1Name, program1State1, program1State2)
    if program2Name:
        formed_frame.addProgram(program2Name, program2State1, program2State2)
    if program3Name:
        formed_frame.addProgram(program3Name, program3State1, program3State2)
    if program4Name:
        formed_frame.addProgram(program4Name, program4State1, program4State2)
    print(formed_frame)

    #make dot file for this frame
    genFrame(formed_frame)

    #display formed file on canvas
    try:
        gif1 = PhotoImage(file='curGraph.gv.gif')
        canvas.create_image(0,0,image=gif1, anchor=NW)
    except:
        gif1 = PhotoImage(file='curGraph.gv.gif')
        canvas.create_image(0,0,image=gif1, anchor=NW)
    mainloop()


def addNewFormula():
    pass

def addNewProg():
    pass

def createGUI():
    global rootWindow
    global canvas
    global statesEntry
    global formulaEntry
    global formulaStateEntry
    global formula2Entry
    global formula2StateEntry
    global formula3Entry
    global formula3StateEntry
    global programNameEntry
    global programState1Entry
    global programState2Entry
    global program2NameEntry
    global program2State1Entry
    global program2State2Entry
    global program3NameEntry
    global program3State1Entry
    global program3State2Entry
    global program4NameEntry
    global program4State1Entry
    global program4State2Entry


    #maxBallSize = 50


    playerWin = 0
    computerWin = 0
    rootWindow = Tk()
    rootWindow.configure(background='white')
    rootWindow.title("Build Kripke Frames")
    
    canvasAndGUI = Frame(rootWindow)
    canvasAndGUI.configure(background='#ADD8E6')


    
    canvasHeight = 620
    canvasWidth = 620
    canvasBorderBuffer = 10
    canvas = Canvas(canvasAndGUI, height=canvasHeight, width=canvasWidth, relief=SUNKEN, borderwidth=2)
    canvas.pack(side=LEFT)
    # gif1 = PhotoImage(file='test2.gif')
    # canvas.create_image(0,0,image=gif1, anchor=NW)


    guiFrame = Frame(canvasAndGUI)
    wonBoardLabel = Label(guiFrame, text='Enter Details',width= 50, height = 4)
    wonBoardLabel.pack()

   
    kripkeStatesDetails = Frame(guiFrame)
    stateLabel = Label(kripkeStatesDetails, text='States:',width= 8, height = 3)
    statesEntry = Entry(kripkeStatesDetails)
    stateLabel.pack(side=LEFT)
    statesEntry.pack(side=LEFT)
       
    KripkeFormula1Frame = Frame(guiFrame)
    formulaLabel = Label(KripkeFormula1Frame, text='Formula:',width= 9)
    formulaEntry = Entry(KripkeFormula1Frame,width= 4)
    formulaStateLabel = Label(KripkeFormula1Frame, text='True in states:',width= 12)
    formulaStateEntry = Entry(KripkeFormula1Frame,width= 10)
    formulaLabel.pack(side=LEFT)
    formulaEntry.pack(side = LEFT)
    formulaStateLabel.pack(side = LEFT,pady = 5)
    formulaStateEntry.pack(side = LEFT)

    KripkeFormula2Frame = Frame(guiFrame)
    formula2Label = Label(KripkeFormula2Frame, text='Formula:',width= 9)
    formula2Entry = Entry(KripkeFormula2Frame,width= 4)
    formula2StateLabel = Label(KripkeFormula2Frame, text='True in states:',width= 12)
    formula2StateEntry = Entry(KripkeFormula2Frame,width= 10)
    formula2Label.pack(side=LEFT)
    formula2Entry.pack(side = LEFT)
    formula2StateLabel.pack(side = LEFT, pady = 5)
    formula2StateEntry.pack(side = LEFT)

    
    KripkeFormula3Frame = Frame(guiFrame)
    formula3Label = Label(KripkeFormula3Frame, text='Formula:',width= 9)
    formula3Entry = Entry(KripkeFormula3Frame,width= 4)
    formula3StateLabel = Label(KripkeFormula3Frame, text='True in states:',width= 12)
    formula3StateEntry = Entry(KripkeFormula3Frame,width= 10)
    formula3Label.pack(side=LEFT)
    formula3Entry.pack(side = LEFT)
    formula3StateLabel.pack(side = LEFT, pady = 5)
    formula3StateEntry.pack(side = LEFT)

    forButtonFrame = Frame(guiFrame)
    createForButton = Button(forButtonFrame, text='Add Another Formula', command=addNewFormula)
    createForButton.pack()

    KripkeProgram1Frame = Frame(guiFrame)
    programNameLabel = Label(KripkeProgram1Frame, text='Program:', width= 8)
    programNameEntry = Entry(KripkeProgram1Frame,width= 4)
    programState1Label = Label(KripkeProgram1Frame, text='goes from state: ', width= 14)
    programState1Entry =  Entry(KripkeProgram1Frame,width= 4)
    programState2Label = Label(KripkeProgram1Frame, text='to state: ', width= 8)
    programState2Entry =  Entry(KripkeProgram1Frame,width= 4)
    programNameLabel.pack(side=LEFT, pady = 5)
    programNameEntry.pack(side = LEFT)
    programState1Label.pack(side = LEFT)
    programState1Entry.pack(side = LEFT)
    programState2Label.pack(side = LEFT)
    programState2Entry.pack(side = LEFT)

   

    KripkeProgram2Frame = Frame(guiFrame)
    program2NameLabel = Label(KripkeProgram2Frame, text='Program:', width= 8)
    program2NameEntry = Entry(KripkeProgram2Frame,width= 4)
    program2State1Label = Label(KripkeProgram2Frame, text='goes from state: ', width= 14)
    program2State1Entry =  Entry(KripkeProgram2Frame,width= 4)
    program2State2Label = Label(KripkeProgram2Frame, text='to state: ', width= 8)
    program2State2Entry =  Entry(KripkeProgram2Frame,width= 4)
    program2NameLabel.pack(side=LEFT, pady = 5)
    program2NameEntry.pack(side = LEFT)
    program2State1Label.pack(side = LEFT)
    program2State1Entry.pack(side = LEFT)
    program2State2Label.pack(side = LEFT)
    program2State2Entry.pack(side = LEFT)

    KripkeProgram3Frame = Frame(guiFrame)
    program3NameLabel = Label(KripkeProgram3Frame, text='Program:', width= 8)
    program3NameEntry = Entry(KripkeProgram3Frame,width= 4)
    program3State1Label = Label(KripkeProgram3Frame, text='goes from state: ', width= 14)
    program3State1Entry =  Entry(KripkeProgram3Frame,width= 4)
    program3State2Label = Label(KripkeProgram3Frame, text='to state: ', width= 8)
    program3State2Entry =  Entry(KripkeProgram3Frame,width= 4)
    program3NameLabel.pack(side=LEFT,pady = 5)
    program3NameEntry.pack(side = LEFT)
    program3State1Label.pack(side = LEFT)
    program3State1Entry.pack(side = LEFT)
    program3State2Label.pack(side = LEFT)
    program3State2Entry.pack(side = LEFT)


    KripkeProgram4Frame = Frame(guiFrame)
    program4NameLabel = Label(KripkeProgram4Frame, text='Program:', width= 8)
    program4NameEntry = Entry(KripkeProgram4Frame,width= 4)
    program4State1Label = Label(KripkeProgram4Frame, text='goes from state: ', width= 14)
    program4State1Entry =  Entry(KripkeProgram4Frame,width= 4)
    program4State2Label = Label(KripkeProgram4Frame, text='to state: ', width= 8)
    program4State2Entry =  Entry(KripkeProgram4Frame,width= 4)
    program4NameLabel.pack(side=LEFT, pady = 5)
    program4NameEntry.pack(side = LEFT)
    program4State1Label.pack(side = LEFT)
    program4State1Entry.pack(side = LEFT)
    program4State2Label.pack(side = LEFT)
    program4State2Entry.pack(side = LEFT)
    #execButton = Button(guiFrame, text='Do it!', command=executePlayerMove)

    progButtonFrame = Frame(guiFrame)
    createProgButton = Button(progButtonFrame, text='Add Another Program', command=addNewProg)
    createProgButton.pack()

    boldFont = font.Font(size = 10, weight = "bold")
    createFrameButton = Button(guiFrame, text='Create Frame', command=initializeNewStructure, background = 'green', font = boldFont)

    # replace the widget below with an Entry widget
    #newHeapLabel = Label(guiFrame, text='New Frame')   
    #newHeapEntry = Entry(guiFrame)
    

    kripkeStatesDetails.pack()

    
    KripkeFormula1Frame.pack()
    KripkeFormula2Frame.pack()
    KripkeFormula3Frame.pack()
    #KripkeFormula4Frame.pack()

    forButtonFrame.pack(pady = 6)
    
    KripkeProgram1Frame.pack()
    KripkeProgram2Frame.pack()
    KripkeProgram3Frame.pack()
    KripkeProgram4Frame.pack()

    progButtonFrame.pack(pady = 10)
    createFrameButton.pack(pady = 15)
    
   
    guiFrame.pack(side=RIGHT)
    canvasAndGUI.pack()


    mainloop()

    

def runGUI():
    createGUI()
    rootWindow.mainloop()


runGUI()
