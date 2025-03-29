from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def add_segment(self,position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def move(self):
        for index in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[index - 1].xcor()
            new_y = self.all_segments[index - 1].ycor()
            self.all_segments[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if  self.head.heading() != DOWN:
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

