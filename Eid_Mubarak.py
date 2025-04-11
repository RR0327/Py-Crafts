# List Available Fonts
"""
from pyfiglet import Figlet

f = Figlet()
fonts = f.getFonts()
print(fonts[:10])
"""


# Example of using pyfiglet to create ASCII art text
"""
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hello, World!")
print(ascii_banner)
"""

# Example of using pyfiglet with a custom font
"""
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Custom Font!'))
"""
# Example of using pyfiglet with a custom font and width
"""
from colorama import init, Fore, Back, Style

init()  # Initialize colorama for Windows support

print(Fore.RED + 'This is red text')
print(Back.YELLOW + 'This has a yellow background')
print(Style.BRIGHT + 'Bright style text')
print(Style.RESET_ALL + 'Back to normal')
"""

# Color Options
"""
Fore (Text Color):

Fore.BLACK
Fore.RED
Fore.GREEN
Fore.YELLOW
Fore.BLUE
Fore.MAGENTA
Fore.CYAN
Fore.WHITE
Fore.RESET

Back (Background Color):

Back.RED
Back.YELLOW
Back.BLUE
Back.RESET

Style (Text Style):

Style.DIM
Style.NORMAL
Style.BRIGHT
Style.RESET_ALL

"""

# Reset is Important
# Always use Style.RESET_ALL or Fore.RESET etc. to go back to normal, otherwise your console might keep using the color.

# Eid Mubarak ASCII Art with Colors
"""
from pyfiglet import Figlet
from colorama import init, Fore

init()

f = Figlet(font='slant')
print(Fore.CYAN + f.renderText('Eid Mubarak!') + Fore.RESET)
print(Fore.YELLOW + f.renderText('Eid Mubarak!') + Fore.RESET)
print(Fore.GREEN + f.renderText('Eid Mubarak!') + Fore.RESET)
print(Fore.MAGENTA + f.renderText('Eid Mubarak!') + Fore.RESET)
print(Fore.RED + f.renderText('Eid Mubarak!') + Fore.RESET)
print(Fore.BLUE + f.renderText('Eid Mubarak!') + Fore.RESET)
print(Fore.WHITE + f.renderText('Eid Mubarak!') + Fore.RESET)
"""
# Eid Mubarak ASCII Art with Colors and Different Fonts
"""
from colorama import Fore
import pyfiglet

font = pyfiglet.figlet_format('Eid Mubarak')

print(Fore.GREEN+font)
print(Fore.YELLOW+font)
print(Fore.RED+font)
print(Fore.BLUE+font)
print(Fore.CYAN+font)
print(Fore.MAGENTA+font)
print(Fore.WHITE+font)
print(Fore.BLACK+font)
print(Fore.RESET+font)
"""

