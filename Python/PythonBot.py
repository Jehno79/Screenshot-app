import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread
import pyautogui
import time
import os

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Screenshot App")
        self.is_capturing = False
        self.screenshot_count = 0
        self.capture_speed = 2

        tk.Label(root, text='Credit: Jehno#4316', font=('Arial', 10, 'italic')).pack(anchor='w', padx=10, pady=10)

        self.label = tk.Label(root, text='Press Start to begin capturing screenshots.', font=('Arial', 12))
        self.label.pack(pady=10)

        self.directory_frame = tk.Frame(root)
        self.directory_frame.pack()

        self.directory_label = tk.Label(self.directory_frame, text='Directory:', font=('Arial', 10))
        self.directory_label.pack(side='left')

        self.directory_entry = tk.Entry(self.directory_frame, width=35, font=('Arial', 10))
        self.directory_entry.pack(side='left', padx=5)

        self.browse_button = tk.Button(self.directory_frame, text='Browse', command=self.browse_directory, width=10, font=('Arial', 10))
        self.browse_button.pack(side='left')

        self.count_label = tk.Label(root, text='Screenshots Taken: 0', font=('Arial', 10))
        self.count_label.pack()

        self.speed_label = tk.Label(root, text='Capture Speed:', font=('Arial', 10))
        self.speed_label.pack()

        self.speed_scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, length=200, font=('Arial', 10), command=self.update_speed)
        self.speed_scale.set(self.capture_speed)
        self.speed_scale.pack()

        self.start_stop_button = tk.Button(root, text='Start', command=self.toggle_start_stop, width=10, font=('Arial', 12, 'bold'), bg='#4CAF50', fg='#FFFFFF')
        self.start_stop_button.pack(pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory(initialdir=os.getcwd())
        if directory:
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(tk.END, directory)

    def update_speed(self, value):
        self.capture_speed = int(value)

    def toggle_start_stop(self):
        if not self.is_capturing:
            self.is_capturing = True
            self.start_stop_button.config(text='Stop', bg='#FF0000')
            self.start_screenshot()
        else:
            self.is_capturing = False
            self.start_stop_button.config(text='Start', bg='#4CAF50')

    def start_screenshot(self):
        directory = self.directory_entry.get()
        if directory:
            self.label.config(text='Capturing screenshots...')
            os.makedirs(directory, exist_ok=True)

            thread = Thread(target=self.take_screenshot, args=(directory,))
            thread.start()

    def take_screenshot(self, directory):
        while self.is_capturing:
            self.screenshot_count += 1
            screenshot = pyautogui.screenshot()
            screenshot.save(os.path.join(directory, f"screenshot{self.screenshot_count}.png"))
            self.count_label.config(text=f'Screenshots Taken: {self.screenshot_count}')

            time.sleep(self.capture_speed)

        self.label.config(text='Press Start to begin capturing screenshots.')

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()