import turtle

# Buat screen
screen = turtle.Screen()
screen.bgcolor("black")

# Buat turtle
t = turtle.Turtle()
t.speed(0)

# Fungsi untuk menggambar bunga
def gambar_bunga(t, x, y, warna):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(warna)
    t.begin_fill()
    t.circle(20)
    t.end_fill()

# Fungsi untuk menggambar daun
def gambar_daun(t, x, y, warna):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(warna)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# Fungsi untuk menggambar batang
def gambar_batang(t, x, y, tinggi, warna):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(warna)
    t.width(5)
    t.goto(x, y + tinggi)

# Gambar bunga
gambar_bunga(t, 0, 100, "white")
gambar_bunga(t, -30, 70, "white")
gambar_bunga(t, 30, 70, "white")

# Gambar daun
gambar_daun(t, -20, 40, "green")
gambar_daun(t, 20, 40, "green")
gambar_daun(t, -10, 20, "green")
gambar_daun(t, 10, 20, "green")

# Gambar batang
gambar_batang(t, 0, 0, 100, "green")
gambar_batang(t, -20, 20, 70, "green")
gambar_batang(t, 20, 20, 70, "green")

# Tunggu user menekan tombol
turtle.done()