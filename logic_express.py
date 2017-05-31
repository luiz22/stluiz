def greet(friend,money):
    if friend and (money>20):
        print"HI"
        money =money -20
    elif friend:
        print "HELLO"
    else:
        print "No way"
        money = money + 10
    return money
    

money = 15

money = greet(True,money)
print"Money:", money
print ""

