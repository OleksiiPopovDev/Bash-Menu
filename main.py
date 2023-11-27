import time

from bash_menu_builder import input_menu, select_menu
from bash_menu_builder.dto import command_option_dto, menu_item_dto
from bash_menu_builder.message import Message


def banner_text() -> str:
    return '\t\tI\'m Banner Text\n\n'


def function_one() -> None:
    print('Some process ...')
    time.sleep(1)
    print('Result of Script One\n')


def function_two() -> None:
    print('Some process ...')
    time.sleep(1)
    print('Result of Script Two\n')


def function_three() -> None:
    print('Some process ...')
    time.sleep(1)
    print('Result of Script Three\n')


def function_four(argument: str) -> None:
    print('Some process ...')
    time.sleep(1)
    print('Result of Script Four')
    print('Argument: %s\n' % argument)


def menu_list() -> list[menu_item_dto.MenuItemDto]:
    return [
        menu_item_dto.MenuItemDto(
            title='Menu Item One',
            option=command_option_dto.CommandOptionDto(
                long_option='one',
                short_option='o',
            ),
            handler=function_one,
            priority=2
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
                short_option='r'
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
    list_items: list[menu_item_dto.MenuItemDto] = menu_list()
    list_items.append(menu_item_dto.MenuItemDto(
        title='Menu Item Four',
        option=command_option_dto.CommandOptionDto(
            long_option='four',
            short_option='f',
            has_value=True
        ),
        handler=function_four
    ))

    input_menu.InputMenu(
        menu=list_items,
        banner=banner_text()
    )


if __name__ == '__main__':
    Message.error(message='This is Error Message for test New length string \nTest')
    Message.set_tabs(1)
    Message.warning(message='This is Error Message for test New length string \nTest')
    Message.set_tabs(2)
    Message.success(title='Some Title Text', message='This is Error \nMessage')
    # exit()
    # input_menu_view()
    select_menu_view()
