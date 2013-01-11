class Secretive:
     #1. private method
     def __invisible(self):
          print ('but u can not see me')
     #2. private mesthod can be visited via class method
     def visible(self):
          print ('you can see me')
          self.__invisible()


a = Secretive()
a.visible()
print()
a._Secretive__invisible()#3.terrible....
