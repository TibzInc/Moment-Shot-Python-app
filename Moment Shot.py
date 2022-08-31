import datetime
import webbrowser

class Journal:
    def save(self):
        response = str(input("How is your current moment?\n"))#get user text

        time = datetime.datetime.now()
        theDate = str(time.day) + "/" + time.strftime("%B") + "/" + str(time.year) #generate formatted current date
    
        f = open("shotfile.txt","a")
        f.write('<p class="pDate">' + theDate + '</p>' + '<p class="pContent">' + response + '</p>')
        f.close()
        print("Saved")

        print("\n\n")
        self.menu() #show menu
        
    def menu(self):
        print("[1] Read your journal")
        print("[2] Write Journal")

        menuresponse = 	int(input("Choose action: "))

        if menuresponse == 1:
            self.read()
        elif menuresponse == 2:
            self.save()
        else:
            self.menu()

    def read(self):
        htmlHeader = """
        <head>
            <style type="text/css">
                .pDate{
                color: #29c1d6;
                font-weight: bold;
                font-size: 18px;

                }
                .pContent{
                background-color: #9999FF;
                padding: 15px 0 15px 5px;
                border-radius: 10px;
                box-shadow: 5px 5px 5px grey;


                }
            

            </style>
        </head>


        """
        f = open("shotfile.txt","r")
        readContent = f.read() #fetch the date and content by line

        if readContent == "":
            print("Journal is empty..")
        else:
            print(readContent)

        #save into html format
        g = open("journ.html","w")

        htmlBody = htmlHeader + readContent
        
        if readContent == "":
            g.write("<p>Journal is empty</p>")
        else:
            g.write("<html>" + htmlBody + "</html>")
        g.close()

        #run html GUI
        webbrowser.open_new_tab("journ.html")

        print("\n\n")
        self.menu() #show menu
        

#main

journal = Journal()
journal.menu()






