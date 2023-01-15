from turtle import Turtle

MOVE_DIST = 20
START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []

        for position in START_POS:
            new_segment = Turtle('square')
            new_segment.color('black')
            # new_segment.shapesize(0.5, 0.5, 0)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        '''
        we want the snake to move as one. in order to obtain this we want to previous segment to move into position 
        of front segment. this enables the snake to turn and th ebody to follow instead of one segment turning
        while the rest of the body continues on straight. We use range to reverse the segment so we return the last segment 
        and pass it coordinates of segment infront of it then the one in fronts get coordinates of the one infront
        this pattern goes on till ther whole body follows the head
        '''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_y = self.segments[seg_num - 1].ycor()
            new_x = self.segments[seg_num - 1].xcor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
