from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget

# Plugin metadata
PLUGIN_METADATA = {
    "name": "EXAMPLEPLUGIN",
    "description": "This plugin does nothing, just provided here as to show how to contribute to the global-plugin-list.",
    "version": "v1.0.0",
}

# Global variables for the plugin's state
plugin_tab = None
greeting_message = "Hello from the Hello Plugin!"

def register(main_window):
    # I think you should know what this does
    global plugin_tab
    plugin_tab = QLabel(greeting_message)
    main_window.tab_widget.addTab(plugin_tab, PLUGIN_METADATA["name"])

def enable(main_window):
    # What should happen when the plugin is enabled
    global plugin_tab
    main_window.tab_widget.addTab(plugin_tab, PLUGIN_METADATA["name"])

def disable(main_window):
    # What should happen when the plugin is disabled
    global plugin_tab
    index = main_window.tab_widget.indexOf(plugin_tab)
    if index != -1:
        main_window.tab_widget.removeTab(index)

def configure(main_window):
    # Put your config dialog logic here
    global greeting_message

    # Create a configuration widget
    config_widget = QWidget()
    config_layout = QVBoxLayout(config_widget)

    # Add a text input for the greeting message
    message_input = QLineEdit(greeting_message)
    config_layout.addWidget(QLabel("Greeting Message:"))
    config_layout.addWidget(message_input)

    # Update the greeting message when the user changes it
    def update_message():
        global greeting_message, plugin_tab
        greeting_message = message_input.text()
        if plugin_tab:
            plugin_tab.setText(greeting_message)

    message_input.textChanged.connect(update_message)

    return config_widget

def save_config(main_window):
    # You can save the configuration to a file or database here
    print("Configuration saved for Hello Plugin.")

def get_plugins(main_window, plugins): 
    # Add this function to get the list of plugins
    print(f"Hello Plugin: Loaded {len(plugins)} plugins.")
    for name, module in plugins.items():
        print(f" - {name}: {getattr(module, 'PLUGIN_METADATA', 'No metadata')}")