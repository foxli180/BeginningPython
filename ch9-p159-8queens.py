#-*-coding:utf-8-*-
'''
判断下一个位置是否有冲突
1. 这个新的位置在 Y 轴方向跟之前的所有位置不冲突(不在同一竖线上)  
2. 这个新的位置在 X 轴方向跟之前的所有位置不冲突(不在对角线上)
'''
def conflict(state,nextX):
     nextY = len(state) #nextY 为新位置的 Y 轴坐标
     for i in range(nextY):
          #state[i]-nextX 新位置与之前位置 [i] 的 X 轴距离
          #nextY-i        新位置与之前位置  i  的 Y 轴距离
          #state[i]-nextX == 0 表示新位置和原来的位置在同一直线上
          #state[i]-nextX == nextY-i 新位置到点 i 的 X Y 轴距离相等(在对角线上)
          if abs (state[i]-nextX) in (0,nextY-i):
               return True
     return False  


def queens(num, state=[]):
     for pos in range(num): # 定义一个一位置
          if not conflict(state,pos): #如果这个位置和之前的位置没有冲突的话
               if len(state) == num-1:#同时这个位置是最后一个位置
                    yield [pos] #等待处理这个位置
               else:#如果这个位置和之前位置没有冲且不是最后一个位置
                    for result in queens(num,state + [pos]): #递归这个位置
                         yield [pos]+result
               
         
               
          
def prettyprint(solution):
     def line(pos,length=len(solution)):
          return ' . '*(pos) + ' x ' + ' . '*(length-pos-1)

     for pos in solution:
          print (line(pos))
