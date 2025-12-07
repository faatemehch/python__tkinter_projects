from tkinter import *

ball_dx = 4
ball_dy = 4
paddle_speed = 15
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 10

class Game:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x850")
        self.left_score = 0
        img = Image('photo', file='/Users/fch/Desktop/python__tkinter_projects/Pong Game/pong.png')
        self.root.call('wm', 'iconphoto', root._w, img)
        self.right_score = 0
        self.game_time = 30  # زمان بازی به ثانیه
        self.game_active = True  # وضعیت بازی
        
        # لیبل‌های امتیاز
        self.left_label = Label(self.root, text="Left Score: 0")
        self.left_label.pack()
        self.right_label = Label(self.root, text="Right Score: 0")
        self.right_label.pack()
        
        # لیبل تایمر
        self.timer_label = Label(self.root, text="Time: 30s", font=("Arial", 14))
        self.timer_label.pack()
        
        # لیبل برنده
        self.winner_label = Label(self.root, text="", font=("Arial", 16, "bold"))
        self.winner_label.pack()
        
        self.canvas = Canvas(root, background='black',
                             width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.canvas.create_rectangle(390, 0, 410, 800, fill='white')
        self.paddle_left = self.canvas.create_rectangle(
            10, 300, 20, 400, fill='white')
        self.paddle_right = self.canvas.create_rectangle(
            790, 300, 780, 400, fill='white')
        self.ball = self.canvas.create_oval(
            345, 345, 385, 385, fill="yellow", outline="yellow")
        self.root.bind("<KeyPress>", self.on_key_press)
        
        # شروع تایمر
        self.start_timer()

    def start_timer(self):
        """شروع تایمر 30 ثانیه‌ای"""
        self.remaining_time = self.game_time
        self.update_timer()

    def update_timer(self):
        """به‌روزرسانی تایمر"""
        if self.remaining_time > 0 and self.game_active:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time: {self.remaining_time}s")
            self.root.after(1000, self.update_timer)
        elif self.remaining_time <= 0:
            self.end_game()

    def end_game(self):
        """پایان بازی و نمایش برنده"""
        self.game_active = False
        
        # تعیین برنده
        if self.left_score > self.right_score:
            winner_text = "Left Player Wins!"
            color = "green"
        elif self.right_score > self.left_score:
            winner_text = "Right Player Wins!"
            color = "blue"
        else:
            winner_text = "It's a Tie!"
            color = "orange"
        
        self.winner_label.config(text=winner_text, fg=color)
        
        # غیرفعال کردن حرکت پدل‌ها
        self.root.unbind("<KeyPress>")
        
        # نمایش پیام پایان بازی
        self.canvas.create_text(
            WIDTH//2, HEIGHT//2,
            text=f"Game Over!\n{winner_text}\nLeft: {self.left_score} - Right: {self.right_score}",
            fill="white",
            font=("Arial", 24, "bold"),
            justify="center"
        )

    def on_key_press(self, event):
        if not self.game_active:
            return
            
        key = event.keysym
        if key == "s":
            self.canvas.move(self.paddle_left, 0, paddle_speed)
        elif key == "w":
            self.canvas.move(self.paddle_left, 0, -paddle_speed)
        elif key == 'Up':
            self.canvas.move(self.paddle_right, 0, -paddle_speed)
        elif key == 'Down':
            self.canvas.move(self.paddle_right, 0, paddle_speed)

    def move_ball(self):
        if not self.game_active:
            return
            
        global ball_dx
        global ball_dy
        self.canvas.move(self.ball, ball_dx, ball_dy)
        ball_pos = self.canvas.coords(self.ball)
        left_paddl_pos = self.canvas.coords(self.paddle_left)
        right_paddl_pos = self.canvas.coords(self.paddle_right)

        # height
        if ball_pos[1] <= 0 or ball_pos[3] >= 600:
            ball_dy = -ball_dy
        # width
        if ball_pos[0] <= 0 or ball_pos[2] >= WIDTH:
            ball_dx = -ball_dx

        # check Left side
        xrange = range(int(left_paddl_pos[0]), int(left_paddl_pos[2]+1))
        yrange = range(int(left_paddl_pos[1]), int(left_paddl_pos[3]+1))
        if (ball_pos[0] in xrange or ball_pos[2] in xrange) and (ball_pos[1] in yrange or ball_pos[3] in yrange):
            ball_dx = -ball_dx
            self.left_score += 1
            self.left_label.config(text=f"Left Score: {self.left_score}")

        # check Right Side
        xrange = range(int(right_paddl_pos[0]), int(right_paddl_pos[2]+1))
        yrange = range(int(right_paddl_pos[1]), int(right_paddl_pos[3]+1))
        if (ball_pos[0] in xrange or ball_pos[2] in xrange) and (ball_pos[1] in yrange or ball_pos[3] in yrange):
            ball_dx = -ball_dx
            self.right_score += 1
            self.right_label.config(text=f"Right Score: {self.right_score}")

    def game_loop(self):
        self.move_ball()
        self.root.after(20, self.game_loop)

root = Tk()
game = Game(root)
game.game_loop()
root.mainloop()