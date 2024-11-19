import time

from bash_menu_builder import input_menu, select_menu, Draw
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
    Message.error(
        message='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
            '\nLorem Ipsum has been the industry\'s standard dummy text ever since the 1500s,'
            '\nwhen an unknown printer took a galley of type and scrambled it to make a type specimen book. '
    )
    Message.set_tabs(1)
    Message.warning(
        message='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
            '\nLorem Ipsum has been the industry\'s standard dummy text ever since the 1500s,'
            '\nwhen an unknown printer took a galley of type and scrambled it to make a type specimen book. '
    )
    Message.set_tabs(2)
    Message.success(
        message='Lorem Ipsum is simply dummy text of the printing and typesetting industry...'
            '\nLorem Ipsum has been the industry\'s standard dummy text ever since the 1500s,'
            '\nwhen an unknown printer took a galley of type and scrambled it to make a type specimen book. ',
        title='Custom Success Title'
    )
    print(Draw.paint(
        '{Red}Lorem Ipsum {Green}is simply {Blue}dummy text of the {Yellow}printing and typesetting industry...'
        '\n{Purple}Lorem Ipsum has been the {Cyan}industry\'s standard dummy {White}text ever since the 1500s,'
        '\n{BBlue}when an unknown {BBlack}printer took a galley {BRed}of type and scrambled it {BPurple}to make a type specimen book. '
        '\n{UGreen}It has survived not only five centuries, {UYellow}but also the leap into electronic typesetting, {UCyan}remaining essentially unchanged.'
        '\n{On_Blue}It was popularised {On_Yellow}in the 1960s with {IGreen}the release of Letraset sheets {IWhite}containing Lorem Ipsum passages, and more '
        '\n{BIRed}recently with {BIYellow}desktop publishing {ColorOff}software like Aldus PageMaker including versions of Lorem Ipsum.'
    ))
    # exit()
    input_menu_view()
    # select_menu_view()
