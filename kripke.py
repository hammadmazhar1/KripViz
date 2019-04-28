## kripke.py - Defines classes and methods for creating and modifying
## Kripke structures and evaluating Positional Dynamic Logic on
## such structures
import re
necessityPattern = re.compile('\[*\]*')
conditionalPattern = re.compile('\<*\>*')
class KripFrame:
	def __init__(self,states,formulas,programs):
		self.states = {}
		for state in states:
			self.states[state.name] = state
		self.formulas = {}
		for formula in formulas:
			self.formulas[formula.name] = formula
		self.programs = {}
		for program in programs:
			self.programs[program.name] = program
	def evalPDL(self,pdlString):
		pdlSides=  pdlString.split('->')
		if len(pdlSides) == 2:
			leftSide = pdlSides[0]
			rightSide = pdlSides[1]

		else:
			leftsSide = pdlSides[0]

class Formula:
	def __init__(self,form_string,states):
		# name of the formula
		if isinstance(form_string,str):
			self.name = form_string
		## list of states that lie in the formula
		if isinstance(states,list):
			self.states = states
		## single state only
		elif isinstance(states,str):
			self.states = [states]
class Program:
	def __init__(self,prog_string,prog_set):
		# name of the program
		self.name = prog_string
		# set of transitions
		if isinstance(prog_set,list):
			prog_set = set(prog_set)
		self.transition_set = prog_set 
class State:
 	def __init__(self, state_string):
 		if isinstance(state_string,str):
 			self.name = state_string
 		else:
 			self.name = str(state_string)
 		 
