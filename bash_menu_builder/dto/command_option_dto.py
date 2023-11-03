class CommandOptionDto:
    def __init__(
            self,
            long_option: str,
            short_option: str,
            has_value: bool = False
    ):
        self.long_option: str = long_option.replace(' ', '')
        self.short_option: str = short_option.replace(' ', '')
        self.has_value: bool = has_value
