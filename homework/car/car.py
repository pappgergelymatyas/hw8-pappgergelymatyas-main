class Car:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.direction = 0.0

    def deg_to_rad(self, degrees: float) -> float:
        return degrees * 3.141592653589793 / 180.0

    def rotate(self, degrees: int):
        self.direction = (self.direction + degrees) % 360
        if self.direction < 0:
            self.direction += 360

    def move(self, distance: float):
        radians = self.deg_to_rad(self.direction)
        self.x += distance * self.cos(radians)
        self.y += distance * self.sin(radians)

    def cos(self, radians: float) -> float:
        return 1 - radians**2 / 2 + radians**4 / 24 - radians**6 / 720

    def sin(self, radians: float) -> float:
        return radians - radians**3 / 6 + radians**5 / 120 - radians**7 / 5040

    def process(self, command: str):
        action = command[0]
        value = int(command[1:])
        
        if action == 'M':
            self.move(value)
        elif action == 'R':
            self.rotate(value)

    def __repr__(self):
        return f"Car(x={self.x:.2f}, y={self.y:.2f}, direction={self.direction:.2f}°)"
pass
