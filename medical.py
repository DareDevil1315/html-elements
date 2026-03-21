medical_cause=input("did you have a medical cause? (Y/N):").strip().upper()
if medical_cause=='Y':
    print("you are allowed")
else:
    atten=int(input("enter the number of students:"))

    if atten>=75:
        print("allowed")
    else:
        print("not allowed")

units=int(input("pls enetr the number of units consumed:"))
if(units<50):
    amount=units*2.60
    surcharge=25

elif(units<=100):
    amount=130+((units-50)*3.25)
    surcharge=35

elif(units<=200):
    amount=130+162.50+((units-100)*5.26)
    surcharge=45

else:
    amount=130+162.50+526+((units-200)*8.45)
    surcharge=75
total=amount+surcharge
print(amount)


print(surcharge)
print("nElectricity bill=%.2f"  %total)

choice=int(input("select ride 1.bike 2.car"))
if (choice==1):
    print("you have selected bike")
elif(choice==2):
    print("you have selected car")