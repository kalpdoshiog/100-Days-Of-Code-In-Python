def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
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
    if wall_in_front() and wall_on_right():
        turn_left()
        if wall_in_front():
            turn_left()
            move()
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif wall_on_right():
        move()
