import operator
import os
import sys
from PyQt6.QtGui import QFont, QAction
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QApplication, QWidget, QMenu, \
    QMenuBar


# Define the main CalculatorApp class which inherits from QMainWindow
class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize the superclass
        self.setObjectName("light")  # Set the default theme to light
        self.initializeUI()  # Set up the UI components
        self.createMenu()  # Create the menu bar
        self.createDisplay()  # Create the display where results are shown
        self.createButtons()  # Create the calculator buttons
        self.loadStyles()  # Load the stylesheet for the app

        # A dictionary mapping the operation symbols to their corresponding functions
        self.operations = {
            '÷': operator.truediv,
            '×': operator.mul,
            '−': operator.sub,
            '+': operator.add
        }

    # Method to initialize the UI
    def initializeUI(self):
        self.setWindowTitle('Hesap Makinesi')  # Set the window title
        self.setGeometry(100, 100, 450, 550)  # Set the initial position and size
        self.setMinimumSize(450, 550)  # Set the minimum size

        # Create a central widget and set it as the central widget of the window
        self.container = QWidget()
        self.setCentralWidget(self.container)

        # Create a QVBoxLayout and set it for the container
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)

    # Method to create the menu bar
    def createMenu(self):
        menu_bar = QMenuBar()  # Create a QMenuBar
        self.setMenuBar(menu_bar)  # Set it as the menu bar of the window

        # Create a "File" menu
        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)

        # Add an "Exit" action to the "File" menu
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)  # Connect the action to close the window
        file_menu.addAction(exit_action)

        # Create a "Settings" menu with theme options
        settings_menu = QMenu("&Settings", self)
        menu_bar.addMenu(settings_menu)
        theme_menu = QMenu("App Theme", self)
        settings_menu.addMenu(theme_menu)

        # Add "Light" and "Dark" theme options to the "App Theme" menu
        light_theme_action = QAction("Light", self)
        light_theme_action.triggered.connect(lambda: self.setAppTheme("light"))
        theme_menu.addAction(light_theme_action)

        dark_theme_action = QAction("Dark", self)
        dark_theme_action.triggered.connect(lambda: self.setAppTheme("dark"))
        theme_menu.addAction(dark_theme_action)

    # Method to load the styles from the QSS file
    def loadStyles(self):
        try:
            # Executable'ın bulunduğu dizini bul
            base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

            # style.qss dosyasının yolunu oluştur
            style_file_path = os.path.join(base_path, "style.qss")

            # Dosyayı aç ve içeriğini oku
            with open(style_file_path, "r") as stylefile:
                self.setStyleSheet(stylefile.read())  # Apply the stylesheet to the app
        except Exception as e:
            print(f"Error loading style.qss: {e}")

    # Method to set the application theme
    def setAppTheme(self, theme):
        self.setObjectName(theme)  # Set the object name to the chosen theme
        self.loadStyles()  # Reload the styles to apply the new theme
        # Refresh styles for each widget
        for widget in self.findChildren(QWidget):
            widget.setStyle(widget.style())

    # Method to create the display (QLineEdit)
    def createDisplay(self):
        self.result_field = QLineEdit()
        self.result_field.setReadOnly(True)  # Make it read-only
        self.result_field.setFont(QFont('Arial', 24))  # Set the font
        self.result_field.setMinimumWidth(200)  # Set a minimum width
        self.layout.addWidget(self.result_field)  # Add it to the layout

    def createButtons(self):
        """Create the buttons."""
        buttons = [
            ['7', '8', '9', '÷'],
            ['4', '5', '6', '×'],
            ['1', '2', '3', '−'],
            ['0', '.', '=', '+']
        ]

        # Create a horizontal layout for the Clear and Backspace buttons
        control_buttons_layout = QHBoxLayout()

        clear_button = QPushButton('Clear')
        clear_button.setFixedSize(100, 50)
        clear_button.clicked.connect(self.clear_result_field)
        control_buttons_layout.addWidget(clear_button)  # Add to horizontal layout

        backspace_button = QPushButton('⌫')
        backspace_button.setFixedSize(100, 50)
        backspace_button.clicked.connect(self.handle_backspace)
        control_buttons_layout.addWidget(backspace_button)  # Add to horizontal layout

        clear_button.setObjectName("clearButton")
        backspace_button.setObjectName("backspaceButton")

        # Add the horizontal layout to the main vertical layout
        self.layout.addLayout(control_buttons_layout)

        for row in buttons:
            button_sizer = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.setFixedSize(100, 100)
                button.clicked.connect(self.on_button_click)
                button_sizer.addWidget(button)
            self.layout.addLayout(button_sizer)

    def on_button_click(self, s):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            expression = self.result_field.text()
            for op_symbol, op_function in self.operations.items():
                if op_symbol in expression:
                    operands = expression.split(op_symbol)
                    try:
                        operand1 = float(operands[0])
                        operand2 = float(operands[1])
                        result = op_function(operand1, operand2)
                        self.result_field.setText(str(result))
                    except ZeroDivisionError:
                        self.result_field.setText("Cannot divide by zero!")
                    except Exception as e:
                        self.result_field.setText("Invalid input!")
                    return

        else:
            current_text = self.result_field.text()
            new_text = current_text + button_text
            self.result_field.setText(new_text)

    def handle_backspace(self):
        current_text = self.result_field.text()
        new_text = current_text[:-1]  # Remove the last character
        self.result_field.setText(new_text)

    def clear_result_field(self):
        self.result_field.clear()

    # Additional functionality to update the button styles
    def updateButtonStyles(self):
        """Update the styles of the buttons."""
        for btnText, button in self.buttons.items():
            if btnText in {'+', '−', '×', '÷'}:
                button.setObjectName("operationButton")
            elif btnText in {'C', 'CE', '⌫', '%', '1/x', 'x^2', '√x'}:
                button.setObjectName("functionButton")
            elif btnText == '=':
                button.setObjectName("equalsButton")
            # Apply the style immediately
            button.setStyle(button.style())


def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
