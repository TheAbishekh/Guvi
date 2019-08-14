name="Abi"
pin=1111
bal=int(10000)
i=1
a=0
for i in range(10):
    nam=str(input("Enter your name:"))
    if nam==name:
        pinin=int(input("Enter your PIN:"))
        while a<3:
            if pin==pinin:
                amt=int(input("Enter the amount:"))
                if (bal>amt):
                        bal=bal-amt
                        print("Remaining Balance is")
                        print(bal)
                        
                        break
                else:
                    print("Insufficient Funds")
                
            else:
                print("Wrong PIN")
                a=a+1
                pinin=int(input("Enter your PIN:"))
                if a==3:
                    print("No more attempts")
                    break
 
    else:
        continue
