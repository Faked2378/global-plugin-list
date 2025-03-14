import os
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QCheckBox
from PySide6.QtCore import Qt

# Plugin metadata
PLUGIN_METADATA = {
    "name": "BANG!",
    "description": "A plugin to have light mode (who ever uses it, I am concerned for you.)",
    "version": "1.0"
}

# Global variable to track if the plugin is enabled on startup
is_enabled_start = True


def configure(main_window):
    """Provide a configuration UI for the plugin."""
    global is_enabled_start

    # Create a configuration widget
    config_widget = QWidget()
    config_layout = QVBoxLayout(config_widget)

    # Add a checkbox for enabling/disabling the plugin on startup
    enable_checkbox = QCheckBox("Enable on startup?")
    enable_checkbox.setChecked(is_enabled_start)
    config_layout.addWidget(enable_checkbox)

    # Update the config file when the checkbox state changes
    def update_config(state):
        global is_enabled_start
        print(is_enabled_start)
        is_enabled_start = state
        try:
            if int(is_enabled_start) == 2:
                is_enabled_start = True
        except TypeError:
            is_enabled_start = False
        print(is_enabled_start)
        try:
            with open("config/pipe-bomb/conf.txt", "w") as f:
                print(f)
                f.write(str(is_enabled_start))
        except Exception as e:
            print(f"Failed to save config: {e}")

    enable_checkbox.stateChanged.connect(update_config)

    return config_widget

def register(main_window):
    """Register the plugin with the main app."""
    global is_enabled_start
    # Ensure the config directory and file exist
    if not os.path.exists("config/"):
        print("conf base directory not found, creating...")
        os.makedirs("config/")
    if not os.path.exists("config/pipe-bomb/"):
        print("conf directory not found, creating...")
        os.makedirs("config/pipe-bomb/")
    if not os.path.exists("config/pipe-bomb/conf.txt"):
        print("conf file not found, creating...")
        with open("config/pipe-bomb/conf.txt", "w") as f:
            f.write(str(is_enabled_start))  # Default to disabled on startup
    # Load the initial state from the config file
    with open("config/pipe-bomb/conf.txt", "r") as f:
        state = f.read()
        print(f'{state == "True"}')
        is_enabled_start = state == "True"
        print(f"debug: is enabled on start? {is_enabled_start}")
    if not is_enabled_start:
        disable(main_window)
    else:
        enable(main_window)

def enable(main_window):
    """Enable the plugin and apply the light mode theme."""
    apply_css(main_window)

def disable(main_window):
    """Disable the plugin and reset the stylesheet to the default (dark mode)."""
    load_stylesheet(main_window, "styles.css")

def load_stylesheet(window, filename):
    """Load a CSS stylesheet from a file and apply it to the window."""
    try:
        with open(filename, "r") as file:
            window.setStyleSheet(file.read())
    except FileNotFoundError:
        print(f"Stylesheet file not found: {filename}")
        window.setStyleSheet("")  # Reset to default
    except Exception as e:
        print(f"Failed to load stylesheet: {e}")

def apply_css(main_window):
    """Apply the light mode CSS to the main window."""
    main_window.setStyleSheet(css)

# Custom CSS for light mode
css = """
/* Light Mode Styles */
QMainWindow {
    background-color: #ffffff;
    color: #000000;
    font-family: "Segoe UI", sans-serif;
}

QTabWidget::pane {
    border: 1px solid #ccc;
    background-color: #f9f9f9;
}

QTabBar::tab {
    background-color: #e0e0e0;
    color: #000000;
    padding: 10px;
    border: 1px solid #ccc;
    border-bottom: none;
    font-size: 14px;
}

QTabBar::tab:selected {
    background-color: #ffffff;
    font-weight: bold;
}

QPushButton {
    background-color: #0078d7;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
}

QPushButton:hover {
    background-color: #005bb5;
}

QPushButton:disabled {
    background-color: #ccc;
    color: #666;
}

QListWidget {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 8px;
}

QListWidget::item {
    padding: -1px;
    border-bottom: 1px solid #eee;
}

QListWidget::item:hover {
    background-color: #f0f0f0;
}

QDialog {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #ccc;
}

QLabel {
    font-size: 14px;
    color: #000000;
}

QLineEdit {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #ccc;
    padding: 5px;
    border-radius: 4px;
}

QMessageBox {
    background-color: #ffffff;
    color: #000000;
}

QMessageBox QLabel {
    color: #000000;
}

QCheckBox {
    color: #000000;
}

QMessageBox QPushButton {
    background-color: #0078d7;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    font-size: 14px;
}

QMessageBox QPushButton:hover {
    background-color: #005bb5;
}
"""