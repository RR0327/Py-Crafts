import periodictable

def get_element_info(symbol):
    element = getattr(periodictable, symbol, None)

    if element:
        print(f"Element: {element.name}")
        print(f"Symbol: {element.symbol}")
        print(f"Atomic Number: {element.number}")
        print(f"Atomic Mass: {element.mass} u")

    else:
        print("Element not found in the periodic table.")

if __name__ == "__main__":
    symbol = input("Enter the Element: ").capitalize()
    get_element_info(symbol)