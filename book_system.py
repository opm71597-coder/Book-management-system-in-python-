from os import listdir,system
from time import strftime
c_time=strftime("%H:%M:%S")
#making all storage file
if("bill_data.txt" not in listdir()):
  system(" touch bill_data.txt")
if("suciryte_data.txt" not in listdir()):
  system(" touch suciryte_data.txt")
if("stock_data.txt" not in listdir()):
  system(" touch stock_data.txt")
if("rent_data.txt" not in listdir()):
  system(" touch rent_data.txt")
if("book_list_data.txt" not in listdir()):
  system(" touch book_list_data.txt")
if("total_data.txt" not in listdir()):
  system(" touch total_data.txt")
if("con_data.txt" not in listdir()):
  system("touch con_data.txt")


#####
def bill():
  print("1.make bill")
  print("2.see bill ")
  x=input("enter :")
  if(x=="1"):
   c_name=input("enter cousemur name :")
   b_name=input("enter purches book name :")
   num_c=input("enter cousetmur number :")
   p_b=input("enter book prize :")
   with open("bill_data.txt","a") as f:
    f.write(f"coustemur name ={c_name}  , book name={b_name} , coustemur name ={num_c} book prize={p_b}  time ={c_time}  \n")
   with open("total_data.txt","a") as f:
    f.write(p_b +"\n")
   with open("con_data.txt","a") as f :
    f.write(f"name={c_name}  number={num_c} \n")
   with open("suciryte_data.txt","a") as f:
    f.write(f" name={c_name} ,coun=bill counter , money={p_b}, phone number ={num_c} time ={c_time} \n")
   print(f"coustemur name ={c_name}  , book name={b_name} , coustemur name ={num_c} book prize={p_b} time ={c_time}")
  elif(x=="2"):
   with open("bill_data.txt","r") as f :
    list_bill=f.readlines()
   for i,bill in enumerate(list_bill,start=1):
    print(f"{i}.{bill}")
  else:
   print("only from options (number)")

###
def rent():
  print("1.add rent ")
  print("2.see rent")
  print("3.remove rent")
  x=input("enter :")
  if(x=="1"):
   r_c_name=input("enter custemur name :")
   r_b_name=input("enter rent book name :")
   num_r_c=input("enter coustemur number :")
   addres_r=input("enter coustemur address :")
   prize_r=input("enter book prize :")
   date_ex=input("enter back book date :")
   with open("rent_data.txt","a") as f:
    f.write(f" coustemur name={r_c_name}, rent_book_name ={r_b_name} , COUSTEMUR_NUMBER={num_r_c} , prize ={prize_r}, rent_time{c_time}, expire={date_ex} \n")
   with open("total_data.txt","a") as f:
    f.write(prize_r +"\n")
   with open("con_data.txt","a") as f:
    f.write(f"name={r_c_name}, number={num_r_c} \n")
   with open("suciryte_data.txt","a") as f:
    f.write(f"counter =rent counter ,name ={r_c_name},phone number={num_r_c} , money={prize_r} , time={c_time} \n")
  elif(x=="2"):
    with open("rent_data.txt","r") as f:
     ren_da_l=f.readlines()
    for i,data_r in enumerate(ren_da_l,start=1):
     print(f"{i}.{ren_da_l}")
  elif(x=="3"):
    with open("rent_data.txt","r") as f:
     rent_data_l_r=f.readlines()
    for i,dt in enumerate(rent_data_l_r,start=1):
     print(f"{i}.{dt}")
    try:
     num_r_r=int(input("enter what you whant to delet (number) :"))
    except:
     print("invalid input")
    rent_data_l_r.pop(num_r_r-1)
    with open("rent_data.txt","w") as f:
     f.writelines(rent_data_l_r)
  else:
   print("only from this optin (number)")


#####
def stock():
  print("1.add stock")
  print("2.see stock ")
  print("3.delet stock")
  x=input("enter :")
  if(x=="1"):
   name_s=input("enter stock name :")
   prize_s=input("enter prize of stock ")
   num_s=input(" in a stock how books :")
   name_s_fill=input("enter your name :")
   with open("stock_data.txt","a") as f:
    f.write(f"{name_s} = {num_s} by {name_s_fill} prize={prize_s} \n")
   with open("suciryte_data.txt","a") as f:
    f.write(f"counter = stok , stock add by {name_s_fill}, num={num_s} stock name ={name_s} \n")
  elif(x=="2"):
   with open("stock_data.txt","r") as f:
    s_l=f.readlines()
   for i,sol in enumerate(s_l,start=1):
    print(f"{i}.{sol}")
  elif(x=="3"):
   with open("stock_data.txt","r") as f:
    s_l_r=f.readlines()
   for i,dcc in enumerate(s_l_r,start=1):
    print(f"{i}.{dcc}")
   try:
    num_s_r=int(input("enter what you want to delet (number) :"))
   except:
    print("linvalid input")
   s_l_r.pop(num_s_r-1)
   with open("stock_data.txt","w") as f:
    f.writelines(s_l_r)
  else:
   print("only from this option (number) ")
###
def books():
  print("1.add books")
  print("2.see books")
  print("3.remove book")
  x=input("enter :")
  if(x=="1"):
   book_n=input("enter book name :")
   with open("book_list_data.txt","a") as f:
    f.write(book_n+"\n")
  elif(x=="2"):
    with open("book_list_data.txt","r") as f:
     book_list=f.readlines()
    for i,goh in enumerate(book_list,start=1):
     print(f"{i}.{goh}")
  elif(x=="3"):
    with open("book_list_data.txt","r") as f:
     book_list_r=f.readlines()
    for i,ghh in enumerate(book_list_r,start=1):
     print(f"{i}.{ghh}")
    try:
     num_l_r=int(input("enter what you want delet (number) :"))
    except:
     print("invalid linput")
    book_list_r.pop(num_l_r-1)
    with open("book_list_data.txt","w") as f:
     f.writelines(book_list_r)
  else:
   print("only from my option (number)")

def get_total():
    total_sum = 0

    with open("total_data.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line != "":
                total_sum += int(line)

    return total_sum



def main():
 while True:
  print("1.bill counter ")
  print("2.book list")
  print("3.rent")
  print("4.stock")
  print("5.total")
  print("6.exit")
  x=input("enter :")
  if(x=="6"):
   break
  elif(x=="1"):
   bill()
  elif(x=="2"):
   books()
  elif(x=="3"):
   rent()
  elif(x=="4"):
   stock()
  elif(x=="5"):
   print(get_total())
  else:
   print("only form option (number)")

main()
