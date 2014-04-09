from graphics import *


class my_stack:
    
    def __init__(self):
        self.mystack = []
        self.mystack2 = []
        
    def pop(self):
        return self.mystack.pop()
        
    def push(self, a):
        self.mystack.append(a)
    
    def isEmpty(self):
        if len(self.mystack) == 0:
            return True
        return False
        
    def top(self):
        return self.mystack[-1]
        
def DrawGraphlines(win):
    y = 35
    while y<= 665:
        line = Line(Point(0, y), Point(700, y))
        line.setWidth(1)
        line.setOutline("grey")
        line.draw(win)
        y += 35
        
    label=Text(Point(306, 66), '8')
    label.draw(win)
    label=Text(Point(306, 136), '6')
    label.draw(win)
    label=Text(Point(306, 206), '4')
    label.draw(win)
    label=Text(Point(306, 276), '2')
    label.draw(win)

    line = Line(Point(0, 350), Point(700, 350)) #center horizontal line
    line.setWidth(3)
    line.draw(win)

    label=Text(Point(310, 416), '-2')
    label.draw(win)
    label=Text(Point(310, 486), '-4')
    label.draw(win)
    label=Text(Point(310, 556), '-6')
    label.draw(win)
    label=Text(Point(310, 626), '-8')
    label.draw(win)
    line = Line(Point(300, 0), Point(300, 700)) #Center vertical line
    line.setWidth(3)
    line.draw(win)
       
    x = 30
    while x<= 570:
        line = Line(Point(x, 0), Point(x, 700))
        line.setWidth(1)
        line.setOutline("grey")
        line.draw(win)
        x += 30
        
    label=Text(Point(328, 360), '1')
    label.draw(win)
    label=Text(Point(357, 360), '2')
    label.draw(win)
    label=Text(Point(387, 360), '3')
    label.draw(win)
    label=Text(Point(417, 360), '4')
    label.draw(win)
    label=Text(Point(447, 360), '5')
    label.draw(win)
    label=Text(Point(477, 360), '6')
    label.draw(win)
    label=Text(Point(507, 360), '7')
    label.draw(win)
    label=Text(Point(537, 360), '8')
    label.draw(win)
    label=Text(Point(567, 360), '9')
    label.draw(win)
    label=Text(Point(266, 360), '-1')
    label.draw(win)
    label=Text(Point(236, 360), '-2')
    label.draw(win)
    label=Text(Point(206, 360), '-3')
    label.draw(win)
    label=Text(Point(176, 360), '-4')
    label.draw(win)
    label=Text(Point(146, 360), '-5')
    label.draw(win)
    label=Text(Point(116, 360), '-6')
    label.draw(win)
    label=Text(Point(86, 360), '-7')
    label.draw(win)
    label=Text(Point(56, 360), '-8')
    label.draw(win)
    label=Text(Point(26, 360), '-9')
    label.draw(win)
    
def DrawButtons(win):
    quitButton = Rectangle(Point(540, 650), Point(580,690))
    quitButton.setFill("lightblue")
    quitButton.draw(win)
    label = Text(Point(560,670),"Quit")
    label.draw(win)
    
    resetButton = Rectangle(Point(490, 650), Point(530,690))
    resetButton.setFill("lightblue")
    resetButton.draw(win)
    label = Text(Point(510,670),"Reset")
    label.draw(win)
    
    enterButton = Rectangle(Point(200, 650), Point(240,690))
    enterButton.setFill("lightblue")
    enterButton.draw(win)
    label = Text(Point(220,670),"Enter")
    label.draw(win)
    
def DrawLabels(win):
    text1 = Text(Point(115, 690),"Enter Formula = example x*x ")
    text1.draw(win)

def InfixToPostfix(infix):
    postfix = " "
    opstack = my_stack()
    for c in infix:
        print c
        if c.isdigit() or c == 'x' or c == 'X':
            postfix += c
        elif c == '(':
            opstack.push(c)
        elif c == ')':
            while opstack.top() !='(':
                postfix += opstack.pop()
            opstack.pop()
        elif c in ['+', '-']:
            while not opstack.isEmpty() and  opstack.top() in ['+', '-', '*', '/']:   
                postfix += opstack.pop()
            opstack.push(c)
        elif c in ['*', '/']:
            while not opstack.isEmpty() and  opstack.top() in ['*', '/']:   
                postfix += opstack.pop()
            opstack.push(c)
    while not opstack.isEmpty():
        postfix += opstack.pop()

    return postfix

def EvaluatePostfix(x, postfix):
    opstack = my_stack()
    for c in postfix:
        if c.isdigit():
            opstack.push(float(c))
        elif c in ['x', 'X']:
            opstack.push(x)
        elif opstack.isEmpty() == False:
            right = float(opstack.pop())
            if opstack.isEmpty():
                return v
            left = float(opstack.pop())
            if c == '+':
                v = left + right
            if c == '-':
                v = left - right
            if c == '*':
                v =  left * right
            if c == '/':
                v = left / right
            opstack.push(v)
    return opstack.pop()
       
    
def print_instructions():
    print "This graphing calculator can graph basic formulas to a graph, from your input"

def main():
    print_instructions()
    
    
    #infix = raw_input("Enter your formula: Example 'x*x/(x+3)' ")
    #postfix = InfixToPostfix(infix)
    win = GraphWin("Jeremy's Graphing Calculator", 600, 700)
    DrawGraphlines(win)
    DrawButtons(win)
    DrawLabels(win)
    entry1 = Entry(Point(110, 670), 20)
    entry1.draw(win)

    win.setCoords(-10, -10, 10, 10)


    
    more = True
    while more:
        p = win.getMouse()
        if(p.x >= 8.07 and p.x <= 9.38 and p.y <= -8.69 and p.y >= -9.76):
            more = False        #Quits the program
        elif(p.x >=-3.25 and p.x <= -2.02 and p.y <= -8.69 and p.y >= -9.76):
            infix = entry1.getText()
            postfix = InfixToPostfix(infix)
            print "test"
            x = -10
            xaxisInc = .1
            while x <= 10:
                point1 = Point(x, EvaluatePostfix(x, postfix))
                point2 = Point(x + xaxisInc, EvaluatePostfix(x + xaxisInc, postfix))
                line = Line(point1, point2)
                line.setWidth(3)
                line.setOutline("green")
                line.draw(win)
                x += xaxisInc
    win.close()

main()
