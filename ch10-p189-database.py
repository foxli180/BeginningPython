import sys,shelve

def store_person(db):
     pid = input('Enter unique ID number:')
     person = {}
     person['name'] = input('Enter name:')
     person['age'] = input('Enter age:')
     person['phone'] = input('Phone number:')
     db[pid] = person

def lookup_person(db):
     pid = input('Enter ID number:')
     field = input('What would u like to know?(name,age,phone)')
     field = field.strip().lower()
     print (field.capitalize()+':'+db[pid][field])


def enter_command():
     cmd = input('Enter command(? for help)')
     cmd = cmd.strip().lower()
     return cmd


def main():
     database = shelve.open('c:/1/database.dat')
     try:
          while True:
               cmd = enter_command()
               if cmd == 'store':
                    store_person(database)
               elif cmd == 'lookup':
                    lookup_person(database)
               elif cmd == '?':
                    pass
               elif cmd == 'quit':
                    return
     finally:
          database.close()


if __name__ == '__main__':main()

          
               
