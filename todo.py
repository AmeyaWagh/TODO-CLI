#!/usr/bin/python

import os
import sys
import termcolors as tc
import datetime

class TODOList:
	usage = '''
	CLI TODO list

	usage
	--------------------------------
	create - 				creates TODO.md
	ls - 					show TODO list
	add <Task message> - 	adds TASK 
	remove <TASK ID> - 		removes TASK 
	check <TASK ID> - 		checks TASK 
	uncheck <TASK ID> - 	unchecks TASK  
	--------------------------------
	'''
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
		print "-"*80,"\n\tTODO LIST\n","-"*80
		print self.parse_file()
		print "-"*80
		print "[ TOTAL TASKS] {}".format(self.tasks)
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

if __name__ == '__main__':
	
	td = TODOList()
	td.parse_args()
	# print sys_args