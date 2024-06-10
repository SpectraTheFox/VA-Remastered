# VA-Remastered
My Virtual Assistant Remastered and redone! HEAVY WORK IN PROGRESS. EXPECT BUGS.
***
## How it works
This is an open source virtual assistant. With full support to create your own commands and modules. I have made this all from scratch to be as easy as possible to add commands and get them working. This uses elevenlabs to use a custom voice.
***
# Installation
This is very basic to install. Just use `git clone https://github.com/SpectraTheFox/VA-Remastered` in any terminal in any folder to clone. You will need to create a `.env` file using the `env_template.txt` file and putting your eleven labs key into the respective variable. It should read them automatically when you run the program. Make sure to also use `pip install -r requirements.txt` to install all requirements for the program.
***
## Making Commands
Making your own commands is very straight forward and simple. as long as you know what you want it to do. Follow the format of `src/modules/template.py` for any commands you would like to add. And make sure to place the file in `src/modules/` to allow it to work. The code is designed to automatically search the directory `modules` for all files and run the `check` for every command until it finds what you are using. then it uses `execute` on that specific command. So make sure that your command has both. Along with placing any `import` statements at the top of the code.
***
## Running the Program
To Run the program simply use `python src/main.py` in your terminal with the main folder open using `cd <path to main folder>/VA-REMASTERED`. It will update in the terminal with things like what you said to wake it up, when it is thinking, etc.