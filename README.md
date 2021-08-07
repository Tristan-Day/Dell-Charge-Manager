# Dell Charge Manager GUI
A GUI wrapper for setting battery charge limits on compatible Dell laptops. Written in Qt &amp; Python

![image](https://user-images.githubusercontent.com/41393868/128606079-e94bd354-9594-4d0f-85e3-0e355a0e5c85.png)

## Installation
Note:
The program relies on `kdesu` in order to bypass issues when launching the application as root. As a result users will need to configure their own GUI elevator by changing the `sudo_elevator` variable in `config.ini` to the appropriate command. Users with other desktop environments and systems may need to make some tweaks to the scripting in order to get it working.

### Arch Based Systems
1. Install [dell-command-configure](https://aur.archlinux.org/packages/dell-command-configure/) from the AUR
2. Use pip to install `pyq5`
3. Clone the repository https://github.com/TROFER/dell-charge-manager-gui.git
4. Configure sudo gui elevator command in `config.ini`
5. Run dell-charge-manager.py file (Do not run as root, you will be prompted to grant it permissions when it launches)
6. (Optional) Create a `.desktop` file in `$./local/share/applications` to add it to the system applications menu

## Feedback and Contributions
If you have any suggestions or improvements that could be made to the program, please let me know by creating an issue.
https://github.com/TROFER/dell-charge-manager-gui/issues/new/choose
