#Abdala S. Zaghab O.
#IP addresses
#Final Code Project
#04/28/2023

#This program works with the ipfile.txt that is attached to the repository

def file_name_in(filenamein,mode): #file input function with parameters to know if the code is read or written
    while True:
        try:

            file_opened= open(filenamein,mode) #open the file if it exists
            

            return file_opened #return value to use later

        except:
            print(f"""
ERROR -- There is an issue with file {filenamein}. Please reenter: 
""") #error message display
            filenamein= input("Enter the input file name: ") #reentry option


#-------------------------------------------------------------------

def file_name_out(filenameout,mode): #output file name function
    while True:
        try:
            file_written= open(filenameout,mode) #creates a fiel to write 

            return file_written #retiurn the value of it to be used later

        except:
            print(f"""
ERROR -- There is an issue with file {filenameout}. Please reenter:
""")
            filenameout= input("Enter the output file name: ")

#-------------------------------------------------------------------
def display_menu(): #display menu for the shell. It prints all the information. 
    print("""
Output Report
--------------
""")
    print(f"The total number of records in the file is: {number_files:,.0f}",end="\n\n") #number of lines = ip addresses
    
    print(f"The number of suspect IP addresses is: {suspect_ip:,.0f}", end="\n\n") #number of suspect ip addresses

    print(f"The percentage of suspect IP addreses is: {percentage_error:,.3f}%",end='\n\n') #percentage of corrupter ip addresses in the file

    print("""Suspect IP Addresses
--------------------
""")
    print('\n'.join(items_error)) #lines with files corrupted
    print("""
Thank you for using the program!""")


    


filenamein= input("Enter the input file name: ") #input of file name for input
filenameout=input("Enter the output file name: ") #input of file name for output

file_opened= file_name_in(filenamein,'r') #call the input funciton with the 'r' mode to indicate that it has to be read
file_written= file_name_out(filenameout,'w') #call the output funciton with the 'w' mode to indicate that it has to be written 


list_string=[] #empty list to add amount of lines in the file. 
items_error= [] #empty llst to add suspect ip addresses lines from the file. 

for line in file_opened: #for loop to read the file 

    list_string.append(line) #this saves each line in the list_string list

    if line[0:7] == "168.193" or line[0:7] == "224.174" or line[0:7] == "233.012": #if condition to see if any corrupted ip is in the file. Exactly the two first octets

        items_error.append(line) #adds the exact line with bad ip addrsses to the items_errror list. 
            

number_files = len(list_string) #length of list_string. amount of lines
suspect_ip= len(items_error) #lenght of suspect_ip. amount of lines           
percentage_error= round((suspect_ip / number_files) * 100, 3) #error% of ip adresses in the file. rounded to 3 decimals
        



display_menu() #call funciton

#This writes the same information in the text output file. This is the report. 
file_written.write(f"Output Report\n--------------\n\n")
file_written.write(f"The total number of records in the file is: {number_files:,.0f}\n")
file_written.write(f"The number of suspect IP addresses is: {suspect_ip:,.0f}\n")
file_written.write(f"The percentage of suspect IP addresses is: {percentage_error:,.3f}\n\n")
file_written.write(f"Suspect IP Addresses\n--------------------\n\n")
file_written.write('\n'.join(items_error))
file_written.write("""
Thank you for using the program!""")

file_opened.close()#close the files. 
file_written.close()
