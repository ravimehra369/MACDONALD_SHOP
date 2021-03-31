import re
import time
import mysql.connector
obj1 = mysql.connector.connect(host="localhost", user="root", password="", port="3306", database="mcdonald")
cursor = obj1.cursor()

class Mcdonald:

     # 1. Menu fucntion is use to show the items in the list
    def Menu(self):
      food_items = ["chicken = $9", "burger  = $6", "french_fry = $3", "cock  = $3", "pasta  = $5", "maggy  = $4" ]
      print("\n")
      print("***MENU***")
      for i in food_items:
       print(i)
      print("\n")

     # while loop because costumer can choose  more than one item or same item many times
    def order(self):
      global oreder_list
     # list for save order number from the costumer
      oreder_list = []
      while True:
       order = int(input("press 1. for chicken\npress 2. for burger\npress3. for french_fry\npress 4. for cock\npress 5. for pasta\npress 6. for maggy\npress 0. for exit\n"))

       if order == 0:
        break

       if order > 6 or order < 0:
        print("please enter valid number")

       oreder_list.append(order)

       print("anything esls you want ")

      print("wait for 10sec\n ")
      time.sleep(10)

      print("you order these items")

    def foreder_list(self):
      global total

      total = 0
      for i in oreder_list:

       if i == 1:
        print("chicken $9")
        total = total + 9
       elif i == 2:
        print("burger $6")
        total = total + 6
       elif i == 3:
        print("french_fry $3")
        total = total + 3
       elif i == 4:
        print("cock $3")
        total = total + 3
       elif i == 5:
        print("pasta $5")
        total = total + 5
       elif i == 6:
        print("maggy $4")
        total = total + 6


       # giving tax if total is 12
      if total == 12:
       tax = total/100
       total = tax + 1

       print("your total is = ", total, "including tax")

      # if total is more than 20 so giving 10% discount and including 2% tax in total
      elif total > 20:
       tax = (total/100) * 2
       discount = total/10
       total = total - discount + tax
       print("your total is = ", total, "including 10% discount and tax")
      if total < 12:
       print("your total is = ", "$", total)


obj = Mcdonald()

if __name__ == '__main__':

 list1 = []
 name = input("Enter your name = ")
 x = re.findall('[0-9]', name)
 if x:
    print("Please don't use numbers in name")

 list1.append(name)
 email = input("Enter your email = ")
 regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'  # it is use to validate email

 if(re.search(regex, email)):
     pass

 else:
     print("Invalid Email")

 list1.append(email)

 q1 = "INSERT INTO mc_customer (name, email) VALUES(%s, %s) "
 cursor.execute(q1, list1)
 obj1.commit()

 obj.Menu()
 obj.order()
 obj.foreder_list()


