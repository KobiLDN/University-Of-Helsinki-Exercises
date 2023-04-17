class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.minutes == 59 and self.seconds == 59:
            self.minutes = 0
            self.seconds = 0
        elif self.seconds == 59:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1

    def __str__(self):
        return f"{self.minutes:02}:{self.seconds:02}"
        # if self.minutes > 9:
        #     return f"{self.minutes}:0{self.seconds}"
        # if self.seconds < 10:
        #     return f"0{self.minutes}:0{self.seconds}"
        # return f"0{self.minutes}:{self.seconds}"

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()