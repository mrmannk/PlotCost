import flet as ft

def main(page: ft.Page):
    # Define a function to handle the price estimation button click
    def on_clicked_estimate_price(e):
        # Access user input from UI elements
        try:
            area = int(page.get_control("uiSqft").value)
            bhk = int(page.get_control("uiBHK").value)
            bath = int(page.get_control("uiBathrooms").value)
            location = page.get_control("uiLocations").value
        except ValueError:
            page.controls["uiEstimatedPrice"].content.text = "Invalid input. Please enter numbers for area."
            return

        # Replace this with your actual price estimation logic (using a model or API)
        estimated_price = "Rs. " + str(int(area) * 1000)  # Placeholder estimation
        page.controls["uiEstimatedPrice"].content.text = f"Estimated Price: {estimated_price}"

    # Create the main app layout
    page.add(
        ft.Column(
            controls=[
                ft.Image(src="https://placeimg.com/640/480/arch", fit=ft.ImageFit.CONTAIN),
                ft.Text(value="Bangalore Home Price Prediction", size=30, center=True),
                ft.Row(
                    controls=[
                        ft.Text(value="Area (Square Feet):"),
                        ft.TextField(label="", value="1000", width=100, id="uiSqft"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                ft.Text(value="BHK:", anchor=ft.Anchor.END),
                ft.Row(
                    controls=[
                        ft.RadioButton(value="1", label="1", id="radio-bhk-1", name="uiBHK"),
                        ft.RadioButton(value="2", label="2", id="radio-bhk-2", name="uiBHK", checked=True),
                        ft.RadioButton(value="3", label="3", id="radio-bhk-3", name="uiBHK"),
                        ft.RadioButton(value="4", label="4", id="radio-bhk-4", name="uiBHK"),
                        ft.RadioButton(value="5", label="5", id="radio-bhk-5", name="uiBHK"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                ft.Text(value="Bath:", anchor=ft.Anchor.END),
                ft.Row(
                    controls=[
                        ft.RadioButton(value="1", label="1", id="radio-bath-1", name="uiBathrooms"),
                        ft.RadioButton(value="2", label="2", id="radio-bath-2", name="uiBathrooms", checked=True),
                        ft.RadioButton(value="3", label="3", id="radio-bath-3", name="uiBathrooms"),
                        ft.RadioButton(value="4", label="4", id="radio-bath-4", name="uiBathrooms"),
                        ft.RadioButton(value="5", label="5", id="radio-bath-5", name="uiBathrooms"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                ft.Text(value="Location:"),
                ft.Dropdown(
                    options=[
                        ft.DropdownOption(value="", label="Choose a Location"),
                        ft.DropdownOption(value="Electronic City", label="Electronic City"),
                        ft.DropdownOption(value="Rajaji Nagar", label="Rajaji Nagar"),
                    ],
                    value="",
                    id="uiLocations",
                ),
                ft.ElevatedButton("Estimate Price", on_click=on_clicked_estimate_price),
                ft.Text(id="uiEstimatedPrice", content=ft.TextValue(text="")),
            ],
            spacing=20,
            padding=20,
        )
    )


ft.app(target=main)
