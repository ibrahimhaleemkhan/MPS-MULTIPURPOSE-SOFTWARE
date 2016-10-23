As stated above “MPS” i.e. Multipurpose Software. Which is basically a Software that can perform different tasks like:
•	To test your internet connection 
•	To shutdown  , restart  or logoff your computer 
•	To open a website 
•	To Click A portrait from your webcam on your device
•	To start matrix 
•	To send an email 
•	To encrypt a string 
•	To Take a Screen capture(i.e. Screenshot) 
HOW DOES IT ALL WORK?
Testing the internet connection:
While testing the internet connection the program imports  urllib from the python library .It uses try and except function.It first to open a website then returns value “Internet Connected” & if its unsuccessful it goes to except: and return value ”Internet Not Connected”.
To shutdown, restart or logoff your computer:
The programs basically run the windows cmd commands from the Python by importing os.system(“”) and using it as a function to call these commands.
To open a website:
A function is called from module webbrowser to open user specific site by taking his input.
To clicka portrait from your webcam on your device:
First it initializes the camera and the modules needed as it imports the specific information needed for capturing with the camera and display the image saved by open using “subprocess”.
To start matrix:
It runs .bat (batch file) using os.system from module os
To send an email:
It takes all the input from the user likes from: to: text &subject: stores it. And it sends all the information in a form of link to my server which is holding a .php file which then further inspects the data given and acts according to it.
To encrypt a string:
It uses AES Encryption type from the modules crypto.cipher which creates the string in to an encrypted one.

To Take a Screen Capture(i.e. Screenshot):
It grabs screen shot using a specified library which is imported from PIL imagegrab And again using pil library it open the image that have been captured using PIL library.
AND MORE

