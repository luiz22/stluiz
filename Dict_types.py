
tennis_super_stars = {"Roland Garos": "Rapheal Nadal","Wimbleden Open":"Roger Federer","Australian Open":"Novak Djokovic","French Open":"Stan Warinka","US Open":"Andy Murray"}


print(tennis_super_stars["Wimbleden Open"]) #print tennis super star

del tennis_super_stars["Roland Garos"] #del tournament

tennis_super_stars['US open']= "thomas berdych" #replace a tennis super star

print(len(tennis_super_stars))

print(tennis_super_stars.get('Novak Djokovic'))

#print(tennis_super_stars.key())
print(tennis_super_stars.values())
