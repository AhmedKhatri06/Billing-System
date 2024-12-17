print("---*Welcome To FAUS Electronics*---")
cust_name=input("Enter Customer Name:-")
cust_no=int(input("Enter Mobile Number:- +91 "))
cust_email=input("Enter Email-ID:-")
total=0
items=[]
sr_no=1
details=[]
details.append((sr_no,cust_name,cust_no,cust_email))
num=int(input("How Many Items:- "))
try:
    if num<=10:
        for i in range(num):
            item_code=int(input("Enter Code Item:-"))
            item_name=input("Enter Item Name:-")
            item_price=float(input("Enter Item Price:- "))
            item_qty=int(input("Enter Item Quantity:-"))
            gst_per=float(input("Enter Percntage of GST:-"))
            gst_amt=((gst_per/100)*item_price)

            item_total=item_qty*item_price+gst_amt
            total += item_total
            items.append((i+1,item_name,item_code,item_price,item_qty,gst_per,item_total))
    else:
        print("Details Not Entered")
except:
    print("You Can not add more than 10 Items")
print("\n")
print("\n")
print("\n")
print("------FAUS Electronics-------")
print("| Customer Name:-",cust_name)
print("| Customer Number:-",cust_no)
print("| Customer Email-ID:-",cust_email)
print("|--------------------------------------------BILL SUMMARY---------------------------------------------------------|")
print(f"| {'Sr.no':<10}        {'Item Name':<10}        {'Item Code':<10}        {'Price':<10}        {'Quantity':<10}    {'GST':<10}      {'Item Total':<10}|")
print("|-----------------------------------------------------------------------------------------------------------------|")
for i in items:
    print(f"| {i[0]:<10}        {i[1]:<20}{i[2]:<10}      {i[3]:<10}        {i[4]:<10}    {i[5]:<10}      {i[6]:<10}|")
    print("|-----------------------------------------------------------------------------------------------------------------|")
print(f"\n Total Amount ={total}")
