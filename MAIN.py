import pyautogui
import time
import random
import tkinter as tk
import tkinter.font as font

pyautogui.FAILSAFE = False

class App:
    def __init__(self, master):
        self.is_running = False
        self.next_interval = 0

        self.button = tk.Button(master, text="Start", font=font.Font(weight=font.BOLD), command=self.toggle)
        self.button.pack()

        self.label = tk.Label(master, text="Time until next interval: --", fg="blue")
        self.label.pack()

        self.made_by = tk.Label(master, text="Made by Jacob Tapp AKA BigDickDaddy", fg="red")
        self.made_by.pack()

    def toggle(self):
        self.is_running = not self.is_running
        self.button.config(text="Stop" if self.is_running else "Start")
        if self.is_running:
            self.start()
        else:
            self.stop()

    def start(self):
        self.mouse_movement_loop()

    def stop(self):
        self.is_running = False

    def mouse_movement_loop(self):
        while self.is_running:
            self.next_interval = random.uniform(0, 60)
            start_time = time.time()
            while (time.time() - start_time) < self.next_interval:
                if not self.is_running:
                    break  # exit the loop if the stop button is pressed
                elapsed_time = time.time() - start_time
                self.label.config(text=f"Time until next interval: {self.next_interval - elapsed_time:.2f}")
                root.update()
                time.sleep(0.1)
            if self.is_running:  # check if the stop button has been pressed
                x_offset = random.uniform(-1000, 1000)
                y_offset = random.uniform(-1000, 1000)
                duration = random.uniform(0.25, 1.0)
                pyautogui.moveRel(x_offset, y_offset, duration=duration)

root = tk.Tk()
root.title("AFK-BOT")
app = App(root)
root.mainloop()
