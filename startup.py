import subprocess
import os


#install for snap, and obsidian 

def main():
    """
    Downloads and installs the latest Obsidian Snap package on Linux.
    """
    print("Attempting to install Obsidian Snap package...")

    # Ensure snapd is installed
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "snapd"], check=True)
        print("snapd is installed or updated.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing snapd: {e}")
        return

	#enable snapd
    try:
        subprocess.run(["sudo", "systemctl", "start", "snapd.service"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "snapd.service"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error enabling snapd: {e}")
        return

    # Install Obsidian using snap
    try:
        subprocess.run(["sudo", "snap", "install", "obsidian", "--classic"], check=True)
        print("Obsidian Snap package installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Obsidian Snap: {e}")
        print("You might need to manually install it or check for errors.")

    # Install GitKraken using snap
    try:
        subprocess.run(["sudo", "snap", "install", "gitkraken", "--classic"], check=True)
        print("GitKraken Snap package installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing GitKraken Snap: {e}")
        print("You might need to manually install it or check for errors.")

    # make desktop shortcuts for newly installed snaps
    #verify correct directory location
    subprocess.run(["cd", "/home/kali/Desktop"], check=True)
    print("Navigating to desktop directory")

    #move .desktop files from snapd to desktop
    subprocess.run(["cd", "/var/lib/snapd/desktop/applications"], check=True)
    print("Navigating to snapd desktop apps")
    subprocess.run(["sudo", "mv", "gitkraken_gitkraken.desktop", "/home/kali/Desktop"], check=True)
    subprocess.run(["sudo", "mv", "obsidian_obsidian.desktop", "/home/kali/Desktop"], check =True)

    #end
    print("All done:)")

if __name__ == "__main__":
    main()


