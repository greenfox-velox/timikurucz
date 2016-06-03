import sys
import csv
import os

class TodoApp:
    def __init__(self):
        self.main_menu_text = "\n\nMake a list so you won't forget anything\n========================================\n\nCommand line arguments:\n\n -la      List all lists\n -create  Create a new list\n -l       List the tasks from the chosen list\n -a       Add new task to the chosen list\n -r       Remove a task from the chosen list\n -c       Complete a task in the chosen list\n -rc      Uncomplete a task in the chosen list"

    def create_file(self):
        input = str(sys.argv[2])
        f = open(input + '.csv','w')
        f.close()

    def is_there_already_same_file(self, this_file):
        for file in os.listdir("."):
            if file.endswith(".csv") and file.startswith(str(this_file)):
                return True

    def list_all_csv(self):
        for file in os.listdir("."):
            if file.endswith(".csv"):
                print(file)

    def add_task(self, new_task):
        if self.is_there_already_same_file(sys.argv[3]):
            f = open(str(sys.argv[3]) + '.csv', 'a')
            f.write('False;' + new_task + '\n')
            f.close()
        else:
            print('There is no file like this.'
            'Please create a new one or try typing correctly.')

    def list_todos(self):
        if self.is_there_already_same_file(sys.argv[2]):
            f = open(str(sys.argv[2]) + '.csv', 'r')
            text_list = csv.reader(f, delimiter = ';')
            output = ''
            i = 0
            for line in text_list:
                i += 1
                output += (str(i) + ' - ' + self.checked_or_not(line[0]) + ' ' + line[1] + '\n')
            if output == '':
                return 'Yay, no todos for today! :)'
            else:
                return output
        else:
            return 'There is no file like this. Please create a new one or try type correctly.'
        f.close()

    def checked_or_not(self, x):
        if x == 'True':
            return '[x]'
        else:
            return '[ ]'

    def write_task(self, input):
        f = open(str(sys.argv[3]) + '.csv', 'w')
        for i in input:
            f.write(i[0] + ';' + i[1] + '\n')
        f.close()

    def check_task(self, task_num):
        if self.is_there_already_same_file(sys.argv[3]):
            try:
                f = open(str(sys.argv[3]) + '.csv', 'r')
                check_task = csv.reader(f, delimiter = ';')
                output = []
                for i in check_task:
                    output.append(i)
                if output[int(task_num)-1][0] == 'False':
                    output[int(task_num)-1][0] = 'True'
                f.close()
                self.write_task(output)
            except IndexError:
                print('Unable to check: Index is out of bound')
            except ValueError:
                print('Unable to check: Index is not a number')

    def uncheck_task(self, task_num):
        if self.is_there_already_same_file(sys.argv[3]):
            try:
                f = open(str(sys.argv[3]) + '.csv', 'r')
                check_task = csv.reader(f, delimiter = ';')
                output = []
                for i in check_task:
                    output.append(i)
                if output[int(task_num)-1][0] == 'True':
                    output[int(task_num)-1][0] = 'False'
                f.close()
                self.write_task(output)
            except IndexError:
                print('Unable to check: Index is out of bound')
            except ValueError:
                print('Unable to check: Index is not a number')

    def remove_task(self, task_num):
        if self.is_there_already_same_file(sys.argv[3]):
            f = open(str(sys.argv[3]) + '.csv', 'r')
            text_list = f.readlines()
            try:
                text_list.remove(text_list[int(task_num)-1])
            except ValueError:
                print('Unable to remove: Index is not a number')
            except IndexError:
                print('Unable to remove: Index is out of bound')
            f.close()
            f = open(str(sys.argv[3]) + '.csv', 'w')
            for line in text_list:
                f.write(line)
            f.close()

    def argument_is_ok(self):
        argvs = ['-l', '-a', '-r', '-c', '-rc', '-la', '-create']
        if sys.argv[1] not in argvs:
            print('Unsupported argument')
            print(self.main_menu_text)

    def controller_l(self):
        if len(sys.argv) == 3:
            print(self.list_todos())
        else:
            print('Hoho, you gave much arguments!')

    def controller_a(self):
        if len(sys.argv) == 2:
            print ('Unable to add: No task is provided')
        else:
            self.is_there_already_same_file(sys.argv[3])
            self.add_task(sys.argv[2])

    def controller_r(self):
        if len(sys.argv) == 2:
            print ('Unable to remove: No index is provided')
        else:
            self.remove_task(sys.argv[2])

    def controller_c(self):
        if len(sys.argv) == 2:
            print ('Unable to check: No index is provided')
        else:
            self.check_task(sys.argv[2])

    def controller_rc(self):
        if len(sys.argv) == 2:
            print ('Unable to uncheck: No index is provided')
        else:
            self.uncheck_task(sys.argv[2])

    def controller_la(self):
        if len(sys.argv) == 2:
            self.list_all_csv()

    def main(self):
        if len(sys.argv) == 1:
            print(self.main_menu_text)
        else:
            self.argument_is_ok()
            if (sys.argv[1]) == '-l':
                self.controller_l()
            elif (sys.argv[1]) == '-a':
                self.controller_a()
            elif (sys.argv[1]) == '-r':
                self.controller_r()
            elif (sys.argv[1]) == '-c':
                self.controller_c()
            elif (sys.argv[1]) == '-rc':
                self.controller_rc()
            elif (sys.argv[1]) == '-la':
                self.controller_la()
            if (sys.argv[1]) == '-create':
                self.create_file()

sample = TodoApp()
sample.main()
