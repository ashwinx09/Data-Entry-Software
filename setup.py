from cx_Freeze import setup, Executable

# Define the script and executable details
executables = [
    Executable("main.py", base="Win32GUI")  # Specify the entry point script and base as Win32GUI
]

# Define the setup options
setup(
    name="GUI",  # Name of the application
    version="1.0",  # Version of the application
    description="data entry GUI",  # Description of the application
    executables=executables  # List of executables to create
)

"""Process to run the application"""

# run this command in terminal <python setup.py build> and it will make a executable file.
# Run the software in your machine by the following ways:
# Go inside  C:\build\exe.win-amd64-3.12 
# there you will find the main application 
# run it 


