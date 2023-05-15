import subprocess

REQUIRED_PACKAGES = ["tkinter", "filedialog", "messagebox", "threading", "pyautogui"]

def install_dependencies():
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.call(['pip', 'install', package])

if __name__ == "__main__":
    install_dependencies()
