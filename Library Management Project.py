 #here you should import for defalut data time if he don't imput it .

class Libray :
  booklist =[] # nasser , ahmed , sala
  BookArray= [] #Empty Array For  More Than one Book
  Number_Of_Books = 0
  Number_of_action=0
  name=[]
  issued = []
  lendBook = []
  def __init__(self ,booklist, book_code=0 , auther="UnKnow" ,price =0 ,Quantity=0, rack_no=0 ,subject_code=0 ):
      self.booklist= booklist # nasser , ahmen d , tareq
      self.book_code = book_code
      self.price = price
      self.Quantity=Quantity
      self.rack_no= rack_no
      self.subject_code = subject_code
      self.auther = auther
      # for issued book .

  def displaybook(self): # Correct Method.
      print("The Books We Have in our library are :")
      #print(self.booklist)
      #for book in self.booklist:
      if len(self.booklist) ==0 : # This If Statement For Check If the list is empty or no .
       print("Oppps , Soory We Don't Have Books Rright Now , Try To Add Book By Press 1 .")
      for book in self.booklist:
        print(book)

  def bookData(self , book):
      #for book in self.booklist:
       print(
             " book name " ,self.booklist ,
            "\nbook code"+ self.book_code +
             "\nbook Author "+ self.auther+
            "\nsubject code "+self.subject_code+
            "\n book Price "+self.price+
            "\n book Quantity "+self.Quantity+
            "\n Book Rack_No  "+self.rack_no )

  def issued(self,book):
      if book  in self.booklist: # Flag ,
          self.lendBook.append(book)
          print(f"You Have been issued {book}. Please Keep it Safe and return it within 30 Days from date {da}")
          self.booklist.remove(book)
          # y=list(self.booklist)
          # y.remove(book)
          return True
      else :
          print("Sorry , This book is either not available or has already been issued somone else .\nPlesase wait until the book is avaible")
          # print(f"Book is alleady is use by {self.lendBook[book]}")

  def addBook(self,book):
      self.booklist.append(book)
      print("The Book have been added to you'r libray")

  def UpdateBook(self,book):
     if book not in self.booklist:
         print("Sorry The Book Not in the book list :( , Try to enther a nother book")
     elif book in self.booklist:
         bname = input("Enter book name: ")
         bcode = input("Enter book code:")
         author = input("Enter book Author:")
         subject = input("Enter subject code:")
         price = input("Enter book Price:")
         quantity = input("Enter book Quantity:")
         rack_No = input("Enter Book Rack_No:")
         Libray.booklist.remove(book)
         Libray.booklist.append(bname)
         self.booklist=Libray.booklist
         self.book_code=bcode

         # Libray.BookArray[index].self.booklist = bname
         # Libray.BookArray[index].self.book_code = bcode
         self.price = price
         self.Quantity = quantity
         self.rack_no = rack_No
         self.subject_code = subject
         self.auther = author
         print("Done ! . The Book Was")

  def ReturnBook(self,book): # java
      if book in self.booklist:
          print("The Book is already in the Libray")
      else:
          print("Thanks For returning this book! Hoppe you enjoid reading it . have a gread day ")
          self.booklist.append(book)
          self.lendBook.remove(book)

  def saerching(self,book):
      if book in self.booklist:
          print("The Book is  in the Libray , You Can Borrow HIM Now")
      elif book in self.lendBook:
         print("The Book Someone Issued Him Sorry you can't Borrow him right him try after 30 days ")
      else:
          print("Sorry The Book Not Avaiable yet , Try to Connect With admin for add him ")

  def showissued(self):
      print("The Book You Have Issued")
      print(self.lendBook)

  def deleteBook(self,book):
      if book in self.booklist:
          if len(self.booklist)==1:
              check = input("Warning After deleting this book, the library will be empty of books\ndo you want to continue\nEnter Yes For Contiune Or Press No For Stop.")
              check.lower()
              if check == "yes":
               self.booklist.remove(book)
               print("The Book Removed")
              else:
                  print("Thank you for your understanding")
      else:
          print("Sorry Try to enter book avaiable in our library")

  def SaveDate(self):
      print("Welcome To Save Data Page :)\nFor Save Data")
      data =["Book Name : " + str(self.booklist) + "\nYou'r Book Code : " + str(self.book_code) + "\nAuthor Book :" + str(self.auther)+
             "\nYou'r Issued Books :" + str(self.lendBook) + "\nNumber Of Books Was in Libray : " + str(Libray.Number_Of_Books)+"\nNumber Of Action Method's In Our Libray:" +str(Libray.Number_of_action)
            ]
      Filedata = open("H:\Codes\Python\File\Libray", "w")
      Filedata.writelines(data)

class User:
     def __init__(self, name, id, unvsitsry):
         self.name = name
         self.id = id
         self.unvsitsry = unvsitsry
     def displayUser(self):
         print("The Users We Have in our library are :")
         if len(self.name) == 0:  # This If Statement For Check If the list is empty or no .
             print("Oppps , Soory We Don't Have Users Rright Now , Try To Add User By Press 1 .")
         for names in self.name:
             print(names)
     def UpdateUser(self, users):
         if users in self.name:
             self.name.remove(users)
             aa = input("Enter new name ")
             self.name.append(aa)
             print("Done ! . The User Name Was Updated")
         else:
             print("Sorry The User Not in the libray:( , Try to enther a nother User")
     def deleteUsers(self, names):
         if names in self.name:
             if len(self.name) == 1:
                 check = input(
                     "Warning After deleting this name, the library will be empty of Users\ndo you want to continue\nEnter Yes For Contiune Or Press No For Stop.")
                 check.lower()
                 if check == "yes":
                     self.name.remove(names)
                     print("The User Removed")
                 else:
                     print("Thank you for your understanding")
         else:
             print("Sorry Try to enter User avaiable in our library")

     def SaveDate(self):
         usa = ["You'r Name : " + str(Libray.name) + "\nBook Name : " + str(Libray.booklist)   + "Issued Book " + str(Libray.lendBook)]
         Filedata2 = open(r"H:\Codes\Python\File\Users", "w")
         Filedata2.writelines(usa)
     def get_name(self):
         return self.name
     def get_unv(self):
         return self.unvsitsry
     def get_id(self):
         return self.id
class Admin:
     def __init__(self,name , id , address , password):
         self.name = name
         self.id = id
         self.password = password

     def get_name(self):
        return self.name
     def get_password(self):
         return self.password
     def get_id(self):
         return self.id




    #Should Be edit .
# p = int(input("Enter Number Of Account User You want Add On Our Bank "))
# while  p!=0:
print("Welcome In Our Libray Pleses Riegister as a Student and Admin\n First Think You Should Make STUDENT account")
us=0
while us!=6:
    print("Pree 1 For Add Account User\nPress 2 For Delete Account User\nPress 3 For Update Account User\nPress 4 For Display Users \nPress 5 For Enter a libray Book Managements System\nPress 6 For Stop Program\nPress 7 for Save Date")
    us = int(input())
    if us ==1:
        nm= input("Enter You'r Name : ")
        ie = input("Enter You'r Id : ")
        ue = input("Enter You'r Unvisty : ")
        Libray.name.append(nm)
        global userObject
        userObject = User(Libray.name,ie,ue)
    elif us==2:
        userObject.displayUser()
        deleteUser = input("Enter User For Deleting")
        userObject.deleteUsers(deleteUser)
    elif us==3:
        print("Welcome in page for Update Date you'r Users")
        userObject.displayUser()
        update = input("Enter Name You Want Update His Data :")
        if update in Libray.name:
            userObject.UpdateUser(update)
            print("You'r User's After Update ")
            userObject.displayUser()
        else:
            print("Try to Enter a avaiable name")
    elif us==4:
        userObject.displayUser()
    elif us==5:
        print("For Student Page press 1\n For Admin Page Enter 2")
        n = int(input(''))
        if n == 1:
            print(
                "Welcome to User Fromat\nPree 1 For Search Book \nPress 2 For  Issued Books  \nPress 3 For View Issued Book\nPress 4 Up Data to  File \nPress 5 to Strop Program\nPress 6 For Go to Main windo\nPress 7 For Enter Data to file")
            p = int(input())
            if p == 1:
                Libray.Number_of_action+=1
                global bookObject
                bookObject.displaybook()
                se = input("Enter Book For Searching ")
                bookObject.saerching(se)

            elif p == 2:
                Libray.Number_of_action+=1
                global da
                da = input("Enter Date  You Take Book")
                bookObject.displaybook()
                iss = input("Enter Book You want Issued")
                bookObject.issued(iss)
            elif p==3:
                Libray.Number_of_action+=1
                bookObject.showissued()

            elif p==4:
                print("Thanks For Come  to our Libray \n This is List Of aviable books")
            elif p==5:
                exit()
            elif p==6:
                pass
            elif p==7:
                bookObject.SaveDate()

        elif n==2 :
            print("Welcome to the management page for admins")
            print("Press 1 For Add Book \nPress 2 For Issue Books Book\nPress 3 For Update Book\nPress 4 for Return Books\nPress 5 For Delete Book\n"
                  "Press 6 For Searching Book\nPress 7 For Show issued books\nPree 8 For Display All Data For Book\nPress 9 For Display Book\nPress 10 For exit Program\nPress 11 For Go to Main windo\nPress 12 For Enter Data to file ")
            p2 = int(input(''))
            if p2==1 :
                # number = int(input("Enter Number Of Books You Want Add in you'r Libray"))
                bname = str(input("Enter book name: "))
                bcode = input("Enter book code:")
                author = input("Enter book Author:")
                subject = input("Enter subject code:")
                price = input("Enter book Price:")
                quantity = input("Enter book Quantity:")
                rack_No = input("Enter Book Rack_No:")
                #Libray.booklist.append(bname)
                Libray.booklist.append(bname)
                Libray.Number_Of_Books+=1
                bookObject = Libray(Libray.booklist,bcode, author, price , quantity ,rack_No ,subject)
                #Libray.BookArray.append(bookObject)


            elif p2==2 :
                bookObject.displaybook()
                iss=input("Enter Book You want Issued")
                da = input("Enter Date  You Take Book")
                bookObject.issued(iss)
                Libray.Number_of_action+=1

            elif p2==3:
                Libray.Number_of_action+=1

                print("Welcome in page for Update Date you'r Book")
                bookObject.displaybook()
                update = input("Enter Name You Want Update His Data :")
                if update in Libray.booklist:
                #     global index
                #     index = self.booklist.index(update)
                #     Libray.BookArray[index].UpdateBook(update)
                   bookObject.UpdateBook(update)
                   print("You'r Book After Update ")
                   bookObject.bookData(update)
                else:
                 print("Try to Enter a avaiable name")

            elif p2==4:
                Libray.Number_of_action+=1
                print("The Book you have Lend From Libray ")
                print(bookObject.lendBook)
                re=input("Enter Book You WANT RETURN")
                bookObject.ReturnBook(re)
            elif p2==5:
                Libray.Number_of_action+=1

                bookObject.displaybook()
                delete = input("Enter Book For Deleting")
                bookObject.deleteBook(delete)
            elif p2==6:

                Libray.Number_of_action+=1
                bookObject.displaybook()
                sea=input("Enter Book For Searching ")
                bookObject.saerching(sea)

            elif p2==7:

                Libray.Number_of_action+=1
                bookObject.showissued()

            elif p2==8:

                Libray.Number_of_action+=1
                bookObject.displaybook()
                d = input("Enter book that you want print his data")
                bookObject.bookData(d)

            elif p2==9:
                Libray.Number_of_action+=1
                bookObject.displaybook()

            elif p2==10:
                 pass
            elif p2==11:
                pass
            elif p2==12:
                bookObject.SaveDate()
            else:
                print("Incorrect Input , Try To Enter it again.")
        elif n==3 :
            pass
        else:
            print("In Correct Input try to enter another thing plesase")

    elif us==7:
        userObject.SaveDate()











  #
  #
  # while True:
  #       print("Welcome to My Libray System \n For Student Page press 1 \n For Admin Page Enter 2 \n Press 3 For exit Program")
  #       n = int(input(''))
  #       if n == 1:
  #           print(
  #               "Welcome to User Fromat\nPree 1 For Search Book \nPress 2 For  Issued Books  \nPress 3 For View Issued Book\nPress 4 Up Data to  File \n Press 5 to Strop Program\nPress 6 For Go to Main windo\nPress 7 For Enter Data to file")
  #           p = int(input())
  #
  #           if p == 1:
  #               Libray.Number_of_action+=1
  #               global bookObject
  #               bookObject.displaybook()
  #               se = input("Enter Book For Searching ")
  #               bookObject.saerching(se)
  #
  #           elif p == 2:
  #               Libray.Number_of_action+=1
  #               global da
  #               da = input("Enter Date  You Take Book")
  #               bookObject.displaybook()
  #               iss = input("Enter Book You want Issued")
  #               bookObject.issued(iss)
  #           elif p==3:
  #               Libray.Number_of_action+=1
  #
  #               bookObject.showissued()
  #           elif p==4:
  #               print("Thanks For Come  to our Libray \n This is List Of aviable books")
  #           elif p==5:
  #               exit()
  #           elif p==6:
  #               pass
  #           elif p==7:
  #               bookObject.SaveDate()
  #
  #       elif n==2 :
  #           print("Welcome to the management page for admins")
  #           print("Press 1 For Add Book \nPress 2 For Issue Books Book\nPress 3 For Update Book\nPress 4 for Return Books\nPress 5 For Delete Book\n"
  #                 "Press 6 For Searching Book\nPress 7 For Show issued books\nPree 8 For Display All Data For Book\nPress 9 For Display Book\nPress 10 For exit Program\nPress 11 For Go to Main windo\nPress 12 For Enter Data to file ")
  #           p2 = int(input(''))
  #           if p2==1 :
  #               # number = int(input("Enter Number Of Books You Want Add in you'r Libray"))
  #               bname = str(input("Enter book name: "))
  #               bcode = input("Enter book code:")
  #               author = input("Enter book Author:")
  #               subject = input("Enter subject code:")
  #               price = input("Enter book Price:")
  #               quantity = input("Enter book Quantity:")
  #               rack_No = input("Enter Book Rack_No:")
  #               #Libray.booklist.append(bname)
  #               Libray.booklist.append(bname)
  #               Libray.Number_Of_Books+=1
  #               bookObject = Libray(Libray.booklist,bcode, author, price , quantity ,rack_No ,subject)
  #               #Libray.BookArray.append(bookObject)
  #
  #
  #           elif p2==2 :
  #               bookObject.displaybook()
  #               iss=input("Enter Book You want Issued")
  #               da = input("Enter Date  You Take Book")
  #               bookObject.issued(iss)
  #               Libray.Number_of_action+=1
  #
  #           elif p2==3:
  #               Libray.Number_of_action+=1
  #
  #               print("Welcome in page for Update Date you'r Book")
  #               bookObject.displaybook()
  #               update = input("Enter Name You Want Update His Data :")
  #               if update in Libray.booklist:
  #               #     global index
  #               #     index = self.booklist.index(update)
  #               #     Libray.BookArray[index].UpdateBook(update)
  #                  bookObject.UpdateBook(update)
  #                  print("You'r Book After Update ")
  #                  bookObject.bookData(update)
  #               else:
  #                print("Try to Enter a avaiable name")
  #
  #           elif p2==4:
  #               Libray.Number_of_action+=1
  #               print("The Book you have Lend From Libray ")
  #               print(bookObject.lendBook)
  #               re=input("Enter Book You WANT RETURN")
  #               bookObject.ReturnBook(re)
  #           elif p2==5:
  #               Libray.Number_of_action+=1
  #
  #               bookObject.displaybook()
  #               delete = input("Enter Book For Deleting")
  #               bookObject.deleteBook(delete)
  #           elif p2==6:
  #               Libray.Number_of_action+=1
  #
  #               bookObject.displaybook()
  #               sea=input("Enter Book For Searching ")
  #               bookObject.saerching(sea)
  #           elif p2==7:
  #               Libray.Number_of_action+=1
  #
  #               bookObject.showissued()
  #           elif p2==8:
  #               Libray.Number_of_action+=1
  #
  #               bookObject.displaybook()
  #               d = input("Enter book that you want print his data")
  #               bookObject.bookData(d)
  #
  #           elif p2==9:
  #               Libray.Number_of_action+=1
  #
  #               bookObject.displaybook()
  #           elif p2==10:
  #                pass
  #           elif p2==11:
  #               pass
  #           elif p2==12:
  #               bookObject.SaveDate()
  #           else:
  #               print("Incorrect Input , Try To Enter it again.")
  #       elif n==3 :
  #           pass
  #       else:
  #           print("In Correct Input try to enter another thing plesase")              