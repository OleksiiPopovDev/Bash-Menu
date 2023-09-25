from bash_menu_builder import input_menu, select_menu, menu_item_dto
from bash_menu_builder.draw import Draw


def test():
    print('Test')
    Draw.separator('=')


def test2():
    print('Test2')
    Draw.separator('.')


def test3():
    print('Test3')
    Draw.separator('+')


if __name__ == '__main__':
    select_menu.SelectMenu(
        menu=[
            menu_item_dto.MenuItemDto(title='Test', option_name='test', handler=test),
            menu_item_dto.MenuItemDto(title='Test2', option_name='test2', handler=test2),
            menu_item_dto.MenuItemDto(title='Test3', option_name='test3', handler=test3),
        ],
        banner='\n\n\t\t\tBANNER'
    )
    exit()
    input_menu.InputMenu(
        menu=[
            menu_item_dto.MenuItemDto(title='Test', option_name='test', handler=test),
            menu_item_dto.MenuItemDto(title='Test2', option_name='test2', handler=test2),
            menu_item_dto.MenuItemDto(title='Test3', option_name='test3', handler=test3),
        ],
        banner='\n\n\t\t\tBANNER'
    )
