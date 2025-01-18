import threading
import time
import queue
import pygame

class AudioManager:
    def __init__(self):
        self.audio_queue = queue.Queue()
        self.current_path = None
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def add_audio_path(self, path):
        self.audio_queue.put(path)

    def run(self):
        pygame.mixer.init()
        while True:
            if not self.audio_queue.empty():
                self.current_path = self.audio_queue.get()
                self.play_audio(self.current_path)
            time.sleep(1)

    def play_audio(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
