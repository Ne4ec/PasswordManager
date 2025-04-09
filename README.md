# PasswordManager
![password_manager_proof_of_concept](https://github.com/Ne4ec/Programming/blob/main/.pictures/passsword_manager_poc.png)
A CLI password manager, created with Python. It is for educational purposes only—do not use it as your default password manager!

## Installation
### Linux
1. Before we begin, we need to install Python to execute the program, as well as Git to install the repository
```bash
sudo pacman -Syu python git 
```
**Notice:** If you're using a different Linux distribution (`apt` or `dnf` etc.), make sure to use the correct `package manager`. The steps should be similar across distributions.
2. after that, install my repository
```bash
sudo git clone https://github.com/Ne4ec/PasswordManager
cd PasswordManager
```
3. Now we are finished, its upon on you, what do you want to do. See the usage
### Windows
1. First, you need to install the following tools
- git: [GIT for Windows](https://git-scm.com/downloads/win)
- python: [Python for Windows](https://www.python.org/downloads/windows/)

Make sure to download the version that matches your system architecture — most commonly 64-bit. Run the Git installer to complete the setup. If you run into any issues during installation, refer to these guides
- for git [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- for python [Downloading Python](https://wiki.python.org/moin/BeginnersGuide/Download)

After installation, open the folder where the Git executable was downloaded (typically your `Downloads` folder). In the File Explorer’s address bar, type `cmd.exe` and press Enter. This will open a terminal window in that directory.

2. write here the following commed
```bash
git clone https://github.com/Ne4ec/PasswordManager
cd PasswordManager
```
3. Now you are finished. Go now the the Usage of the password manager.
____
## Useage
A simple password manager that allows you to create a password and assign it a name.
```
SYNOPSIS 
    ./main.py [OPTIONS]

    [OPTIONS]
        -a  all
                show the entire list
        -c  create
                create an new Password
        -h  help
                get more help
```
**Warning**: This project is designed for learning purposes only. It is not intended for professional use and is suitable for school or study projects. <br>
____
## Conculution
Hopefully, everything is working. If not, please leave a comment in the Issues tab. Thank you for paying attention, and have a nice day :)<br>
~ Ne4ec
____