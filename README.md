# VA-Remastered
My Virtual Assistant Remastered and redone! HEAVY WORK IN PROGRESS. EXPECT BUGS.
***
## How it works
This is an open source virtual assistant. With full support to create your own commands and modules. I have made this all from scratch to be as easy as possible to add commands and get them working. This uses elevenlabs to use a custom voice and openai for questions and such with ChatGPT 3.5. 
***
## Installation
This is very basic to install. Just use `git clone https://github.com/SpectraTheFox/VA-Remastered` in any terminal in any folder to clone. You will need to create `elevenlabskey.txt` and `openaikey.txt` and put your API keys for both services into those files. It should read them automatically when you run the program. Make sure to also use `pip install -r requirements.txt` to install all requirements for the program.
***
## Making Commands
Making your own commands is very straight forward and simple. as long as you know what you want it to do. Follow the format of `src/modules/template.py` for any commands you would like to add. And make sure to place the file in `src/modules/` to allow it to work. The code is designed to automatically search the directory `modules` for all files and run the `check` for every command until it finds what you are using. then it uses `execute` on that specific command. So make sure that your command has both. Along with placing any `import` statements at the top of the code.
***
## Running the Program
To run the program you will run `src/main.py` and it will start waiting for you to wake it up. The wakeup is "prism" but you may change that to whatever within. After that just ask any question or give any command. **Keep an eye on the command line. it will tell you when it is listening**. it automatically responds and resets to wait for the wakeup once it finishes the last command.