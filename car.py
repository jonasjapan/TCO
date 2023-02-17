class Car():
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.brand: str = ""
        

    def __str__(self) -> str:
        return f"car named: {self.name}"