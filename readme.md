# Sandbox Mod Files

### This repository contains all of the actual game files for the Sandbox Mod. **This should almost never be manually downloaded, to install the mod, use the [Sandbox Mod Installer](https://github.com/TheWRDNoob/Sandbox-Mod-Installer "Sandbox Mod Installer").**

## File Organization
+ version.txt: States current mod version
+ install_location.json: Contains paths for game files after `Data/WARGAME/PC`
+ patcher_paths.json: Contains names and paths for XML patches
+ Installer: For installing assets and uninstalling
    + WargameModInstaller.exe: Executable for asset installation and general uninstallation
	+ Modded: Changed files required for mod
	+ Original: Original files to use for uninstallation
+ Patcher: For applying game data changes
    + WGPatcher.exe: Executable that takes .xml script files and NDF_Win.dat file as input and outputs new file with changes applied.
+ Script Library: Contains all .xml script files for patcher.

