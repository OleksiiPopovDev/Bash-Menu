from bash_menu_builder.dto.command_option_dto import CommandOptionDto


class MenuItemDto:
    def __init__(
            self,
            title: str,
            handler: object,
            option: CommandOptionDto = None,
    ):
        self.title: str = title
        self.handler: object = handler
        self.option: CommandOptionDto = option
