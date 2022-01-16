print("-----------------------phone book------------------------")
print("0.close the phone book ")
print("1.add phone number")
print("2.search phone number")
print("3.view all contact list\n")
d1={}
while True:

     n=int(input("enter Number[0/1/2]:-"))
     print("------------------------------------------------------------------------------------")
     if n==1:
         name=input("enter person name:-")
         phno=int(input("enter phone number:-"))
         d1[name]=phno
         print("phone number is successfully added")
     elif n==2:
         test = input("enter character to search for phone number for the person:")
         name2 = [i for i in d1 if i[0].lower() == test.lower()]
         print("The contact names with this substring are " + str(name2))
         name1 = input("name of the person you want to search from above: ")
         print("||    The contact number of ", name1, " is :-- ", d1[name1],"  ||")

     elif n==0:
         break
     elif n==3:
         print("The numbers in this contact book is: ")
         contact_1 = sorted(d1)
         sorted_contact = {number: d1[number] for number in contact_1}
         print(sorted_contact)
