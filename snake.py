from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.snakes()

    def snakes(self):
        for index in POSITION:
            self.add_segment(index)

    def add_segment(self, index):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(index)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.snakes()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)

        self.segments[0].forward(20)

    def right(self):
        self.segments[0].left(270)

    def left(self):
        self.segments[0].left(90)
