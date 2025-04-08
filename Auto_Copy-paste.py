"""
# Base code
import pyperclip as pc

txt1 = input("Enter a text : ")
pc.copy(txt1)

txt2 = pc.paste()

print(txt2)"""

# Modified with some functionalities
import pyperclip as pc  

class ClipboardManager:  
    def __init__(self):  
        self.history = []  

    def copy_text(self):  
        text = input("Enter the text to copy: ").strip()  
        if text:  
            # Apply formatting if necessary  
            format_choice = input("Format options: (1) Uppercase (2) Lowercase (3) None: ")  
            if format_choice == '1':  
                text = text.upper()  
            elif format_choice == '2':  
                text = text.lower()  

            pc.copy(text)  
            self.history.append(text)  
            print("Text copied to clipboard!")  

    def paste_text(self):  
        text = pc.paste()  
        print(f"Pasted text: {text}")  

    def clear_clipboard(self):  
        pc.copy("")  # Clear the clipboard  
        print("Clipboard cleared!")  

    def show_history(self):  
        if self.history:  
            print("Clipboard History:")  
            for i, text in enumerate(self.history, 1):  
                print(f"{i}: {text}")  
        else:  
            print("No history available.")  

    def save_to_file(self):  
        text = input("Enter the text to save to file: ").strip()  
        if text:  
            file_name = input("Enter the filename (without extension): ") + ".txt"  
            with open(file_name, 'w') as file:  
                file.write(text)  
            print(f"Text saved to {file_name}.")  
        else:  
            print("No text to save!")  

def main():  
    manager = ClipboardManager()  
    
    while True:  
        print("\nOptions:")  
        print("1. Copy text")  
        print("2. Paste text")  
        print("3. Show clipboard history")  
        print("4. Clear clipboard")  
        print("5. Save to file")  
        print("6. Exit")  
        
        choice = input("Choose an option (1-6): ")  
        
        if choice == '1':  
            manager.copy_text()  
        elif choice == '2':  
            manager.paste_text()  
        elif choice == '3':  
            manager.show_history()  
        elif choice == '4':  
            manager.clear_clipboard()  
        elif choice == '5':  
            manager.save_to_file()  
        elif choice == '6':  
            print("Exiting the Clipboard Manager. Goodbye!")  
            break  
        else:  
            print("Invalid choice, please try again.")  

if __name__ == "__main__":  
    main()