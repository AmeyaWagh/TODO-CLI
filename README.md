# TODO-CLI
a CLI based TODO manager for projects. writes to TODO.md which makes the TODO file github friendly 


- create alias of the todo.py file and add it to your .bashrc or .zshrc
eg:
```
  alias todo='$HOME/<path to TODO>/todo.py'
```
- create a todo list file TODO.md, or let todo.py automatically create it for you. Given below is a sample


![alt text](doc/image.img)

- usage
```
	CLI TODO list

	usage
	---------------------------------------
	ls - 			show TODO list
	add <Task message> - 	adds TASK 
	remove <TASK ID> - 	removes TASK 
	check <TASK ID> - 	checks TASK 
	uncheck <TASK ID> - 	unchecks TASK  
	---------------------------------------
```
- goto the directory where TODO.md is saved and use todo alias.
	- to list tasks
```
$todo ls
```
	- to add a TASK
```
$todo add "create custom ROS message for classifier."
```
	- to remove a TASK
```
$todo remove 5
```
	- to check a TASK once it is done
```
$todo check 7
```
	- to uncheck a TASK, (just in case)
```
$todo uncheck 9
```

- This is how the TODO.md looks on github

![alt text](doc/image2.img)