stars = [ ]
while True:
    print ("ما هو ختيارك☆")
    print ("1-إضافة امنية")
    print ("2-مسح امنية محددة ")
    print ("3-عرض قائمة أمنياتك")
    print ("4-خروج")
    print ("5-مسح الكل")
    x  = input (">>>")
    
    #سوأل
    
    if x =="1":
       S=input ("ادخل امنيتك هنا :")
       stars.append(S)
    elif x =="2":
       S2 = input ("ماهي الأمنية التي تريد حذفها : ")
       if S2 in stars:
          stars.remove(S2)
       else:
          print ("لا يوجد ضمن قائمة أمنياتك ")
    elif x == "3":
       print (stars)
    elif x == "4":
       break 
    elif x =="5":
       stars.clear()
    else  :
       print ("خطأ اعد المحاولة")