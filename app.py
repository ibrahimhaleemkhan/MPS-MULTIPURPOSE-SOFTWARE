
#multi purpose Software updated v12.2 at 25/12/2015
#WIthout Use of class
#IBRAHIMHALEEMKHAN
#github.com/ibrahimhaleemkhan

#dont copy as it is, do some modification tooo :)
import datetime ,os
def loading():  #for loading 
    sys.stdout.write("\t \t  \n LOADING - PLEASE_WAIT \t")
    for i in range(4):
        sys.stdout.write('|')
        time.sleep(.90)
    sys.stdout.write(" \n \t READY \n\n")
    
# for logging


def log():
    os.system("lock.bat")
    f=open("Groove/log.txt" , "a")
    now = datetime.datetime.now()
    f.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t")
    f.write("\nLast Time opened at \n")
    f.write(str(now))
    f.write("\n \t - - - - - - - \n ")
    f.close()
    os.system("lock.bat")
    


def logoption(a):
    os.system("lock.bat")
    f=open("Groove/log.txt" , "a")
    now = datetime.datetime.now()
    f.write("\nOption -")
    f.write(a)
    f.write("\nChosed  at \n")
    f.write(str(now))
    f.write("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t")
    f.close()
    os.system("lock.bat")

log()
# test if required Module are Installed
print """Checking info.
and if Modules are installed .\n
\nAn error will be given if initializing failed. \n \t """
try:
    import PIL
    print "PIL Installed"
except ImportError:
    print "Error PIL not Installed .. GooglE IT"
    

try:
    import VideoCapture
    print "vidcap Installed"
except ImportError:
    print "Error VIDCap not Installed .. GooglE IT"
 
try:
    from Crypto.Cipher import AES
    print "Cipher cipher Installed"
except ImportError:
    print "Error Cipher cipher  not Installed .. GooglE IT"

 

 
def printmenu():
    #print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "1.  To test your internet connection :\n\t\t\t \t "
    print "2.  To shutdown  , restart  or logoff your computer :\n\t\t\t\t"
    print "3.  To open a website :\n\t\t\t\t"
    print "4.  To click A portrait from your webcam from your device : \n\t\t\t\t"
    print "5.  To start matrix :\n\t\t\t\t"
    print "6.  To send an email :\n\t\t\t\t"
    print "7.  To encrypt a string :\n\t\t\t\t"
    print "8.  To Take a Screencapture(i.e Screenshot) :\n\t\t\t\t "
    print "9.  To Listen winnsound magic :\n\t\t\t\t"
    print "10. To adjust your brightness according to your lighting : \n\t\t\t\t"
    print "11. To Exit : \n\t\t\t\t"



import sys ,time 
print "\t\t\n \t\t Welcome to MPS- Multipurpose Software \
\t\t\n \t\t \t COPY LEFT thinkdiff.co.in \n \n"
loading() 
import os


#log clear


CL=raw_input("Do you wanna clear the log (y/n) \n:")
if CL=="y":
    PD=raw_input("If you wanna clear the log Enter the password \n :  ")
    if PD==("y"):
        os.system("lock.bat")
        f=open("Groove/log.txt", "w")
        f.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        f.write("LOG CLEARED !! AT -")
        now = datetime.datetime.now()
        f.write(str(now))
        f.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        f.close()
        os.system("lock.bat")
        print "LOG CLEARED"
                  
        
    else:
        print "ACCESS-DENIED-AUTHORISATION"
        os.system("lock.bat")
        f=open("log.txt", "w")
        f.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        f.write("UNAUTHORISED ENTRY - Invalid password !! AT -")
        now = datetime.datetime.now()
        f.write(str(now))
        f.write("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        f.close()
        os.system("lock.bat")
        
else:
    print "\n Log maintained\n "
    
    
    


    
#program start 
while True:
     print "\t\t\n \t\t Welcome to MPS- Multipurpose Software \
            \t\t\n \t\t \t COPY LEFT thinkdiff.co.in \n \n"
     #printmenu
     print "Do You Want ??"   
     printmenu()
     print "\n \t "
          
     a=raw_input("\t\nEnter the option of your choice nothing else  : \n")
     logoption(a)
               
     if a=="1":
        import urllib
        try :
            stri = "https://www.google.co.in"
            data = urllib.urlopen(stri)
            print "Internet Connected\n"
        except:
            print "Internet not connected\n" 


        continue
            
       


    
     elif a=="2":
         option2a=raw_input("\n 1. to shutdown \n 2. to reboot  \n 3. logoff \n 4.Exit the situation\n ")
         if option2a=="1":         
             os.system("shutdown /s")
         elif option2a=="2":
             os.system("shutdown /r")
         elif option2a=="3":
             os.system("shutdown /l")
         elif option2a=="4":
             print "Saved!!"
             
         else:
             print "you gave wrong input \n \t"
         continue


            
     elif a=="3":
          os.system("lock.bat")
          website=raw_input("Enter The name of a Website \n :")
          f=open("Groove/log.txt" , "a")
          f.write("Website opened")
          f.write(str(website))
          f.write("at")
          now = datetime.datetime.now()
          f.write(str(now))
          f.close()
          import  webbrowser 
          webbrowser.open_new(website)
          os.system("lock.bat")
          continue



     elif a=="4":
        os.system("lock.bat")
        from VideoCapture import Device
        cam = Device()
        sys.stdout.write("\t \t  \n Be ready you  are gonna be clicked  2 seconds\t")
        for i in range(4):
           sys.stdout.write("\-/ ")
           time.sleep(.5)
        sys.stdout.write(" \n \tSay Victory ... \n")
        time.sleep(2)
        #file handling used
        cam.saveSnapshot('Groove/image.jpg')
        from PIL import Image
        image = Image.open('Groove/image.jpg')
        image.show("12")
        os.system("lock.bat")
      
        
        continue



     elif a=="5":
        
       os.system("matrix.bat")
       continue
        

     elif a=="6":
         print "welcome to anonyy email sending.... \n \t \n"
         import urllib
         

         to = raw_input('To :\n')
         subject = raw_input('Subject :\n')
         fro = raw_input('From :\n')
         text = raw_input('Text :\n')

         stri = "http://register.tangelo-town.com/mailer.php?to="+to+"&from="+fro+"&text="+text+""
          #use Your Own server as this link is not available anymore
         data = urllib.urlopen(stri)
         data = urllib.urlopen(strj)
         print data,stri,strj, "/n mail Sent  | you got it |\n \t \n "
         
         continue


     elif a=="7":
        import sys , os


        k=int(input("Enter the value to increase the power of encryption : \n"))

        def encrypt(k):
            plaintext = raw_input('Enter plain text message: ')
            cipher = ''

            for each in plaintext:
                    c = (ord(each)+k) % 126
                    
                    if c < 32: 
                            c+=31
                            
                    cipher += chr(c)
                    
            
            
            os.system("lock.bat")
            f=open("Groove/encry.txt" , "a")
            f.write(plaintext)
            f.write(" - TO - ")
            f.write(cipher)
            f.write("\n")
            f.close()
            os.system("lock.bat")
            print 'Your encrypted message is: ' + cipher    


        def decrypt(k):
            cipher = raw_input('Enter encrypted message: ')
            plaintext = ''

            for each in cipher:
                    p = (ord(each)-k) % 126

                    if p < 32:
                            p+=95
                                                    
                    plaintext += chr(p)
                    
            
            os.system("lock.bat")
            f=open("Groove/encry.txt" , "a")
            f.write(cipher)
            f.write(" - TO - ")
            f.write(plaintext)
            f.write("\n")
            f.close()
            os.system("lock.bat")
            print 'Your plain text message is: ' + plaintext    

        encrypt(k)
        print "\n"
        decrypt(k)







        #encrypto
         
       
        continue
        
     elif a=="8":
        os.system("lock.bat")
        from PIL import ImageGrab
        import time
        print'Caputuring in 2 seconds'
        time.sleep(2)
        #file handing used
        ImageGrab.grab().save("Groove/screencapture.jpg", "JPEG")
        print "IMage Grabbed"
        from PIL import Image
        image = Image.open('Groove/screencapture.jpg')
        image.show()
        os.system("lock.bat")
        continue

     elif a=="9":
          
        #winsound comp music
        import winsound;
        beatlength = 300;

        winsound.Beep(261, beatlength) # C
        winsound.Beep(262, beatlength) # C
        winsound.Beep(294, beatlength) # D
        winsound.Beep(330, beatlength) # E

        winsound.Beep(262, beatlength) # C
        winsound.Beep(330, beatlength) # E
        winsound.Beep(294, 2*beatlength) # D (double length)

        winsound.Beep(262, beatlength) # C
        winsound.Beep(262, beatlength) # C
        winsound.Beep(294, beatlength) # D
        winsound.Beep(330, beatlength) # E

        winsound.Beep(262, 2*beatlength) # C (double length)
        winsound.Beep(247, 2*beatlength) # B (double length)

        winsound.Beep(262, beatlength) # C
        winsound.Beep(262, beatlength) # C
        winsound.Beep(294, beatlength) # D
        winsound.Beep(330, beatlength) # E

        winsound.Beep(349, beatlength) # F
        winsound.Beep(330, beatlength) # E
        winsound.Beep(294, beatlength) # D
        winsound.Beep(262, beatlength) # C

        winsound.Beep(247, beatlength) # B
        winsound.Beep(196, beatlength) # G
        winsound.Beep(220, beatlength) # A
        winsound.Beep(247, beatlength) # B

        winsound.Beep(262, 3*beatlength) # C (double length)
        winsound.Beep(262, 3*beatlength) # C (double length)

     elif a=="10":
        
        os.system("lock.bat")
        print "Adjusting the brightness"
        from VideoCapture import Device
        cam = Device()
        sys.stdout.write("\t \t  \n Be ready ur are gonna be clicked  2 seconds\t")
        time.sleep(2)
        #file handling used
        cam.saveSnapshot('Groove/image.jpg')
        from PIL import Image
        image = Image.open('Groove/image1.jpg')
        image= image.convert('1') # convert image to black and white
        image.save('image.jpg')
        #calualtion of grey scale area and to adjust the brightness accoding to it
        black, white = image.getcolors()
        print black[0] , "black"
        print white[0],"white"
        z=(white[0]*1.00/black[0]*1.00)*100.00 #cals the black and white pecentage in float
        print "The % of W&B is",z
        #condition for changing the brightnes
        #condition for linux 
       
        os.system("lock.bat")

        
         
     elif a=="11":
         print "THANK YOU ! FOR USING MPS !! "
         logoption("exit at")
         time.sleep(1.98182)
         exit()
         
        


         
     else:
        print "INVALID INPUT >> Enter Correct Choice ... \n \t \n "
        continue




