# as we relate to the methods and attributes of turtle module (Turtle class)
from turtle import Turtle
# Global Variables
MOVE_DISTANCE = 20
COLOR = "white"
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def reset(self):
        """Sends old snake out of the screen and creates new snake"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a snake of length 3"""
        for position in range(3):
            new_segment = Turtle(shape="circle")
            new_segment.color(COLOR)
            new_segment.penup()
            new_segment.setposition(x=0 - (position * MOVE_DISTANCE), y=0)
            self.segments.append(new_segment)

    def extend(self):
        """Add new segment, by eating the food"""
        # adds new segment to the end of a list
        new_segment = Turtle(shape="circle")
        new_segment.penup()
        new_segment.color(COLOR)
        new_segment.setposition(x=0 - (self.position() * MOVE_DISTANCE), y=0)
        self.segments.append(new_segment)

    def position(self):
        """Gives the x coordinate of last segment"""
        for seg in self.segments:
            return seg.xcor()

    def move(self):
        """Moves forward in any direction."""
        for seg_pos in range(len(self.segments) - 1, 0, -1):
            # starting from last piece of snake moves each piece to the position of the segment standing before itself
            new_x = self.segments[seg_pos - 1].xcor()
            new_y = self.segments[seg_pos - 1].ycor()
            self.segments[seg_pos].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

# # Method 2 of creating a snake:
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# for position in starting_position:
#     segment = Turtle("square")
#     segment.color("white")
#     segment.penup()
#     segment.goto(position)
#     segments.append(segment)
