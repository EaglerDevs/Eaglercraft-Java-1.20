import turtle

class EaglercraftText:
    def __init__(self):
        turtle.tracer(0)
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
    def draw_text(self, message, color, size, x, y):
        on_letter = -1
        for letter in message:
            on_letter += 1
            x += pow(size, size)*pow(size, size)
            if letter == 'a':
                self.draw_square(color, size, x+size, y)
                self.draw_square(color, size, x+size*2, y)
                self.draw_square(color, size, x+size*3, y)
                self.draw_square(color, size, x+size*4, y-size)
                self.draw_square(color, size, x+size*4, y-(size*2))
                self.draw_square(color, size, x+size*3, y-(size*2))
                self.draw_square(color, size, x+size*2, y-(size*2))
                self.draw_square(color, size, x+size*1, y-(size*2))
                self.draw_square(color, size, x+size*4, y-(size*3))
                self.draw_square(color, size, x+size*4, y-(size*4))
                self.draw_square(color, size, x+size*3, y-(size*4))
                self.draw_square(color, size, x+size*2, y-(size*4))
                self.draw_square(color, size, x+size*1, y-(size*4))
                self.draw_square(color, size, x, y-(size*3))
            elif letter == 'b':
                self.draw_square(color, size, x-(size*1), y+(size*3))
                self.draw_square(color, size, x-(size*1), y+(size*2))
                self.draw_square(color, size, x-(size*1), y+(size*1))
                self.draw_square(color, size, x-(size*1), y)
                self.draw_square(color, size, x-(size*1), y-(size*1))
                self.draw_square(color, size, x-(size*1), y-(size*2))
                self.draw_square(color, size, x-(size*1), y-(size*3))
                self.draw_square(color, size, x-(size*1), y-(size*4))
                self.draw_square(color, size, x+size-(size*1), y-(size*1))
                self.draw_square(color, size, x+(size*2)-(size*1), y)
                self.draw_square(color, size, x+(size*3)-(size*1), y)
                self.draw_square(color, size, x+(size*4)-(size*1), y-(size*1))
                self.draw_square(color, size, x+(size*4)-(size*1), y-(size*2))
                self.draw_square(color, size, x+(size*4)-(size*1), y-(size*3))
                self.draw_square(color, size, x+(size*3)-(size*1), y-(size*4))
                self.draw_square(color, size, x+(size*2)-(size*1), y-(size*4))
                self.draw_square(color, size, x+(size*1)-(size*1), y-(size*4))
            elif letter == 'c':
                self.draw_square(color, size, x-(size*4)-(size*1), y-(size*1))
                self.draw_square(color, size, x-(size*4)-(size*1), y-(size*2))
                self.draw_square(color, size, x-(size*4)-(size*1), y-(size*3))
                self.draw_square(color, size, x-(size*3)-(size*1), y-(size*4))
                self.draw_square(color, size, x-(size*2)-(size*1), y-(size*4))
                self.draw_square(color, size, x-(size*1)-(size*1), y-(size*4))
                self.draw_square(color, size, x-(size*1), y-(size*3))
                self.draw_square(color, size, x-(size*2)-(size*2), y)
                self.draw_square(color, size, x-(size*1)-(size*2), y)
                self.draw_square(color, size, x-(size*2), y)
                self.draw_square(color, size, x-(size*1), y-(size*1))
            elif letter == 'd':
                self.draw_square(color, size, x, y+(size*5))
                self.draw_square(color, size, x, y+(size*4))
                self.draw_square(color, size, x, y+(size*3))
                self.draw_square(color, size, x, y+(size*2))
                self.draw_square(color, size, x-(size*1), y)
                self.draw_square(color, size, x-(size*2), y+(size*1))
                self.draw_square(color, size, x-(size*3), y+(size*1))
                self.draw_square(color, size, x-(size*4), y)
                self.draw_square(color, size, x-(size*4), y-(size*1))
                self.draw_square(color, size, x-(size*4), y-(size*2))
                self.draw_square(color, size, x-(size*4), y-(size*3))
                self.draw_square(color, size, x-(size*3), y-(size*4))
                self.draw_square(color, size, x-(size*2), y-(size*4))
                self.draw_square(color, size, x-(size*1), y-(size*4))
                self.draw_square(color, size, x, y+(size*1))
                self.draw_square(color, size, x, y)
                self.draw_square(color, size, x, y-(size*1))
                self.draw_square(color, size, x, y-(size*2))
                self.draw_square(color, size, x, y-(size*3))
                self.draw_square(color, size, x, y-(size*4))
            elif letter == 'e':
                self.draw_square(color, size, x, y)
                self.draw_square(color, size, x+(size*1), y)
                self.draw_square(color, size, x+(size*2), y)
                self.draw_square(color, size, x+(size*3), y)
                self.draw_square(color, size, x+(size*3), y+(size*1))
                self.draw_square(color, size, x+(size*2), y+(size*2))
                self.draw_square(color, size, x+(size*1), y+(size*2))
                self.draw_square(color, size, x, y+(size*2))
                self.draw_square(color, size, x-(size*1), y+(size*1))
                self.draw_square(color, size, x-(size*1), y)
                self.draw_square(color, size, x-(size*1), y-(size*1))
                self.draw_square(color, size, x, y-(size*2))
                self.draw_square(color, size, x+(size*1), y-(size*2))
                self.draw_square(color, size, x+(size*2), y-(size*2))
                self.draw_square(color, size, x+(size*3), y-(size*2))
            elif letter == ' ':
                x += (size*1)
            elif letter == 'f':
                self.draw_square(color, size, x, y)
                self.draw_square(color, size, x, y-(size*1))
                self.draw_square(color, size, x, y-(size*2))
                self.draw_square(color, size, x, y-(size*3))
                self.draw_square(color, size, x, y-(size*4))
                self.draw_square(color, size, x, y+(size*1))
                self.draw_square(color, size, x, y+(size*2))
                self.draw_square(color, size, x, y+(size*3))
                self.draw_square(color, size, x+(size*1), y+(size*4))
                self.draw_square(color, size, x+(size*2), y+(size*4))
                self.draw_square(color, size, x-(size*1), y+(size*1))
                self.draw_square(color, size, x+(size*1), y+(size*1))
                self.draw_square(color, size, x+(size*2), y+(size*1))
            elif letter == 'g':
                self.draw_square(color, size, x, y)
                self.draw_square(color, size, x-(size*1), y)
                self.draw_square(color, size, x+(size*1), y)
                self.draw_square(color, size, x+(size*2), y)
                self.draw_square(color, size, x+(size*3), y)
                self.draw_square(color, size, x+(size*3), y+(size*1))
                self.draw_square(color, size, x+(size*3), y+(size*2))
                self.draw_square(color, size, x+(size*3), y+(size*3))
                self.draw_square(color, size, x+(size*3), y+(size*4))
                self.draw_square(color, size, x+(size*2), y+(size*4))
                self.draw_square(color, size, x+(size*1), y+(size*4))
                self.draw_square(color, size, x, y+(size*4))
                self.draw_square(color, size, x-(size*1), y+(size*4))
                self.draw_square(color, size, x-(size*2), y+(size*3))
                self.draw_square(color, size, x-(size*2), y+(size*2))
                self.draw_square(color, size, x-(size*2), y+(size*1))
                self.draw_square(color, size, x+(size*3), y-(size*1))
                self.draw_square(color, size, x+(size*2), y-(size*2))
                self.draw_square(color, size, x+(size*1), y-(size*2))
                self.draw_square(color, size, x, y-(size*2))
                self.draw_square(color, size, x-(size*1), y-(size*2))
                self.draw_square(color, size, x-(size*2), y-(size*2))
            elif letter == 'h':
                self.draw_square(color, size, x, y+(size*2))
                self.draw_square(color, size, x+(size*1), y+(size*2))
                self.draw_square(color, size, x+(size*2), y+(size*1))
                self.draw_square(color, size, x+(size*2), y)
                self.draw_square(color, size, x+(size*2), y-(size*1))
                self.draw_square(color, size, x+(size*2), y-(size*2))
                self.draw_square(color, size, x-(size*3), y-(size*2))
                self.draw_square(color, size, x-(size*3), y-(size*1))
                self.draw_square(color, size, x-(size*3), y)
                self.draw_square(color, size, x-(size*3), y+(size*1))
                self.draw_square(color, size, x-(size*2), y+(size*1))
                self.draw_square(color, size, x-(size*1), y+(size*1))
                self.draw_square(color, size, x-(size*3), y+(size*2))
                self.draw_square(color, size, x-(size*3), y+(size*3))
                self.draw_square(color, size, x-(size*3), y+(size*4))
                self.draw_square(color, size, x-(size*3), y+(size*5))
                self.draw_square(color, size, x-(size*3), y+(size*6))
                self.draw_square(color, size, x-(size*3), y+(size*7))
            elif letter == 'i':
                self.draw_square(color, size, x, y)
                self.draw_square(color, size, x, y+(size*1))
                self.draw_square(color, size, x, y+(size*2))
                self.draw_square(color, size, x, y+(size*3))
                self.draw_square(color, size, x, y+(size*5))
                self.draw_square(color, size, x, y-(size*1))
                self.draw_square(color, size, x, y-(size*2))
            elif letter == 'j':
                self.draw_square(color, size, x, y)
                self.draw_square(color, size, x, y+(size*1))
                self.draw_square(color, size, x, y+(size*2))
                self.draw_square(color, size, x, y+(size*3))
                self.draw_square(color, size, x, y+(size*5))
                self.draw_square(color, size, x, y-(size*1))
                self.draw_square(color, size, x, y-(size*2))
                self.draw_square(color, size, x-(size*1), y-(size*3))
                self.draw_square(color, size, x-(size*2), y-(size*3))
                self.draw_square(color, size, x-(size*3), y-(size*2))
    def draw_square(self, color, size, x, y):
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.fillcolor(color)
        self.pen.pencolor(color)
        for _ in range(4):
            self.pen.forward(size)
            self.pen.left(90)
        self.pen.end_fill()
        turtle.update()
    def destroy_text(self):
        self.pen.clear()
    def show_typing_thingy(self):
        pass
        

#remember to remove this part later, its just a test!
eaglertext = EaglercraftText()
eaglertext.draw_text('abcdefghij', 'black', 2, 0, 0)

turtle.mainloop()
