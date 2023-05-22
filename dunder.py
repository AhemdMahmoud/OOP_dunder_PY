class Order:
  
  def __init__ (self, cart, customer):
    self.cart=cart
    self.customer=customer

  
 #overloding
  def __len__(self):      #len(object)
    return len(self.cart) 

  
  def __call__(self):   #call object like order()
    print(f"{self.customer}")

  
  def __str__(self): #to show object as a string
    return f"{self.customer}" 

  
  def __repr__(self):    #insted of __str__
    return f" order(list of item ,customer name?)" 

  def __bool__ (self): #to show true or false
    return len(self.cart)>0 
  
  def add_item(self,other):
    return self.cart.append(other)



  def __add__(self,other):
    return self.cart.append(other)

  def __iadd__(self,other): #in order to add like x+=5 
    self.cart.append(other)   #to add an object  from calss  to string
    # you can add item in the first by insert instead of  append
    return self

  def __radd__(self,other): #in order to add like x+=5 
    self.cart.insert(0,other)
    return self



  # to show index_item from object we use __getitem__(se)
  def __getitem__(self,key):
   return self.cart[key]


# we can change item from list by index  like order [0]="monitor" using __setitem__
  def __setitem__ (self ,key,value):
     self.cart[key]= value 
     return self

order =Order(["laptop", "mac"],"Ahmed")
# print (len(order))
 # order()    #by call dunder method
# print (order)
# print (repr(order))



# order =Order(["mouse","key"],"Ahmed") #order is empty
# if order :
#   print (f"{order.customer} order is processing")
# else:
#   print (f"shopping cart is empty")
# print (bool(order))  



# order.add_item("mause")
# print (order.cart)          #by add_item dunder methode

# we try other dunder methode using __add__ to + 

# order+"sub"
# print (order.cart)


 #__iadd__

# order+="usb"
# print (order.cart)


# same previous dunder methode like  __mul__ ,__div__,__sub__ and you can add i in the front like  __imul__ ,__idiv__,__isub__  to operation like   /= or ,,,, 



# __radd__

# order ="woofer"+order

# print (order.cart) 

# __getitem__
# print (order[0])

# __setitem__
# order[0]="Keyboard"
# print (order.cart)   #output= ['Keyboard', 'mac'] 


