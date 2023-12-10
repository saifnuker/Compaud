# compaud.py

This module, `compaud.py`, provides functionality to manage computer information and write it to a file.

## Overview

- Computer Object Management: Provides a compaud class to create computer objects with attributes such as hostname, IP address, location, operating system, and version.
- File Writing: Offers a function to write computer information to a specified file, aiding in maintaining a log of computer-related data.


### compaud.py Usage

#### `compaud` Class

The `compaud` class represents a computer and takes the following attributes:

- `name`: Host name of the computer device.
- `ip`: IP address of the device.
- `location`: Location of the device.
- `os`: Operating system of the device.
- `ver`: Version of the operating system.


# computer_audit.py

The `computer_audit.py` script allows auditing and filing of computer information. It utilizes the `compaud` module to manage computer details and write them to a file.

## Overview
- Record Information: Capture crucial details such as host names, IP addresses, locations, operating systems, and versions of computers.
- Logging to a File: Write the collected computer information to a specified file for future reference or auditing purposes.
- User Interaction: Prompt users to input information for audit purposes and interactively record it to the log file.


### computer_audit.pyUsage
Arguments
The script takes the arguments provided in the compaud.py class list.

#### Example Usage:
```bash
python computer_audit.py --name desktop-01 --ip 192.168.1.100 --location 'Reception desk' --os Win10 --ver Version
```
Replace desktop-01, xxx.xxx.xxx.xxx, and other arguments with the appropriate values for your computer.

The script writes the provided computer information to a file named (computer_audit.txt) located in the current working directory.


# search_compinfo.py

This script, `search_compinfo.py`, allows users to search for computer information entries in a specified file based on specific categories such as name, IP address, location, OS, or version.

## Overview

- The script contains a `retrieve_info()` function that reads a file containing computer audit information and searches for entries based on user-provided criteria.
- The primary purpose of search_compinfo.py is to facilitate quick searches and retrieval of specific computer information entries within a log or audit file.


## Usage

### Running the Script

To run the script, execute the following command in your terminal:

```bash
python search_compinfo.py
```
#### Input Prompt
Upon execution, the script will prompt the user to enter the information category (name, ip, location, os, version) they want to search for. After providing the category, the user will be prompted to enter the specific value to search for within that category.

```bash
Enter the information category (name, ip, location, os, version): os
Enter the Os to search for: Windows
```
#### Output
The script will search the specified computer_audit.txt file for entries matching the provided category and value. If a match is found, it will display the information related to that entry.

#### Error Handling
If the specified file (computer_audit.txt) is not found, it will display a "File not found" error message.
If no entry is found for the given category and value, it will display a "No entry found" message.

## Requirements
- Python 3.x
- The compaud module
- computer_audit.txt file to be created and ready to be written into.

## Ref
- [Make a ReadMe](https://www.makeareadme.com/).
- [Python docs](https://docs.python.org/3/library/argparse.html?highlight=create%20module).

## License
- [GNU](https://github.com/saifnuker/Compaud/blob/main/LICENSE).
