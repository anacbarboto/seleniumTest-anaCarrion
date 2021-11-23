Selenium Test by Ana Carrión Barbotó

These exercises apply the Page Objects design pattern as follows:
- principal.py
This file contains the main and calls two functions from page.py file that perform exercises requested.
- page.py
This file contains actions of the main page and career page using necessary locators from locators.py file.
- locators.py
This file contains all locators using XPATH to grab the html elements that are needed.
- element.py
This file contains set and get functions of main page.

create_excel_file () function creates a file called educacion_espol.xlsx that contains a list of careers, faculty and link, it also fills a list with the links of each career that belongs to the main object.
Result in image/exercise1.JPG

show_abet_list () function reads the list created by the create_excel_file () method and changes the main url according to each element in the list to validate if 'abet' exists on each page.
Result in image/exercise2.JPG


To use:
- open cmd or terminal
- run "python3 principal.py"