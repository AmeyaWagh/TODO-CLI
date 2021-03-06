#!/usr/bin/python

import os
import sys
import termcolors as tc
import datetime
import argparse

class TODOList:
    usage = '''
    {} A CLI BASED TODO list{}

    a CLI based TODO manager for projects. 
    writes to TODO.md which makes the TODO file github friendly
    
    todo --help for help
    -----------------------------------------
    '''.format(tc.HEADER,tc.ENDC)
    def __init__(self):
        if "TODO.md" not in os.listdir(os.getcwd()):
            print("No TODO.md Found")
            ip = raw_input("Do you wish to create? Y/N?")
            if (ip=="y") or (ip=="Y"):
                self.create_file()
            exit()
        self.read_file()
        self.tasks = 0
        self.completed_tasks = 0
        self.remaining_tasks = 0
        self.task_buffer = {}

    def create_file(self):
        self.todo_file = "## TODO TASKLIST\n"
        self.write_file()
        print "TODO.md created"

    def read_file(self):
        with open(os.path.join(os.getcwd(),"TODO.md"),'r') as fp:
            self.todo_file = fp.readlines()
        if '\n' in self.todo_file: 
            self.todo_file.pop(self.todo_file.index('\n'))  

    def write_file(self):
        with open(os.path.join(os.getcwd(),"TODO.md"),'w') as fp:
            fp.write(''.join(self.todo_file))       

    def parse_file(self):
        print_buffer = ""
        self.tasks = 0
        self.completed_tasks = 0
        for line in self.todo_file:
            if ('-' in line) and ('[' in line) and (']' in line):
                self.tasks+=1
                self.task_buffer[self.todo_file.index(line)] = line
                if ('[x]' in line) or ('[X]' in line):
                    self.completed_tasks+=1
                    print_buffer += "{}) ".format(self.todo_file.index(line))+tc.OKGREEN+line+tc.ENDC
                else:
                    print_buffer += "{}) ".format(self.todo_file.index(line))+tc.FAIL+line+tc.ENDC
        return print_buffer
        
    def pretty_print(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print "-"*80,"\n\t{}TODO LIST{}\n".format(tc.BOLD,tc.ENDC),"-"*80
        print self.parse_file()
        print "-"*80
        print tc.BOLD+"[ TOTAL TASKS] {}".format(self.tasks)
        print tc.OKGREEN+"[ COMPLETED] {}".format(self.completed_tasks)
        print tc.WARNING+"[ REMAINING] {}".format(self.tasks-self.completed_tasks)+tc.ENDC
        print "-"*80
        self.write_file()
        # print self.task_buffer
            
    def add_task(self,task_str):
        self.todo_file.append('- [ ] {} [CREATED] {}\n'.format(task_str,datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")))
        # self.todo_file.append('\n')
        # print self.todo_file
        self.pretty_print() 

    def check_task(self,task_id):
        self.parse_file()
        task_idx = self.todo_file.index(self.task_buffer[int(task_id)])
        self.todo_file[task_idx] = self.todo_file[task_idx].replace("[ ]","[x]")
        self.pretty_print()

    def uncheck_task(self,task_id):
        self.parse_file()
        task_idx = self.todo_file.index(self.task_buffer[int(task_id)])
        # print ">>",self.todo_file[task_idx]
        self.todo_file[task_idx] = self.todo_file[task_idx].replace("[x]","[ ]")
        self.todo_file[task_idx] = self.todo_file[task_idx].replace("[X]","[ ]")
        self.pretty_print()

    def remove_task(self,task_id):
        self.parse_file()
        task_idx = self.todo_file.index(self.task_buffer[int(task_id)])
        self.todo_file.pop(task_idx)
        self.pretty_print()


    def parse_args(self):
        sys_args = sys.argv[1:]
        # print sys_args
        try:    
            if "ls" in sys_args[0]:
                # print td.todo_file
                td.pretty_print()
            elif "add" in sys_args[0]:
                td.add_task(sys_args[1])
            elif "check"==sys_args[0]:
                td.check_task(sys_args[1])
            elif "uncheck"==sys_args[0]:
                td.uncheck_task(sys_args[1])
            elif "remove" in sys_args[0]:
                td.remove_task(sys_args[1])     
            else:
                print td.usage
        except Exception as e:
            print td.usage

    def parse_args_2(self):
        desc = """
        a CLI based TODO manager for projects. \n writes to TODO.md which makes the TODO file github friendly
        """
        parser = argparse.ArgumentParser(description=desc)
        parser.add_argument('--ls', help='show TODO list' , action='store_true')
        # parser.add_argument('--create', help='create TODO list', action='store_true')
        parser.add_argument('--add', help='add TODO list',type=str)
        parser.add_argument('--check', help='add TODO list',type=int)
        parser.add_argument('--uncheck', help='add TODO list',type=int)
        parser.add_argument('--remove', help='add TODO list',type=int)
        args = parser.parse_args()
        print(">>",args)
        try:    
            if args.ls:
                self.pretty_print()
            elif args.add is not None:
                td.add_task(args.add)
            elif args.check is not None:
                td.check_task(args.check)
            elif args.uncheck is not None:
                td.uncheck_task(args.uncheck)
            elif args.remove is not None:
                td.remove_task(args.remove)     
            else:
                print td.usage
        except Exception as e:
            print td.usage

if __name__ == '__main__':
    
    td = TODOList()
    td.parse_args_2()
    # print sys_args