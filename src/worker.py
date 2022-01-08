import logging
from threading import Thread, Lock

class Worker(Thread):
    thread_counter_lock = Lock()
    thread_counter = 0

    def __init__(self, *args, **kwargs):
        if "name" not in kwargs:
            with Worker.thread_counter_lock:
                kwargs["name"] = f"{self.__class__.__name__}-{self.thread_counter}"
                Worker.thread_counter += 1
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(kwargs["name"])
        self.started = False
        
    def start(self):
        self.logger.info(f"Starting thread: {self.getName()}")
        self.started = True
        super().start()
        
    def stop(self):
        self.logger.info(f"Stopping thread {self.getName()}")
        self.started = False
        super().join()
        self.logger.info(f"Thread exited succesfully: {self.getName()}")