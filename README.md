# Password brute-force using selenium

This demo application is for learning purposes and only works with demo application. 

Original code from [EkaanshArora/Bruteforce-Selenium](https://github.com/EkaanshArora/Bruteforce-Selenium).

# Requirements
 - Git
 - Python 3.*
 - pip3
 - msedgedriver.exe (Download [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/), Instructions [here](https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=c-sharp) ) must be placed in the cloned git folder
 - A text editor

Recommendation: [Visual Studio Code](https://code.visualstudio.com/) See [
Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) 

# Usage
 - Open git bash in desired directory
 - Clone the repository
```
git clone https://github.com/alptbz/seleniumbruteforce.git
```
 - Change into directory
```
cd seleniumbruteforce
``` 
 - Install requirements.txt using pip3
```
pip install -r requirements.txt
```
 - Open words.txt with a text editor of your choice. (Or add the folder to Visual Studio Code) 
 - Add the desired words to the list from which passwords should be generated.
 - Run password_generator.py without any arguments.
```
python password_generator.py
``` 
 - Check if *dictonary.txt* has been created and filled if variants.
 - Run bruteforce.py with the URL and usernames
```
python bruteforce.py http://example.com --username admin
``` 


 

 