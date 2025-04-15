import math
import webcolors
from webcolors import name_to_hex, name_to_rgb, hex_to_rgb, rgb_to_hex

# ✅ Build HEX-to-NAME map safely (no missing var issue)
def build_hex_to_name_map():
    css_names = [
        'red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'magenta',
        'purple', 'pink', 'lime', 'navy', 'teal', 'gray', 'white', 'black',
        'skyblue', 'brown', 'gold', 'silver', 'maroon', 'olive'
    ]
    return {name_to_hex(name): name for name in css_names}

# 🛡️ This will always be initialized at runtime
CSS3_HEX_TO_NAMES = build_hex_to_name_map()

# -------------------------------
# Color Conversion Utilities
# -------------------------------

def color_name_to_code(color_name):
    try:
        return name_to_hex(color_name.lower())
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
        return hex_to_rgb(hex_code.strip())
    except ValueError:
        return None

def rgb_to_hex_code(rgb_tuple):
    try:
        return rgb_to_hex(rgb_tuple)
    except ValueError:
        return None

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
