import sys

class TodoApp:
    def __init__(self):
        self.file_name = 'todo-list.txt'
        self.main_menu_text = 'Python Todo application\n=======================\n\nCommand line arguments:\n -l   Lists all the tasks\n -a   Adds a new task\n -r   Removes a task\n -c   Completes a task'

    def create_file(self):
        f = open(todo-list+"."+txt,'a')

    def create_file_if_missing(self):
        try:
            g = open(self.file_name,'a')
        except FileNotFoundError:
            self.create_file()

    def list_todos(self):
        f = open(self.file_name)
        text_list = f.readlines()
        f.close()
        output = ''
        i = 0
        for line in text_list:
            i += 1
            output += str(i) + ' - ' + line
        if output == '':
            return 'No todos for today! :)'
        else:
            return output

    def add_task(self, new_task):
        f = open(self.file_name, 'a')
        f.write(new_task + '\n')
        f.close()

    def remove_task(self, task_num):
        f = open(self.file_name)
        text_list = f.readlines()
        try:
            if (len(text_list)) == 1 and task_num == len(text_list):
                text_list.remove(text_list[0])
            elif (len(text_list)) < int(task_num):
                print('Unable to remove: Index is out of bound')
            else:
                text_list.remove(text_list[int(task_num)-1])
        except ValueError:
            print('Unable to remove: Index is not a number')
        f.close()
        g = open(self.file_name, 'w')
        for line in text_list:
            g.write(line)
        g.close()

    def argument_is_ok(self):
        argvs = ['-l', '-a', '-r', '-c']
        if sys.argv[1] not in argvs:
            print('Unsupported argument')
            print(self.main_menu_text)

    def what_to_do_when_first_argv_is_l(self):
        if len(sys.argv) == 2:
            if (sys.argv[1]) == '-l':
                print(self.list_todos())

    def what_to_do_when_first_argv_is_a(self):
        if len(sys.argv) == 2:
            print ('Unable to add: No task is provided')
        else:
            self.add_task(sys.argv[2])

    def what_to_do_when_first_argv_is_r(self):
        if len(sys.argv) == 2:
            print ('Unable to remove: No index is provided')
        else:
            self.remove_task(sys.argv[2])

    def main(self):
        self.create_file_if_missing()
        if len(sys.argv) == 1:
            print(self.main_menu_text)
        else:
            self.argument_is_ok()
            if (sys.argv[1]) == '-l':
                self.what_to_do_when_first_argv_is_l()
            elif (sys.argv[1]) == '-a':
                self.what_to_do_when_first_argv_is_a()
            elif (sys.argv[1]) == '-r':
                self.what_to_do_when_first_argv_is_r()


sample = TodoApp()
sample.main()
