 #My new title
 ##This is a second title
###And of course the third one
# Selenium WedDriver wit hPython
## Selenium setup:
1. download selenium
   ```python
   pip instal selenium
   pip freeze (to check version)
    ```
3. download ChromeDriver
- check the version of chrome browse
- download the chromedriver, unzip it and move it in the Python39 directory
3. save in the Python main location: 'C:\Program Files\Python39'
4. import selenium, run sample code
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.thelevelupsolutions.com/')
driver.maximize_window()

driver.quit()
```
## Web Services/API
Data providers: customers, stock prices, analytical, news 
Service providers: google map, google authenticator, keycloak
## Company A:API (web services)
1. Integrated with company system to provide necessary data for the system to operate
2. Bank of america uses location search, they use Google Maps web services
3. Many websites use Google, facebook, instagram authentication web services
4. Many banks use Zelle money transfer web services (API)
5. Selenium API, when in use it is using local copy of the code, this is API but not web services

 - don's have UI yet, then use Postman
 - scope of testing is API only (not focusing  on UI,) execute many combinations very fast, performance testing
## What is HTML?
 ```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```
##Elements explained:
```html

- The <!DOCTYPE html> declaration defines that this document is an HTML5 document
- The <html> element is the root element of an HTML page
- The <head> element contains meta information about the HTML page
- The <title> element specifies a title for the HTML page (which is shown in the browser's title bar or in the page's tab)
- The <body> element defines the document's body, and is a container for all the visible contents, such as headings, paragraphs, images, hyperlinks, tables, lists, etc.
- The <h1> element defines a large heading
- The <p> element defines a paragraph
```
- Document Object Model - html document (DOM)
- tags: head, body, div, button, span, a(links), input (text, password, submit, checkbox, radio button, file (upload a file))
### Color - coding of the tools options to inspect web elements 
1. Tags are **purple** 
2. Attributes are **red** 
3. Values of the attributes are **blue** 
4. Text in the elements, that are in the tags, will be **black** 




