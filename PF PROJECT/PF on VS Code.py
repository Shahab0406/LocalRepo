from math import *
dic={27:{"name":"Shahab","balance":12345},51:{"name":"Raheel","balance":6430},45:{"name":"Ali","balance":3205}}
ask_acc=eval(input("enter your acc number:"))
print("Plese Enter your Task")
print("For Cash Withdraw enter CW")
print("For Cash deposit enter CD")
print("For Cash Transfer enter CT")
print("For LOAN enter loan")
print("--"*10)

for i,j in dic.items():
    for x,y in j.items():
        if ask_acc==i:
            print(j)
            ASK=input("Do you want to proceed answer in yes or no:")
            if ASK=="yes":
                ask_task=input("enter the tasks given above:")
                
                #Cash Withdraw
                if ask_task=="CW":
                    new_ask=eval(input("enter the ammount of cash:"))
                    if new_ask<j["balance"]:
                        j["balance"]=j["balance"]-new_ask
                        print(j["balance"])
                    #recipt
                        print("Do you want the recipt? it will cost 3 ruppes only enter yes or no to answer")
                        ask_for_recipt=input("enter your answer in yes or no:")
                        if ask_for_recipt=="yes":
                            j["balance"]=j["balance"]-3
                            print(f'NAME:{j["name"]} __Balance deducted:{new_ask}/n__updated Balance:{j["balance"]}')
                        else:
                            print("bye")

                        
                #Cash Deposit       
                if ask_task=="CD":
                    new_ask=eval(input("enter the ammount of cash:"))
                    j["balance"]=j["balance"]+new_ask
                    print(j["balance"])
                #recipt
                    print("Do you want the recipt? it will cost 3 ruppes only enter yes or no to answer")
                    ask_for_recipt=input("enter your answer in yes or no:")
                    if ask_for_recipt=="yes":
                        j["balance"]=j["balance"]-3
                        print(f'NAME:{j["name"]} __Balance deducted:{new_ask}/n__updated Balance:{j["balance"]}')
                    else:
                        print("bye")

                    
                #Cash Transfer    
                if ask_task=="CT":
                    ask_whereToSend=eval(input("enter the account number where to send the ammount:"))
                    for p,q in dic.items():
                        for newp,newq in q.items():
                            if ask_whereToSend==p:
                                new_ask=eval(input("enter your ammount:"))
                                if new_ask<j["balance"]:
                                    j["balance"]=j["balance"]-new_ask
                                    print(j["balance"])
                                #then
                                    q["balance"]=q["balance"]+new_ask
                                    print(q["balance"])
                                #recipt
                                    print("Do you want the recipt? it will cost 3 ruppes only enter yes or no to answer")
                                    ask_for_recipt=input("enter your answer in yes or no:")
                                    if ask_for_recipt=="yes":
                                        j["balance"]=j["balance"]-3
                                        print(f'NAME:{j["name"]} __Balance deducted:{new_ask}/n__updated Balance:{j["balance"]}')
                                    else:
                                        print("bye")

                                    ASK=input("Do you want to proceed answer in yes or no:")
                                    if ASK=="yes":
                                        continue
                                        break
                                        break
                                        
                                    else:
                                        break
                                        break
                                        break
                                        
            else:
                print("Thank You")
                break
                break
        else:
            print("Access Denied!")
            break