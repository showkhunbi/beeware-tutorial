"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, flex=1))

        image = toga.ImageView(
            image="./resources/DELANIBLOGPNG.png", style=Pack(width=200, height=75, flex=1, alignment="left", padding=(10, 100, 10, 100)))
        imageBox = toga.Box(style=Pack(
            alignment="right", direction=COLUMN))
        imageBox.add(image)

        info_Box = toga.Box(style=Pack(
            padding=(5, 20), alignment="center", direction=COLUMN, text_align="center"))
        app_description = toga.Label(
            'Get Blog posts on the click of one button',
            style=Pack(padding=(0, 5), text_align="center")
        )
        info_Box.add(app_description)

        select_Box = toga.Box(style=Pack(
            padding=(5, 20), direction=COLUMN, alignment="center", text_align="center"))
        select = toga.Selection(items=["Home", "Music", "Entertainment", "Videos",
                                       "Album & EP", "Lyrics", "Mixtape", "Trending"],
                                style=Pack(alignment="center", flex=1, text_align="center", padding_top=10, height=30))

        page_number = toga.NumberInput(
            min_value=0, style=Pack(padding_top=30, height=30))

        submit_button = toga.Button(
            "Get Posts", on_press=self.say_hello, style=Pack(padding_top=30, height=50))

        select_Box.add(select)
        select_Box.add(page_number)
        select_Box.add(submit_button)

        credit_Box = toga.Box(style=Pack(
            padding=(100, 20, 0, 20), alignment="center", direction=COLUMN, text_align="center"))

        editor_button = toga.Button(
            "Open Text Editor", on_press=self.text_editor, style=Pack(height=30))
        credit = toga.Label(
            "Developed by Johnson Cooper",
            style=Pack(padding=(0, 5), text_align="center")
        )
        phone = toga.Label(
            "08139002724",
            style=Pack(padding=(0, 5), text_align="center")
        )
        credit_Box.add(editor_button)
        credit_Box.add(credit)
        credit_Box.add(phone)

        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )

        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(
            direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(imageBox)
        main_box.add(info_Box)
        main_box.add(select_Box)
        main_box.add(credit_Box)
        main_box.add(name_box)
        main_box.add(button)

        select.style.update(alignment="center")

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        self.main_window.size = (400, 500)

    def text_editor(self, *args, **kwargs):
        box = toga.Box(style=Pack(direction=COLUMN))
        editor = toga.MultilineTextInput(style=Pack(flex=1))
        copy_button = toga.Button(
            "Copy Text", on_press=self.say_hello, style=Pack(height=30))
        box.add(editor)
        box.add(copy_button)

        self.window = toga.Window('my window', title='This is a window!')
        self.window.content = box
        self.window.show()

    def say_hello(self, widget):
        if self.name_input.value:
            name = self.name_input.value
        else:
            name = 'stranger'

        self.main_window.info_dialog(
            'Hi there!',
            "Hello, {}".format(name)
        )
        self.text_editor()


def main():
    return HelloWorld()
