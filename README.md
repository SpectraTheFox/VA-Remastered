# SpectraTheFox's VA-Remastered
My Virtual Assistant Remastered and redone! HEAVY WORK IN PROGRESS. EXPECT BUGS.
***
## How it works
This is an open source virtual assistant with full support to create your own commands and modules. Designed from scratch to be as easy as possible to add and get commands working. It uses ElevenLabs for custom voice support.
***
## Installation
To install VM-Remastered, follow these steps:
1. Clone the repository: `git clone https://github.com/SpectraTheFox/VM-Bemastered`
2. Navigate to the project directory: `cd VM-Remastered`
3. Create a .env file using the `env_template.txt` file and add your ElevenLabs API key to the respective variable.
4. Install the required dependencies: `pip install -r requirements.txt`
***
## Making Commands
Creating your own commands is straightforward. Follow the format of `src/modules/template.py` for any commands you wish to add. Place the file in `src/modules/` to ensure it works. The code automatically searches the modules directory for all files and runs the check for every command until it finds the one you are using. Then it uses execute on that specific command. Ensure your command includes both check and execute functions and place any import statements at the top of the code.
***
## Running the Program
To run the program, use the following command in your terminal: 
`python src/main.py`
Make sure the terminal is open in the main folder using cd <path to main folder>/VM-Bemastered. The terminal will update with information such as wake-up commands, thinking status, etc.
***
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
***
## Support
For support, please open an issue on the GitHub repository or contact the maintainers directly.
