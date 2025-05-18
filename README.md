
## Table of Contents
- [DSG-V1.py](#DSG-V1.py)
	- [Simple-Use-case](#simple-use-case)
- [DSG-GUI-1.2.0v](#DSG-GUI-v1.2.0)
	- [Getting Direct Build Setup](#Getting_Direct_Build_Setup)
	- [Executable Version of the Early Beta](#executable-version-of-the-early-beta)
	- [Getting started with the GUI](#getting-started-with-the-gui)
		- [Template Creation](#template-creation)
		- [Excel Generator](#Excel-Generator)

---

### DSG-V1.py

An automation program to generate Excel sheets with dedicated formulas and colors to make a Excel file that only requires data entries.

The focus of this project was to streamline a specific requirement for excel file generation that could allow more effective methods to enter data and not make inefficient self calculations for each situation.

The layout was planned out and the code has the template to generate embedded within the code itself, I.E. the program is a proof of concept for effective generation of the excel files that can be generated to make the process of data entry within excel sheets significantly faster and all the required calculation regions auto-completed by specific planned out formulas.

Now, a new version, which will be based on GUI to allow construction of the templates, is in progress.

_Note - "Template" here means a "date-wise table", where all dates should have similar dimensions of rows and columns._

---

#### Simple-Use-case

- The application was made to construct a rigorous, non-changing template structure.
- The GUI focuses on giving options to allow construction of flexible templates and templates that can be saved and loaded back up.
- You can still get the code for the DSG-V1.py from my GitHub as a proof of concept.
- The CLI menu will prompt my ASCII sir name and ask for year as an input, there you need to put the year for which you need to generate the sheet for.

---

### DSG-GUI-v1.2.0

This program is a re-factor of prior DSG version which only had the ability to produce an excel sheet for the template of 1 hardcoded table.

The GUI integration allows the user to create their own templates, one can create simple templates which may or may not have Excel formulas within them.

Here, the excel formulas have to be static in nature (I.E. you should expect them to be just copy-pasted throughout the sheets the program will generate.)

This program uses JSON for storing templates, Pandas for Data frames creation and excel sheet generation, and OpenPyXL for basic editing of the generated excel sheet for a little finishing touch.

---

#### Getting-Direct-Build-Setup

1. Firstly, get the files downloaded from the v1.2.0/alphas within development.
2. Here, there will be requirement of GUI_Base that you will see within the v1.2.0 folder, the structure of this file is as follows:

	```
	folder_name/                # Root package directory, here it is named GUI_Base
	├── __init__.py             # Make this a Python package
	├── _CSS_APPLIER_VER1.py    # CssManager implementation
	├── _GUI_COMPONENT_with_themes_ver4.py  # WidgetsTypes & MainWindow
	├── folder_themes/          # Sub-package for themes
	│   ├── __init__.py         # Make this a Python sub-package
	│   └── themes.py           # THEMES definitions
	└── pyproject.toml          # Package metadata for this module
	
	pyproject.toml              # Root-level metadata for workspace
	```

3. Now, from the directory levels of the ```folder_themes``` and ```folder_names```  here, execute the pyproject.toml files to make the folder contents assessable. This finishes the process of GUI class files setup.
4. Now, focusing abstractly over the rest of the structure, this is how it should look like:
	```
	v1.2.0/alphas
	├── GUI_Base
	├── testing_json_saves
	├── excel_extractor.py
	├── Main_GUI_screen_test1.py    # The main GUI file.
	└── testing_excel.xlsx
	```
5. Here, the main file of execution is ```Main_GUI_screen_test1.py```, there should not be  a problem running this file, if there is then you may contact me with the issue you encountered and/or try the compiled .exe version instead.

---
#### Executable-Version-of-the-Early-Beta
1. Simply download the executable from ```Versions``` folder, which will have it inside ```1.2.0v/dist``` path.
2. There is no requirement needed for this one and it should run without issue, if it doesn't then do raise an issue.
3. The .exe creation was possible with the help of ```PyInstaller```.

---

#### Getting-started-with-the-GUI
![HomeScreen](assets/HomeScreen.png)
1. After successfully getting the program on your system, you can open it and will be prompted with the Home Screen.
	1. The Home screen consists of (options):
		1. [Template Creation](#template-creation)
		2. [Excel Generator](#Excel-Generator)
		3. Quit (Exits the application)

---
##### Template-Creation
![TemplateScreen](assets/TemplateScreen.png)
1. Consists of Operations such as:
	1. Save & Load templates. (Uses JSON file format to store data points.)
	2. Simple Add feature Rows and Columns within the Template.
	3. Simple Remove feature Rows and Columns within the Template.

---

##### Excel-Generator
![GenerationScreen](assets/GenerationScreen.png)
1. Consists of:
	1. 3 Input fields: 
		1. The ```.json``` file location and name field. (To retrieve that JSON table template.)
		2. The year for which you need the sheet to generate for.
		3. Excel file name you want that sheet to have.
	2. The generate button which generates the sheet, if the inputs are valid.

---
