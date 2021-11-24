# Selenium Test by Ana Carrión Barbotó

This Python program uses ESPOL Education page as principal and each career page as secondary
![](images/C4.JPG)

Goals:
- Create a driver which simulate that a user get into ESPOL Education web page and read each faculty and their each carrer. 
- Current driver opens each ESPOL carrers web page and validate if it has abet certification.

To achieve these goals I applied the Page Objects design pattern and I got these objects:
1. In principal.py there is a class called ESPOLSearch which contains 3 methods:
- setUp() -> Initialize a webdriver of Chrome and open a page of ESPOL Education.
- test_search_in_espol() -> Create a variable called main_page which is an EspolEducationPage instance which receives 3 elements (a driver, a empty list of careers link, a empty list of careers name) that inherits from the father Base Page object, then, it calls 2 methods create_excel_file() and show_abet_list() which doesn't receive any element.
- tearDown () -> Close an instance of webdriver.
2. In page.py there are 3 objects called BasePage, EspolEducationPage and CareerEducationPage.
- Base Page object has 3 attributes mentioned in test_search_in_espol().
- EspolEducationPage object has 4 methods:
  - get_faculties() -> returns html objects which meets this XPATH '//div[@class="panel-heading"]//h4[@class="panel-title"]//a'
  - get_classes() -> returns html objects which meets this XPATH '//div[@id="'+code+'"]//div[@class="field-content"]//ul//li//a', variable code is id of "a" tag of each faculty
  - create_excel_file() -> uses both mentioned methods to go through both html list and create an excel file called educacion_espol.xlsx that follow this format: career_name_es, faculty_name, link_to_career_curriculum and set BasePage values list_href and careers_name which will use in the next method.
  ![](images/exercise1.JPG)
  - show_abet_list() -> return a list which indicates name of careers that has abet certfication using the information obtained from create_excel_file() method.
  ![](images/exercise2.JPG)
3. In locators.py there are all locators to use of each web page. Inspecting ESPOL Education page and Careers page, I have these XPATHs:
- FACULTY_LIST -> both html elements of faculties has <div class="panel-heading></div> next to <h4 class="panel-title"></h4> and next to <a></a>.
- ABET_HREF -> all careers have an element which contains abet url <a href="http://www.abet.org"></a> except 2 careers
 - OCEANOGRAPHY -> which has <a href="https://amspub.abet.org/aps/category-search?disciplines=57"></a>
 - FOOD -> which has <img src="/sites/fimcp.espol.edu.ec/files/EAC-RGB-W-L.jpg">
4. element.py is empty.

To use:
- open cmd or terminal
- run "python3 principal.py"
