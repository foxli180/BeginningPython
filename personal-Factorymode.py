class Operation:

     def __init__(self):
          __NumberA = 0.0
          __NumberB = 0.0

     def NumberA(self,value):
          def __get__(self):
               return self.__NumberA
          def __set__(self,value):
               self._NumberA = value

     
     def NumberB(self,value):
          def __get__(self):
               return self.__NumberB
          def __set__(self,value):
               self._NumberB= value

     def getResult(self):
          result = 0.0
          return result

class OperationAdd(Operation):

     def getResult (self):
          result = 0.0
          result = self.NumberA + self.NumberB
          return result

     
class OperationSub(Operation):
     def getResult(self):
          result = 0.0
          result = self.NumberA - self.NumberB
          return result


class OperationMul(Operation):
     def getResult(self):
          result = 0.0
          result = self.NumberA * self.NumberB
          return result


class OperationDiv(Operation):
     def getResult(self):
          result = 0.0
          try:
               result = self.NumberA/self.NumberB
          except ZeroDivisionError:
               print ("Check NumberB:"+" divison by zero")


class OperationFactory:
     @staticmethod
     def CreateOperrator(operator):
          oper = Operation ()
          oper = {
               '+' : lambda : OperationAdd(),
               '-' : lambda : OperationSub(),
               '*' : lambda : OperationMul(),
               '/' : lambda : OperationDiv()
               }[operator]()
     
     
          return oper


def test():
     #oper = Operation()
     oper = OperationFactory.CreateOperrator('*')
     oper.NumberA = 20
     oper.NumberB = 30
     print (oper.getResult())


if __name__ =='__main__':test()



