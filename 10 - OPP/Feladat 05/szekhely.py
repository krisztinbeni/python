class Szekhely:
    
    def __init__(self, telepules: str, iranyitoszam: int, cim: str, megye: str):
        super().__init__()

        self.telepules: str = telepules
        self.iranyitoszam: int = iranyitoszam
        self.cim: str = cim
        self.megye: str = megye

    def __str__(self) -> str:
        return f"Település adatai:\n\tnév: {self.telepules}\n\tirányítószám: {self.iranyitoszam}\n\tcím: {self.cim}\n\tmegye: {self.megye}\n"