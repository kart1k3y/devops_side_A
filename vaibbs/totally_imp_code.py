import random
import time
import itertools
import math

class FakeComputation:
    def __init__(self, size=1000):
        self.size = size
        self.data = [random.random() for _ in range(size)]

    def shuffle_data(self):
        random.shuffle(self.data)

    def pretend_to_calculate(self):
        result = 0
        for i, val in enumerate(self.data):
            result += math.sin(val) * math.cos(val) / (i + 1)
        return result

    def meaningless_loop(self):
        for combo in itertools.combinations(range(10), 2):
            time.sleep(0.001)  # slows things down
        return "Loop finished"

def main():
    fc = FakeComputation(size=500)
    print("Starting fake computation...")
    fc.shuffle_data()
    res = fc.pretend_to_calculate()
    print("Intermediate result:", res)
    msg = fc.meaningless_loop()
    print(msg)
    print("Final output:", sum(fc.data) / len(fc.data))  # just average of random numbers

if __name__ == "__main__":
    main()
