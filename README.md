#Selenium Test

These exercises apply the Page Objects design pattern as follows:
- principal.py
This file contains the main and calls the two functions that perform the exercises requested from the page.py file.
- page.py
This file contains the actions of the main page and career page using the necessary locators from the locators.py file.
- locators.py
This file contains all locators using XPATH to grab the html elements that are needed.
- element.py
This file contains set and get functions for the main page.

create_excel_file () function creates a file called educacion_espol.xlsx that contains a list of careers, faculty and link, it also fills a list with the links of each career that belongs to the main object.
<img
src=“images/exercise1.JPG”
raw=true
alt=“Subject Pronouns”
style=“margin-right: 10px;”
/>

show_abet_list () function reads the list created by the create_excel_file () method and changes the main url according to each element in the list to validate if 'abet' exists on each page.
<img
src=“images/exercise2.JPG”
raw=true
alt=“Subject Pronouns”
style=“margin-right: 10px;”
/>