class NextObserver:
    def __init__(self) -> None:
        self._is_change = False
        self.history = ''

    def forward(self, next_puyo_color: str) -> None:
        if 0 < next_puyo_color.count('_') < 4:
            return

        is_change = False if next_puyo_color.count('_') else True
        if not self._is_change and is_change:
            self.history += next_puyo_color[:2]
        self._is_change = is_change
