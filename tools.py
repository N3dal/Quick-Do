from os import name as OS_NAME
from os import system


def clear():
    """
        wipe terminal screen;

        return None;
    """

    if OS_NAME == "posix":
        # for *nix machines;
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for any other os in this world;
        # system("your-command-here")
        pass

    return None
