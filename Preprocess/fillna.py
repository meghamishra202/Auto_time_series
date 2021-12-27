class te:
    def __init__(self):
        self.X_train=None
        self.target=None
        self.column=None
    def fill(self, X, y, time):
        self.X_train=X
        self.target=y
        self.column=time

