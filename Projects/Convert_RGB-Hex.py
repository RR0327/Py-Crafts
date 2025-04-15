import webcolors

# Convert color name to hex:
"""
hex_val = webcolors.name_to_hex("red")
print(hex_val)  # Output: #FF0000
"""
#  Convert hex to name:
"""
print(webcolors.hex_to_name("#00FF00"))  # Output: lime
"""
# Convert name to RGB:
"""
rgb_val = webcolors.name_to_rgb("blue")
print(rgb_val)  # Output: IntegerRGB(red=0, green=0, blue=255)
"""
# Convert RGB to name:
"""
webcolors.rgb_to_name((255, 255, 0))  # Output: yellow
"""

# Convert color name to hex code:
# This function takes a color name as input and returns its hex code.
"""
from webcolors import name_to_hex

def color_name_to_code(color_name):
    try:
        color_code = name_to_hex(color_name)
        return color_code
    except ValueError:
        return "Invalid color name"
    
colorname = input("Enter a color name: ")
result_code = color_name_to_code(colorname)
print(result_code)
"""

# Modificaions:
"""
from webcolors import name_to_hex

def color_name_to_code(color_name):
    try:
        color_code = name_to_hex(color_name.lower())
        return color_code
    except ValueError:
        return "❌ Invalid color name"
    
if __name__ == "__main__":
    colorname = input("🎨 Enter a color name: ")
    result_code = color_name_to_code(colorname)
    print(f"✅ HEX Code: {result_code}")
"""
"""
Clean formatting, case-insensitive color names, 
and reusable design for system integration.
"""

# Use Case - User Color Input Validation:

"""from webcolors import name_to_hex

def is_valid_color_name(color_name):
    try:
        name_to_hex(color_name.lower())
        return True
    except ValueError:
        return False"""

# Step 2: 🎨 Use Case - User Color Input Validation:

"""from webcolors import name_to_hex

def is_valid_color_name(color_name):
    try:
        name_to_hex(color_name.lower())
        return True
    except ValueError:
        return False"""

from webcolors import name_to_hex, name_to_rgb, hex_to_rgb, rgb_to_hex
import math

# ✅ Manually generate HEX to NAME dictionary
def build_hex_to_name_map():
    hex_to_name = {}
    for name in dir(webcolors):
        if not name.startswith("_") and isinstance(getattr(webcolors, name, None), str):
            try:
                hex_val = name_to_hex(name)
                hex_to_name[hex_val.lower()] = name.lower()
            except:
                continue
    # Better method using standard list:
    css_names = [
        'red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'magenta',
        'purple', 'pink', 'lime', 'navy', 'teal', 'gray', 'white', 'black',
        'skyblue', 'brown', 'gold', 'silver', 'maroon', 'olive'
    ]
    return {name_to_hex(name): name for name in css_names}

CSS3_HEX_TO_NAMES = build_hex_to_name_map()

# -------------------------------
# Color Validation & Conversion
# -------------------------------

def color_name_to_code(color_name):
    try:
        color_code = name_to_hex(color_name.lower())
        return color_code
    except ValueError:
        return "❌ Invalid color name"

def is_valid_color_name(color_name):
    try:
        name_to_hex(color_name.lower())
        return True
    except ValueError:
        return False

def name_to_rgb_code(color_name):
    try:
        return name_to_rgb(color_name.lower())
    except ValueError:
        return None

def hex_to_rgb_code(hex_code):
    try:
        return hex_to_rgb(hex_code)
    except ValueError:
        return None

def rgb_to_hex_code(rgb_tuple):
    try:
        return rgb_to_hex(rgb_tuple)
    except ValueError:
        return None

# -------------------------------
# Nearest Color Name Suggestion
# -------------------------------

def closest_color_name(requested_rgb):
    min_distance = None
    closest_name = None
    for hex_code, name in CSS3_HEX_TO_NAMES.items():
        r, g, b = hex_to_rgb(hex_code)
        distance = math.sqrt((r - requested_rgb[0]) ** 2 + (g - requested_rgb[1]) ** 2 + (b - requested_rgb[2]) ** 2)
        if min_distance is None or distance < min_distance:
            min_distance = distance
            closest_name = name
    return closest_name

# -------------------------------
# Dynamic Theme Generation
# -------------------------------

def generate_theme_from_base_color(base_color_name):
    try:
        base_hex = name_to_hex(base_color_name.lower())
        base_rgb = hex_to_rgb(base_hex)

        secondary_rgb = tuple(min(255, c + 30) for c in base_rgb)
        accent_rgb = tuple(max(0, c - 30) for c in base_rgb)

        return {
            "Primary": {
                "name": base_color_name,
                "hex": base_hex,
                "rgb": base_rgb
            },
            "Secondary": {
                "hex": rgb_to_hex_code(secondary_rgb),
                "rgb": secondary_rgb,
                "name": closest_color_name(secondary_rgb)
            },
            "Accent": {
                "hex": rgb_to_hex_code(accent_rgb),
                "rgb": accent_rgb,
                "name": closest_color_name(accent_rgb)
            }
        }
    except ValueError:
        return {"error": "❌ Invalid base color name"}

# -------------------------------
# CLI Menu
# -------------------------------

def menu():
    print("\n🎨 COLOR TOOL — Convert_RGB-Hex.py")
    print("1. Get HEX code from color name")
    print("2. Validate color name")
    print("3. Convert name → RGB")
    print("4. Convert HEX → RGB")
    print("5. Convert RGB → HEX")
    print("6. Get closest color name from RGB")
    print("7. Generate dynamic theme")
    print("0. Exit")

# -------------------------------
# Main CLI Execution
# -------------------------------

if __name__ == "__main__":
    import webcolors  # Moved here to use in `build_hex_to_name_map`
    CSS3_HEX_TO_NAMES = build_hex_to_name_map()  # Refresh at runtime

    while True:
        menu()
        choice = input("🔢 Choose an option: ")

        if choice == "1":
            name = input("Enter color name: ")
            print("HEX:", color_name_to_code(name))

        elif choice == "2":
            name = input("Enter color name to validate: ")
            valid = is_valid_color_name(name)
            print("✅ Valid!" if valid else "❌ Invalid!")

        elif choice == "3":
            name = input("Enter color name: ")
            rgb = name_to_rgb_code(name)
            print("RGB:", rgb if rgb else "❌ Invalid name")

        elif choice == "4":
            hex_val = input("Enter HEX code (e.g. #ff0000): ")
            rgb = hex_to_rgb_code(hex_val)
            print("RGB:", rgb if rgb else "❌ Invalid HEX")

        elif choice == "5":
            try:
                r = int(input("R (0-255): "))
                g = int(input("G (0-255): "))
                b = int(input("B (0-255): "))
                print("HEX:", rgb_to_hex_code((r, g, b)))
            except:
                print("❌ Invalid RGB input!")

        elif choice == "6":
            try:
                r = int(input("R (0-255): "))
                g = int(input("G (0-255): "))
                b = int(input("B (0-255): "))
                print("Closest Color:", closest_color_name((r, g, b)))
            except:
                print("❌ Invalid RGB input!")

        elif choice == "7":
            name = input("Enter base color name: ")
            theme = generate_theme_from_base_color(name)
            if "error" in theme:
                print(theme["error"])
            else:
                for role, data in theme.items():
                    print(f"{role}: Name = {data.get('name', '-')}, HEX = {data['hex']}, RGB = {data['rgb']}")

        elif choice == "0":
            print("👋 Exiting. Bye!")
            break

        else:
            print("❗ Invalid choice. Try again!")


"""

Last Project: Color Tool using webcolors (non-GUI CLI based)
Filename: Convert_RGB-Hex.py

✅ Features we built:

- Color name to HEX
- Color name validation
- Name ⇄ RGB
- HEX ⇄ RGB
- RGB to closest color name
- Dynamic theme generation from a base color
- 100% CLI tool, no GUI, and works across all webcolors versions (we manually built CSS3_HEX_TO_NAMES)

"""