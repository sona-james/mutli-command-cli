#  Multi-command CLI

This project focuses on design and implementation of multi-command command line interfaces.

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 💡Project Overview

In this assignment, I implemented 3 subcommands for the multi command CLI. The theme of my commands is calculators. All three of the subcommands I have implemented are calculators, which include: basic arithmetic calculator, final grade calculator, and age calculator.

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🛠️ Installation Guide

Below listed are the certain tools that you need installed before running the project.

-   [VS CODE](https://code.visualstudio.com/download) (Code Editor)

-   [GIT](https://git-scm.com/downloads) (Version Control System)

-   [GH CLI](https://cli.github.com/) (GitHub on the Command Line)

-   [Quarto](https://quarto.org/docs/get-started/) (Scientific and Publishing System)

-   [pyenv and Python](https://github.com/pyenv-win/pyenv-win#installation) (Python Version Management Tool)

-   [Poetry](https://python-poetry.org/docs/#installing-with-pipx) (Dependency Management and Packaging in Python)

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🛠️ How to Build/Run the Project

**Cloning the Repository**

The following steps are done from the command line to clone the repository:

1.  Clone the repository using GH CLI:

    ``` bash
    gh repo clone sona-james/mutli-command-cli
    ```

2.  Navigate into the cloned repository:

    ``` bash
    cd sona-james/mutli-command-cli
    ```

**Testing**

To verify that the tools are working properly, follow these instructions to render the report qmd file.

1.  Navigate to the location where you cloned the repository, then install the dependicies.

    ``` bash
    poetry install
    ```

2.  Navigate to the location where you cloned the repository, then activate the virtual environment.

    ``` bash
    poetry shell
    ```

3. To get the list of the commands, run:

    ``` bash
    mytools
    ```

4. To run each of the commands (replace #nameofthecommand with the actual name):

    ``` bash
    mytools #nameofthecommand
    ```

***Optional***: Open the report file in VS Code:

1. Change the directory to the `./report` folder:

    ``` bash
    cd report
    ```

2. Open the file:

    ``` bash
    code ./report.qmd
    ```

3.  Render the report file to HTML:

    ``` bash
    quarto render ./report.qmd
    ```

The rendered HTML file will be saved in the `report` directory itself. You can open them from the command line using their filenames with the ***.html*** extension as shown below.

6.  Make sure you are still in the `./report` folder, then run the following command to open the ***.html*** version of the report file.

    ``` bash
    ./report.html
    ```

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🗃️ Files and Folders

-   *./reports* - contains the homework assignment scaffold and demo.

    -   *report.qmd* - the QMD file is the main assignment file that needs to be edited accordingly.

    -   *report.html* - this file is the rendered HTML version of the report QMD file.

    -   *cli_quickmath.py* - this python file contains a simple basic arithmetic calculator program.

    -   *cli_grader.py* - this python file contains a simple final grade calculator program.

    -   *cli_lifeline.py* - this python file contains an age calculator program.

-   *cli_demo.py* - this file contains a simple program that greets NAME for a total of COUNT times.

-   *./assets* - contains the images used in this assignment

![](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 🙆‍♀️ Author

[\@sona-james](https://github.com/sona-james)
