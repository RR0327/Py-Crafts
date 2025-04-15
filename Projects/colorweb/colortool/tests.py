from django.test import TestCase
from .utils import (
    color_name_to_code, name_to_rgb_code, hex_to_rgb_code,
    rgb_to_hex_code, closest_color_name, generate_theme_from_base_color
)

class ColorToolUtilsTest(TestCase):

    def test_color_name_to_code(self):
        self.assertEqual(color_name_to_code("red"), "#ff0000")
        self.assertEqual(color_name_to_code("invalidcolor"), "❌ Invalid color name")

    def test_name_to_rgb_code(self):
        self.assertEqual(name_to_rgb_code("red"), (255, 0, 0))
        self.assertIsNone(name_to_rgb_code("invalidcolor"))

    def test_hex_to_rgb_code(self):
        self.assertEqual(hex_to_rgb_code("#ff0000"), (255, 0, 0))
        self.assertIsNone(hex_to_rgb_code("not-a-color"))

    def test_rgb_to_hex_code(self):
        self.assertEqual(rgb_to_hex_code((0, 128, 128)), "#008080")

    def test_closest_color_name(self):
        self.assertEqual(closest_color_name((250, 0, 0)), "red")

    def test_generate_theme(self):
        theme = generate_theme_from_base_color("blue")
        self.assertIn("Primary", theme)
        self.assertIn("Secondary", theme)
        self.assertIn("Accent", theme)
