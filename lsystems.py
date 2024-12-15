import turtle
import pyscheme
import sys

def draw(string,p):
    ang = p[0]
    s = p[1]
    # Consider replacing with numpy
    stack = []
    turtle.screensize(3000,3000)
    turtle.setworldcoordinates(-1000, 00, 1000, 2000)
    turtle.width(2)
    turtle.speed(0)
    turtle.left(90)
    if s != 't':
        for i in string:
            if i == '0':
                #print("fw")
                if s != 'p':
                    turtle.forward(20)
            elif i == '1':
                #print("fw")
                turtle.forward(20)
            elif i == '+':
                #print("angr")
                turtle.left(ang)
            elif i == '-':
                #print("angl")
                turtle.right(ang)
            elif i == '[':
                #print("+stk")
                stack.append([turtle.pos(),turtle.heading()])
            elif i == ']':
                #print("-stk")
                info = stack.pop()
                turtle.up()
                turtle.goto(info[0])
                turtle.seth(info[1])
                turtle.down()
    else:
        turtle.setworldcoordinates(-1000, 0, 1000, 2000)
        #turtle.left(90)
        turtle.speed(0)
        turtle.width(5)
        for i in string:
            if i == '0':
                turtle.forward(10)
            elif i == '1':
                turtle.forward(20)
            elif i == '[':
                stack.append([turtle.pos(),turtle.heading()])
                turtle.left(45)
            elif i == ']':
                info = stack.pop()
                turtle.up()
                turtle.goto(info[0])
                turtle.seth(info[1])
                turtle.right(45)
                turtle.down()
                
    turtle.done()
    turtle.bye()

def inps():
    start = input("Enter start string\n")
    rules = input("Enter rules (0->str 1->str etc.)\n")
    iters = int(input("Enter number of iterations\n"))
    inputs = [start,rules,iters]
    return inputs

def inps2():
    angle = float(input("Enter angle\n"))
    special = input("Enter special case (t/p/ )\n")
    inputs = [angle,special]
    return inputs

def runscheme(params,schemecode):
    sys.setrecursionlimit(2000000)
    env = pyscheme.new_env()

    init = params[0]
    n = params[2]
    rules = params[1]
    
    temp = []
    
    init = init.replace("+", "2")
    init = init.replace("-", "3")
    init = init.replace("[", "4")
    init = init.replace("]", "5")
    rules = rules.replace("+", "2")
    rules = rules.replace("-", "3")
    rules = rules.replace("[", "4")
    rules = rules.replace("]", "5")
    
    rules = rules.split()
    
    rule1 = rules[0]
    
    for c in init:
        temp.append(int(c))
    init = temp
    temp = []
    
    rule2 = ""
    if (rules[1]):
        rule2 = rules[1]
        for c in rule2:
            temp.append(int(c))
        rule2 = temp
        temp = []
    
    for c in rule1:
        temp.append(int(c))
    rule1 = temp
    temp = []
    
    pyscheme.put("INIT", init, env)
    pyscheme.put("RULE1", rule1, env)
    pyscheme.put("RULE2", rule2, env)
    pyscheme.put("N", n, env)
    
    ans = pyscheme.run(schemecode, env)
    finstring = ""
    for i in ans:
        finstring = finstring + str(i)
    finstring = finstring.replace("2", "+")
    finstring = finstring.replace("3", "-")
    finstring = finstring.replace("4", "[")
    finstring = finstring.replace("5", "]")
    
    return finstring

if __name__ == '__main__':
    params = inps()
    f = open("s.scm","r")
    finstring = runscheme(params,f.read())
    f.close()
    p2 = inps2()
    draw(finstring,p2)