'''A game that uses Monte Carlo simulation. We will “randomly” throw a number of darts at a specially configured dartboard. A round dartboard is  mounted a square piece of wood. The dartboard has a radius of one unit. The piece of wood is exactly two units square so that the round board fits perfectly inside the square.'''

import turtle
import random

def dartToss(turt):
    hits = 0
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    turt.goto(x,y)
    if turt.distance(0, 0) <= 1:
        turt.color("red")
        turt.dot()
        hits = 1
    else:
        turt.color("blue")
        turt.dot()
    return hits

def numThrows(turt, num):
    totalHits = 0
    for i in range(num):
        hits = dartToss(turt)
        totalHits = totalHits + hits
    return(float(totalHits)/float(num)*4.0)

def main():
    num = int(input("How many darts would you like to throw?\n>> "))
    wn = turtle.Screen()
    wn.setworldcoordinates(-1,-1,1,1)
    ron = turtle.Turtle()
    ron.shape("circle")
    ron.pensize(1)
    ron.penup()
    ron.speed(9)
    print(numThrows(ron,num))
    wn.exitonclick()

main()
