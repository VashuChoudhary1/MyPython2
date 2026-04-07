import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("#020024")  # deep galaxy color
screen.title("Galaxy Love 💖")
screen.tracer(0)

# Main heart turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(3)
t.speed(0)

# Floating hearts turtle
h = turtle.Turtle()
h.hideturtle()
h.speed(0)

# Stars turtle
s = turtle.Turtle()
s.hideturtle()
s.speed(0)

# -------- Stars (Galaxy Background) --------
stars = []
for _ in range(80):
    stars.append({
        "x": random.randint(-350, 350),
        "y": random.randint(-350, 350),
        "size": random.randint(1, 3),
        "brightness": random.randint(150, 255)
    })

# -------- Floating Hearts --------
hearts = []
for _ in range(18):
    hearts.append({
        "x": random.randint(-300, 300),
        "y": random.randint(-350, 0),
        "size": random.randint(8, 14),
        "speed": random.uniform(0.5, 1.2)
    })

# Draw main heart
def draw_heart(size):
    t.penup()
    t.goto(0, -size/2)
    t.pendown()
    
    t.color("#ff0033")
    t.begin_fill()
    
    t.setheading(140)
    t.forward(size)
    t.circle(-size/2, 200)
    t.setheading(60)
    t.circle(-size/2, 200)
    t.forward(size)
    
    t.end_fill()

# Draw text
def draw_text():
    t.penup()
    t.goto(0, 70)
    t.color("white")
    t.write("Love You Mr. Saroy", align="center", font=("Arial", 30, "bold"))

# Draw small heart
def draw_small_heart(x, y, size):
    h.penup()
    h.goto(x, y)
    h.pendown()
    
    h.color(random.choice(["#ff4d6d", "#ff758f", "#ff8fa3"]))
    h.begin_fill()
    
    h.setheading(140)
    h.forward(size)
    h.circle(-size/2, 200)
    h.setheading(60)
    h.circle(-size/2, 200)
    h.forward(size)
    
    h.end_fill()

# Draw stars
def draw_stars():
    s.clear()
    for star in stars:
        s.penup()
        s.goto(star["x"], star["y"])
        
        # Twinkling effect
        brightness = random.randint(150, 255)
        color = (brightness/255, brightness/255, brightness/255)
        
        s.dot(star["size"], color)

# -------- Animation Loop --------
scale = 0
direction = 1

while True:
    t.clear()
    h.clear()
    
    # Galaxy stars
    draw_stars()
    
    # Smooth beating heart
    size = 180 + (scale * 8)
    draw_heart(size)
    draw_text()
    
    scale += direction * 0.4
    if scale > 2 or scale < -2:
        direction *= -1
    
    # Floating hearts
    for heart in hearts:
        heart["y"] += heart["speed"]
        
        if heart["y"] > 350:
            heart["y"] = -350
            heart["x"] = random.randint(-300, 300)
        
        draw_small_heart(heart["x"], heart["y"], heart["size"])
    
    screen.update()