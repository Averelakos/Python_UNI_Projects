
##############################################3
#   Author  :     I.Tsikas,P.Doulgeridis
#   Function: Parses a text by all possible triplets
#             then combines them to create a new text.
#   Usage   : python pyParseBy3.py <file_input> <file_output>
#             <file_input> : Input file
#             <file_output>: Name of output file
#
#   Notes   : <file_output> will be generated in the same directory
#              as input file.   
#

# Stack Automaton
# Calculates whether an expression is syntactically correct, based 
# on the parentheses problem, which can be proven that cannot be solved
# with a dfa but requires a stack automaton. Some basic test cases for the
# problem are:


# Input	        Output	Comment
# ''	        true	the empty string is balanced
# '()'	        true	 
# '(())'	    true	parentheses can nest
# '()()'	    true	multiple pairs are acceptable
# '(()()())()'	true	multiple pairs can nest
# '((()'	    false	missing closing parentheses
# '()))'	    false	missing opening parentheses
# ')('	        false	close before open


# This problem is part of a class of problems that all have the same basic form:

#   - We have a language, by which we mean, we have a set of strings. 
#   - Each string must be finite in length, although the set itself may have infinitely many members.
#   - We wish to construct a program that can “recognize” (sometimes called “accept”) strings 
#   - that are members of the language, while rejecting strings that are not.
#   - The “recognizer” is constrained to consume the symbols of each string one at a time.


# Pushdown Automata is a finite automata with extra memory called stack which helps Pushdown automata to recognize Context Free Languages.
 
# A Pushdown Automata (PDA) can be defined as :

# Q is the set of states
# ∑is the set of input symbols
# Γ is the set of pushdown symbols (which can be pushed and popped from stack)
# q0 is the initial state
# Z is the initial pushdown symbol (which is initially present in stack)
# F is the set of final states
# δ is a transition function


# In our example: 
#
#   Left Parenthesis    : D   (P.Doulgeridis)
#   Right Parenthesis   : T   (I.Tsikas)

import json
import sys

stack = []
eos   = ';'

def push_stack(item):
    '''
    Function: push_stack(item)
    Input: <datatype>
    Output: Null
    Usage: push_stack(1)
    Notes: Edits stack in place, by reference, pushes a value at 
    the top of the stack. One of the basic functions that every
    stack has to implement.
    '''
    global stack
    stack.append(item)
    
def pop_stack():
    '''
    Function: pop_stack()
    Input: <none>
    Output: <none>
    Usage: pop_stack() or a=pop_stack()
    Notes: Pops the first element out of the stack, and returns the value.
    One of the basic functions that every stack has to implement.
    '''
    global stack
    return_value = stack.pop()
    return return_value
    
def display_stack():
    '''
    Function: display_stack
    Input:
    Output:
    Usage:
    Notes:
    '''
    global stack
    print(json.dumps(stack, indent=5))


def peek_stack():
    '''
    Function:
    Input:
    Output:
    Usage:
    Notes:
    '''
    global stack
    print(stack[0])
    pass


def get_expression():
    '''
    Function: 
    Input:
    Output:
    Usage:
    Notes:
    '''
    expression = input("Enter expression (Only 'D' or 'T' ) : ")
    print("Provided expression: {0}".format(expression))
    return expression
    
def end_of_statement(input_in):
    '''
    Function: 
    Input:
    Output:
    Usage:
    Notes:
    '''
    global eos
    if input_in == eos:
        print("End of input reached")
        
        
def main_proc():
    '''
    Function: 
    Input:
    Output:
    Usage:
    Notes:
    '''
    print("Displaying initial stack:")
    display_stack()
    
    print("Populating with initial element -> V")
    push_stack('V')
    
    print("Displaying initialized stack")
    display_stack()


    user_input = get_expression()
    print("Parsing expression: [ {0} ]".format(user_input))
    
    index_in = 0
    flag = False
    
    if user_input == '':
        print("Syntactically correct")
        return 0
    else:
   
        for character in user_input:
        
            print("Read character: {0}".format(character))
            x = input("pause")
            print("Flag: {0}".format(flag))
            if character not in [ 'D', 'T', ';' ]:
                print("Illegal character encountered at index: {0}".format(index_in))
                flag = False
                sys.exit(1)
            else:
                if character == 'D':
                    print("Encountered left parenthesis (D): {0}".format(character))
                    print("Adding to stack, and displaying...")
                    push_stack("I")
                    display_stack()
                elif character == 'T':
                    print("Encountered right parenthesis (T): {0}".format(character))
                    if len(stack) == 1:
                        print("Stack is initial. Nothing to remove. Unmatched right parenthesis (T) at index {0}".format(index_in))
                        print("Process result: Not syntactically correct")
                        sys.exit(1)
                        flag = False
                    
                    
                    print("Popping top I from stack:")
                    element = pop_stack()
                    print("Element {0} removed from stack, displaying stack: ".format(element))
                    display_stack()
    
            index_in += 1


            
    #print("Reached command separator: {0}".format(character))
    print("Displaying current stack: ")
    display_stack()
    if stack[0] == 'V' and len(stack) == 1:
        print("Stack is initial, only one element: {0}".format(stack[0]))
        flag = True
    else:
        print("Stack is not initial. Unmatched left parenthesis (D)")
        flag = False
            
    
    
    if flag == False:
        print("Process result: Not syntactically correct")
    else:
        print("Process result: Syntactically correct")
    
    
if __name__ == '__main__':
    main_proc()