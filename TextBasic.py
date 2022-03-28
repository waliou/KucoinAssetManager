class bcolors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    PURPLE = '\033[0;35m'
    LCYAN = '\033[1;36m'
    ENDC = '\033[0m'

def prompt_input(hint):
    return input(bcolors.YELLOW + '*) ' + bcolors.ENDC +hint)