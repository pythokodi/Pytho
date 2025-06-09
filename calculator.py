while True:
   print ("1- Addition ")
   print ("2- difference ")
   print ("3- multiplication ")
   print ("4- division ")
   print ("5- exit")
   choice = str (input (" enter your choice:"))
   num1= float (input (" enter the number 1: "))
   num2=float (input(" enter the  number 2:  "))
   if choice == "1":
      print ("=",num1+num2)
   elif choice =="2":
      print ("=",num1-num2)
   elif choice == "3":
      print ("=",num1*num2)
   elif choice == "4":
      if num2 <= 0 :
         print(" error!! ")
      else:
         print (num1/num2)
   elif choice =="5":
      break  
   else:
      print ("error!!!")
   