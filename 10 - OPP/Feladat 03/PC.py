class PC:

    def __init__(self, alaplap: str, memoria: str, hutes: str, processzor: str, tapegyseg: str) -> None:
        super().__init__()

        self.alaplap = alaplap
        self.memoria = memoria
        self.hutes = hutes
        self.processzor = processzor
        self.tapegyseg = tapegyseg

    def __str__(self) -> str:
        return f"alaplap: {self.alaplap}\nmemória: {self.memoria}\nhűtés: {self.hutes}\nprocesszor: {self.processzor}\ntápegység: {self.tapegyseg}"