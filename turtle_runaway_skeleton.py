# Updating the game to have 5 rounds, with increasing scores per round, and showing the final score at the end.

import tkinter as tk
import turtle
import random


class RunawayGame:
    def __init__(self, canvas, runner, chaser, root, catch_radius=50, max_rounds=5):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2
        self.root = root
        self.score = 0
        self.round_number = 1
        self.max_rounds = max_rounds
        self.is_game_over = False

        # Initialize 'runner' and 'chaser'
        self.runner.shape("turtle")
        self.runner.color("blue")
        self.runner.penup()

        self.chaser.shape("turtle")
        self.chaser.color("red")
        self.chaser.penup()

        # Instantiate another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

    def is_catched(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start_round(self):
        self.is_game_over = False
        self.runner.setpos((-200, 0))
        self.runner.setheading(
            random.randint(0, 360)
        )  # Random starting direction for the runner
        self.chaser.setpos((200, 0))
        self.chaser.setheading(180)

        # Timer countdown for each round
        self.time_remaining = 30  # 30 seconds per round
        self.update_timer_display()

        self.canvas.ontimer(self.step, 100)

    def update_timer_display(self):
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        self.drawer.write(
            f"Round: {self.round_number} | Time left: {int(self.time_remaining)} sec | Score: {self.score}",
            font=("Arial", 16, "normal"),
        )

    def step(self):
        if self.time_remaining <= 0 or self.is_game_over:
            self.end_round()
            return

        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        if self.is_catched():
            self.is_game_over = True
            self.update_score()
            self.end_round()
            return

        self.time_remaining -= 0.1
        self.update_timer_display()

        if not self.is_game_over:
            self.canvas.ontimer(self.step, 100)

    def update_score(self):
        self.score += self.round_number  # Add points based on the round number

    def end_round(self):
        if self.round_number >= self.max_rounds:
            self.end_game()
        else:
            self.round_number += 1
            self.start_round()

    def end_game(self):
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        self.drawer.write(
            f"Game Over! Final Score: {self.score}", font=("Arial", 16, "normal")
        )


class SmarterMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10, boundary=300):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn
        self.boundary = boundary  # Define screen boundary for movement

    def run_ai(self, opp_pos, opp_heading):
        # Smarter AI moves away from the chaser (opponent)
        my_pos = self.pos()
        dx = my_pos[0] - opp_pos[0]
        dy = my_pos[1] - opp_pos[1]
        distance = (dx**2 + dy**2) ** 0.5

        if distance < 150:
            # Turn away from the chaser and move faster
            angle_to_chaser = self.towards(opp_pos)
            self.setheading(angle_to_chaser + 180)  # Move in the opposite direction
            self.forward(self.step_move * 3)  # Move even faster when the chaser is near
        else:
            self.forward(self.step_move)

        self.check_boundary()  # Check if the turtle is within the boundary

    def check_boundary(self):
        x, y = self.pos()
        # Teleport to the opposite side when hitting a boundary
        if x > self.boundary:
            self.setx(-self.boundary)  # Appear on the opposite side
        elif x < -self.boundary:
            self.setx(self.boundary)  # Appear on the opposite side
        if y > self.boundary:
            self.sety(-self.boundary)  # Appear on the opposite side
        elif y < -self.boundary:
            self.sety(self.boundary)  # Appear on the opposite side


class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10, boundary=300):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn
        self.boundary = boundary

        # Register event handlers for manual control
        canvas.onkeypress(lambda: self.forward(self.step_move), "Up")
        canvas.onkeypress(lambda: self.backward(self.step_move), "Down")
        canvas.onkeypress(lambda: self.left(self.step_turn), "Left")
        canvas.onkeypress(lambda: self.right(self.step_turn), "Right")
        canvas.listen()

    def run_ai(self, opp_pos, opp_heading):
        pass

    def check_boundary(self):
        x, y = self.pos()
        # Teleport to the opposite side when hitting a boundary
        if x > self.boundary:
            self.setx(-self.boundary)  # Appear on the opposite side
        elif x < -self.boundary:
            self.setx(self.boundary)  # Appear on the opposite side
        if y > self.boundary:
            self.sety(-self.boundary)  # Appear on the opposite side
        elif y < -self.boundary:
            self.sety(self.boundary)  # Appear on the opposite side


if __name__ == "__main__":
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    # Modify the runner and chaser to use SmarterMover and ManualMover with boundary limits
    runner = SmarterMover(screen)
    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser, root)  # 5-round game
    game.start_round()
    screen.mainloop()
