import time

from bash_menu_builder import input_menu, select_menu
from bash_menu_builder.dto import command_option_dto, menu_item_dto


def banner_text() -> str:
    return '\t\tI\'m Banner Text\n\n'


def function_one() -> None:
    print('Some process ...')
    time.sleep(2)
    print('Result of Script One\n')


def function_two() -> None:
    print('Some process ...')
    time.sleep(2)
    print('Result of Script Two\n')


def function_three(argument: str) -> None:
    print('Some process ...')
    time.sleep(2)
    print('Result of Script Three')
    print('Argument: %s\n' % argument)


def menu_list() -> list[menu_item_dto.MenuItemDto]:
    return [
        menu_item_dto.MenuItemDto(
            title='Menu Item One',
            option=command_option_dto.CommandOptionDto(
                long_option='one',
                short_option='o'
            ),
            handler=function_one
        ),
        menu_item_dto.MenuItemDto(
            title='Menu Item Two',
            option=command_option_dto.CommandOptionDto(
                long_option='two',
                short_option='t'
            ),
            handler=function_two
        ),
        menu_item_dto.MenuItemDto(
            title='Menu Item Three',
            option=command_option_dto.CommandOptionDto(
                long_option='three',
                short_option='r',
                has_value=True
            ),
            handler=function_three
        ),
    ]


def select_menu_view() -> None:
    select_menu.SelectMenu(
        menu=menu_list(),
        banner=banner_text()
    )


def input_menu_view() -> None:
    input_menu.InputMenu(
        menu=menu_list(),
        banner=banner_text()
    )


if __name__ == '__main__':
    input_menu_view()
    # select_menu_view()
