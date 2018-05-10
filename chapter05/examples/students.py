import random
import math


dorms = ['Hammerschlag', 'Donner', 'Gardens', 'E-Tower', 'Stever', 'Resnik', 'McGill', 'Mudge']

rooms = ['Room1', 'Room2', 'Room3', 'Room4', 'Room5', 'Room6']

prefs = [('Ryan', ('Gardens', 'Mudge', 'E-Tower')), ('James', ('Mudge', 'Gardens', 'Stever')), ('Steve', ('Stever', 'Mudge', 'Gardens')), ('Alex', ('Hammerschlag', 'Donner', 'Gardens')), ('Reuben', ('Donner', 'Mudge', 'Gardens')), ('Fred', ('Gardens', 'E-Tower', 'Mudge')), ('Sarah', ('Gardens', 'E-Tower', 'Mudge')), ('Karen', ('Gardens', 'E-Tower', 'Mudge')), ('Kelly', ('Gardens', 'E-Tower', 'Mudge')), ('Sophia', ('Gardens', 'E-Tower', 'Mudge')), ('Kim', ('Gardens', 'E-Tower', 'Mudge')), ('Joe', ('Gardens', 'E-Tower', 'Mudge'))]

studpref = [('Ryan', ('James', 'Steve')), ('James', ('Steve', 'Ryan')), ('Steve', ('James', 'Alex')), ('Kelly', ('Kim', 'Sarah')), ('Fred', ('Reuben', 'Alex')), ('Sarah', ('Kelly', 'Kim')), ('Joe', ('Fred', 'Ryan')), ('Karen', ('Sarah', 'Kelly')), ('Sophia', ('Sarah', 'Karen')), ('Alex', ('Steve', 'Fred')), ('Patrick', ('Terrence','Ryan')), ('Terrence', ('David', 'Patrick'))]

students = ['Ryan', 'James', 'Steve', 'Kelly', 'Fred', 'Sarah', 'Joe', 'Karen', 'Sophia', 'Alex', 'Patrick', 'Terrence']

domain = [(0, (len(rooms)*2)-i-1) for i in range(0, len(rooms)*2)]

def roomcost(vec):
    cost = 0 
    slots = [0,0,1,1,2,2,3,3,4,4,5,5]
    assignments = []
    
    for i in range(len(vec)):
        x=int(vec[i])
        room=rooms[slots[x]]
        assignments.append(room)
        #print('Student: ' + studpref[i][0] + '  Room:  ' + room)
        del slots[x]
        
        # First choice costs 0, second choice costs 1
    for i in range(len(vec)):
        student=studpref[i][0]
        #print(' Student: ' + student)
        roomate = find_roomate(assignments, student, assignments[i])
        #print(' Roommate: ' + roomate)
        #print(' Prefs: ' + studpref[i][1][0] + ',' + studpref[i][1][1])
        
        if studpref[i][1][0] == roomate:
            add=0
            #print(' add : ' + str(add))
            cost = cost + 0
        elif studpref[i][1][1] == roomate:
            add=1
            #print(' add : ' + str(add))
            cost = cost + 1
        else:
            add=3
            #print(' add : ' + str(add))
            cost = cost + 3
    
    return cost


def find_roomate(assignments, student, room):
    for i in range(len(assignments)):
        if assignments[i] == room and prefs[i][0] != student:
            return studpref[i][0]
                  

                  
def printsolution(vec):
    slots=[]
    # Create two slots for each dorm
    for i in range(len(rooms)): slots += [i,i]

    # Loop over each students assignment
    for i in range(len(vec)):
        x=int(vec[i])

        # Choose the slot from the remaining ones
        room=rooms[slots[x]]
        # Show the student and assigned dorm
        print studpref[i][0],room
        # Remove this slot
        del slots[x]
    