from bash_menu_builder import input_menu, select_menu, menu_item_dto
import time


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


def function_three() -> None:
    print('Some process ...')
    time.sleep(2)
    print('Result of Script Three\n')


def select_menu_view() -> None:
    select_menu.SelectMenu(
        menu=[
            menu_item_dto.MenuItemDto(title='Menu Item One', option='one', handler=function_one),
            menu_item_dto.MenuItemDto(title='Menu Item Two', option='two', handler=function_two),
            menu_item_dto.MenuItemDto(title='Menu Item Three', option='three', handler=function_three),
        ],
        banner=banner_text()
    )


def input_menu_view() -> None:
    input_menu.InputMenu(
        menu=[
            menu_item_dto.MenuItemDto(title='Menu Item One', option='one', handler=function_one),
            menu_item_dto.MenuItemDto(title='Menu Item Two', option='two', handler=function_two),
            menu_item_dto.MenuItemDto(title='Menu Item Three', option='three', handler=function_three),
        ],
        banner=banner_text()
    )


if __name__ == '__main__':
    #input_menu_view()
    select_menu_view()
