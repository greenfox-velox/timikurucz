import sys
import csv

class TodoApp:
    def __init__(self):
        self.file_name = 'todo_list.csv'
        self.main_menu_text = 'Python Todo application\n=======================\n\nCommand line arguments:\n -l   Lists all the tasks\n -a   Adds a new task\n -r   Removes a task\n -c   Completes a task'

    def create_file(self):
        f = open(todo_list+'.'+csv,'w')

    def create_file_if_missing(self):
        try:
            g = open(self.file_name,'a')
            g.close()
        except FileNotFoundError:
            self.create_file()

    def list_todos(self):
        f = open(self.file_name)
        text_list = csv.reader(f, delimiter = ';')
        output = ''
        i = 0
        for line in text_list:
            i += 1
            output += (str(i) + ' - ' + self.checked_or_not(line[0]) + ' ' + line[1] + '\n')
        f.close()
        if output == '':
            return 'No todos for today! :)'
        else:
            return output

    def add_task(self, new_task):
        f = open(self.file_name, 'a')
        f.write('False;' + new_task + '\n')
        f.close()

    def checked_or_not(self, x):
        if x == 'True':
            return '[x]'
        else:
            return '[ ]'

    def check_task(self, task_num):
        try:
            f = open(self.file_name)
            check_task = csv.reader(f, delimiter = ';')
            output = []
            for i in check_task:
                output.append(i)
            if output[int(task_num)-1][0] == 'False':
                output[int(task_num)-1][0] = 'True'
            f.close()
            f = open(self.file_name, 'w')
            for i in output:
                f.write(i[0] + ';' + i[1] + '\n')
            f.close()
        except IndexError:
            print('Unable to check: Index is out of bound')
        except ValueError:
            print('Unable to check: Index is not a number')

    def remove_task(self, task_num):
        f = open(self.file_name)
        text_list = f.readlines()
        try:
            text_list.remove(text_list[int(task_num)-1])
        except ValueError:
            print('Unable to remove: Index is not a number')
        except IndexError:
            print('Unable to remove: Index is out of bound')
        f.close()
        f = open(self.file_name, 'w')
        for line in text_list:
            f.write(line)
        f.close()

    def argument_is_ok(self):
        argvs = ['-l', '-a', '-r', '-c']
        if sys.argv[1] not in argvs:
            print('Unsupported argument')
            print(self.main_menu_text)

    def controller_l(self):
        if len(sys.argv) == 2:
            print(self.list_todos())
        else:
            print('Hoho, you gave much arguments!')

    def controller_a(self):
        if len(sys.argv) == 2:
            print ('Unable to add: No task is provided')
        else:
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

    def main(self):
        self.create_file_if_missing()
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
                
sample = TodoApp()
sample.main()
