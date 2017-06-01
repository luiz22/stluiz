#Example of data type LIST

grocery_lsit = ['Juice', 'Tomatoes','Potatoes','bananas']
print("First item", grocery_lsit[0])
grocery_lsit[0]= "Green Juice"			#change value of index 0 in grocerylist
print("first Item", grocery_lsit[0])

print(grocery_lsit[1:3]) #Print subset of grocerylist up to third index 


#insert list inside list

other_events =['wash car','pick up kids','cash check']

to_do_list =[other_events, grocery_lsit]
print(to_do_list)

print((to_do_list[1][1]))

grocery_lsit.append('onions')
print(to_do_list)

grocery_lsit.insert(1,'Kwesi')
grocery_lsit.remove("Kwesi")

grocery_lsit.sort()

grocery_lsit.reverse()

del grocery_lsit[4]
print(to_do_list)

to_do_list2 =other_events + grocery_lsit
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))





