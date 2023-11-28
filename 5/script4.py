class Human:
    def __init__(self, name, age, proff, hobby):
        self.name = name
        self.age = age
        self.proff = proff
        self.hobby = hobby
        self.status = self._set_status()
        pass
    def _set_status(self):
        if self.age < 18:
            return "kid"