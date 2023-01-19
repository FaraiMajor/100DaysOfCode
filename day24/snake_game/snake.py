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
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def add_segment(self, position):
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
        self.head.forward(MOVE_DIST)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def grow_snake(self):
        # add new segment to the snake
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
