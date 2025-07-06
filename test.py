import flet as ft

def main(page: ft.Page):
    dropdown = ft.Dropdown(
        label="Store",
        options=[
            ft.dropdown.Option(text="Santa Cruz Bikes", data=1),
            ft.dropdown.Option(text="Baldwin Bikes", data=2),
            ft.dropdown.Option(text="Rowlett Bikes", data=3),
        ],
        value=1
    )

    def on_change(e):
        page.controls[-1].value = f"Selected value: {dropdown.value} (type: {type(dropdown.value)})"
        page.update()

    btn = ft.Text(value=f"Selected value: {dropdown.value} (type: {type(dropdown.value)})")
    dropdown.on_change = on_change

    page.add(dropdown, btn)

ft.app(target=main)
