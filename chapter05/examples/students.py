import random
import math


dorms = ['Hammerschlag', 'Donner', 'Gardens', 'E-Tower', 'Stever', 'Resnik', 'McGill', 'Mudge']

prefs = ['Ryan', ('Gardens', 'Mudge', 'E-Tower'), 'James', ('Mudge', 'Gardens', 'Stever'), 'Steve', ('Stever', 'Mudge', 'Gardens'), 'Alex', ('Hammerschlag', 'Donner', 'Gardens'), 'Reuben', ('Donner', 'Mudge', 'Gardens'), 'Fred', ('Gardens', 'E-Tower', 'Mudge'), 'Sarah', ('Gardens', 'E-Tower', 'Mudge'), 'Karen', ('Gardens', 'E-Tower', 'Mudge'), 'Kelly', ('Gardens', 'E-Tower', 'Mudge'), 'Sophia', ('Gardens', 'E-Tower', 'Mudge'), 'Kim', ('Gardens', 'E-Tower', 'Mudge'), 'Joe', ('Gardens', 'E-Tower', 'Mudge')]

studpref = ['Ryan', ('James', 'Steve'), 'James', ('Steve', 'Ryan'), 'Steve', ('James', 'Alex'), 'Kelly', ('Kim', 'Sarah'), 'Fred', ('Reuben', 'Alex'), 'Sarah', ('Kelly', 'Kim'), 'Joe', ('Fred', 'Ryan'), 'Karen', ('Sarah', 'Kelly'), 'Sophia', ('Sarah', 'Karen'), 'Alex', ('Steve', 'Fred'), 'Patrick', ('Terrence','Ryan'), 'Terrence', ('David', 'Patrick')]

students = ['Ryan', 'James', 'Steve', 'Kelly', 'Fred', 'Sarah', 'Joe', 'Karen', 'Sophia', 'Alex', 'Patrick', 'Terrence']

def assignmentcost(vec):
    cost = 0 
    slots = [0,1,2,3,4,5]
    
    for i in range(len(vec)):
        x=int(vec[i])
        student=students[slots[x]]
        pref=studpref[i][1]
        # First choice costs 0, second choice costs 3
        if pref[0]==student: 
            cost = cost
            
        elif pref[1]==student: 
            cost = cost + 3
            
        else: cost = cost + 5
            
        # Not on the list costs 5

        # Remove selected slot
        del slots[x]
    
    return cost




def printsolution(vec):
    slots=[]
    # Create two slots for each dorm
    for i in range(len(students) / 2): slots+=[i,i]

    # Loop over each students assignment
    for i in range(len(vec)):
        x=int(vec[i])

        # Choose the slot from the remaining ones
        student=studpref[slots[x]]
        # Show the student and assigned dorm
        print prefs[i][0],dorm
        # Remove this slot
        del slots[x]
    