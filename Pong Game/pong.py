from tkinter import *
import random
import math

WIDTH,  HEIGHT = 600, 400
RADIUS = 30
BALL_COLOUR = "white"

PADDLE_WIDTH = 120
PADDLE_HEIGHT = 10
PADDLE_COLOUR = "white"
PADDLE_SPEED = 15


ball_dx = 3
ball_dy = 3




class Ball:
    def __init__(self):
        self.pos = [random.randint(RADIUS, 800 - RADIUS),
                    random.randint(RADIUS, 300)]


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.canvas = Canvas(root, background='black',
                             width=WIDTH, height=HEIGHT)
        self.health = 3
        self.xp = 0
        # i = PhotoImage(file='heart.png')
        # self.xp_label = Label(self.root, image=i)
        # self.xp_label.pack()
        # self.heart_label = Label(self.root, text=f": {self.xp}")
        self.canvas.pack()
        self.ball = [random.randint(RADIUS, 800 - RADIUS),
                    random.randint(RADIUS, 300)]
        self.paddle = [400, 500]
        self.root.bind("<Key>", self.on_key_press)
        self.is_gameover = False

    def on_key_press(self, event):
        key = event.keysym
        paddle_pos = self.canvas.coords(self.paddle_game)
        # print(key)
        if key == 'Left' and paddle_pos[0] > 0:
            self.canvas.move(self.paddle_game, -PADDLE_SPEED, 0)
        elif key == 'Right' and paddle_pos[2] < WIDTH:
            self.canvas.move(self.paddle_game, +PADDLE_SPEED, 0)

    def draw_shapes(self):
        self.canvas.delete(ALL)

        self.paddle_game = self.canvas.create_rectangle((self.paddle[0], self.paddle[1], self.paddle[0] +
                                                         PADDLE_WIDTH, self.paddle[1] + PADDLE_HEIGHT), fill=PADDLE_COLOUR)

        self.ball_game = self.canvas.create_oval(
            (self.ball[0], self.ball[1], self.ball[0] + RADIUS, self.ball[1] + RADIUS), fill=BALL_COLOUR)


    def move_ball(self):
        global ball_dx
        global ball_dy
        self.canvas.move(self.ball_game, ball_dx, ball_dy)
        ball_pos = self.canvas.coords(self.ball_game)
        # height
        if ball_pos[1] <= 0 or ball_pos[3] >= HEIGHT:
            ball_dy = -ball_dy
        # width
        if ball_pos[0] <= 0 or ball_pos[2] >= WIDTH:
            ball_dx = -ball_dx

        if ball_pos[1] > 500 + PADDLE_HEIGHT or ball_pos[3] > 500 + PADDLE_HEIGHT:
            self.health -= 1
            if self.health == 0:
                self.health -= 1
                if self.health == 0:
                    self.is_gameover = True

        # collision with paddle
        paddle_pos = self.canvas.coords(self.paddle_game)
        xrange = range(int(paddle_pos[0]), int(paddle_pos[2]+1))
        yrange = range(int(paddle_pos[1]), int(paddle_pos[3]+1))
        if (ball_pos[0] in xrange or ball_pos[2] in xrange) and (ball_pos[1] in yrange or ball_pos[3] in yrange):
            ball_dy = -ball_dy
            self.xp += 1

    def game_loop(self):
        if not self.is_gameover:
            self.move_ball()
        else:
            self.root.unbind("<Key>")

            self.canvas.create_text(
                WIDTH//2, HEIGHT//2, fill='red', text="Game Over :(", font=('arial', 50))

        self.root.after(20, self.game_loop)


root = Tk()

game = Game(root)
game.draw_shapes()
game.game_loop()

root.mainloop()
