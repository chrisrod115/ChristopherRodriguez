"""# Goal: is to make the robot reach the flag on own
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    # Turn if you are in front of a wall
    turn_left()
    # Move if if wall on right()
    while wall_on_right():
        move()
    # Turn back down if you are on top
    turn_right()
    move()
    turn_right()
    # Go down till you reach the end.
    while front_is_clear():
        move()
    # Turn left if you reached the end.
    turn_left()
        

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
"""

"""
Goal: Finsh the maze
Algorithm: Have the robot follow the right side of the wall
Condition 1: If right side == clear follow the edge.
Condition 2: If not clear go straight.
Condition 3: If not clear/cant turn right turn left.

"""
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hit_wall():
    while wall_on_right and wall_in_front():
        turn_left()
def no_right_wall():
    turn_right()
    move()
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif not wall_on_right():
        no_right_wall()
    else:
        hit_wall()
"""
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    else:
        move()
"""
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
    
    
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_around()
"""
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def jump_hurdle():
    wall = True
    while wall != False:
        if wall_on_right() and is_facing_north():
            move()
        elif wall_on_right() and front_is_clear():
            move()
        elif not is_facing_north() and front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
            move()
            turn_right()
        else:
            wall = False
    
while not at_goal():
    if wall_on_right() and wall_in_front():
        turn_left()
        if wall_on_right() and is_facing_north():
            jump_hurdle()
    else:
        move()
"""            
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def jump_hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_hurdle()
    else:
        move()
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right() 
        move()
    else:
        turn_left()



    