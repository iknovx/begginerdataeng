from turtle import *

# Настройка экрана
speed(3)
bgcolor("pink")
penup()
goto(0, -100)
pendown()
color("red", "red")  # цвет контура и заливки
begin_fill()

# Рисуем сердце
left(140)
forward(180)
circle(-90, 200)
left(120)
circle(-90, 200)
forward(180)
end_fill()

# Пишем текст внутри сердца
penup()
goto(0, 30)  # подбираем координаты так, чтобы текст был в центре
color("white")
write("Мама", align="center", font=("Arial", 32, "bold"))

hideturtle()
done()