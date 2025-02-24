import subprocess


def prompt_install(package: str, warn: bool = False):  # pragma: no cover
    """
    Function used to prompt user to install a package.
    """
    cmd = f"pip install {package}"
    try:
        if warn and input(f"Install {package}? Y/n: ") != "Y":
            raise ModuleNotFoundError(f"No module named {package}")
        subprocess.check_call(cmd, shell=True)
        print(f"{package} installed successfully!")
    except subprocess.CalledProcessError:
        print(f"Ran into error installing {package}.")
