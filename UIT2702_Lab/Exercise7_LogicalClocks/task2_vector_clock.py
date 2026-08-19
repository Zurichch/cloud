# Task 2 - Vector Clocks
# Run: python task2_vector_clock.py
class VectorClock:
    def __init__(self, pid, n):
        self.pid = pid
        self.n = n
        self.vector = [0] * n

    def internal_event(self):
        self.vector[self.pid] += 1
        print(f"Process {self.pid} internal event -> {self.vector}")

    def send_event(self):
        self.vector[self.pid] += 1
        print(f"Process {self.pid} sends message -> {self.vector}")
        return list(self.vector)

    def receive_event(self, received_vector):
        for i in range(self.n):
            self.vector[i] = max(self.vector[i], received_vector[i])
        self.vector[self.pid] += 1
        print(f"Process {self.pid} received message -> {self.vector}")

# Example simulation with 3 processes
P0 = VectorClock(0, 3)
P1 = VectorClock(1, 3)
P2 = VectorClock(2, 3)

P0.internal_event()      # E1
msg = P0.send_event()    # E2 send -> P1
P1.receive_event(msg)    # E3 receive
P2.internal_event()      # E4
P1.send_event()          # E5 send -> P2
P2.receive_event(P1.vector)  # E6 receive
