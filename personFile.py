class Shirt:

  def __init__(self,_color,_length,_hasButtons,_size):
    self.color = _color
    self.length = _length
    self.buttons = _hasButtons
    self.size = _size



class Person:

  def run(self):
    if self.currentFood <= 0:
      print("You can't run, you need to eat first!")
    else:
      self.currentFood -= 2
      print("Run Run Run")
      print("Current Food is "+str(self.currentFood))
  
  #Waiter that takes the order
  def __init__(self,_name,_height,_weight,_hairColor,_hairLength,_age,_shirt):
    self.name = _name
    self.height = _height
    self.age = _age
    self.hairLength = _hairLength
    self.hairColor = _hairColor
    self.weight = _weight
    self.shirt = _shirt
    self.maxFood = 30
    self.currentFood = 4


BobsShirt = Shirt("blue",23,True,700)
Bob = Person("Bob",71,278,"brown","long",39,BobsShirt)

Bob.run()
Bob.run()
Bob.run()
Bob.run()
Bob.run()
Bob.run()
