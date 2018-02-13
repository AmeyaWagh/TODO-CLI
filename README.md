# TODO-CLI
a CLI based TODO manager for projects. writes to TODO.md which makes the TODO file github friendly 


- create alias of the todo.py file
eg:
```
  alias todo='$HOME/utilities/TODO/todo.py'
```
- create a todo list file TODO.md, or let todo.py automatically create it for you. Given below is a sample
```
-------------------------------------------------------------------------------- 
	TODO LIST
--------------------------------------------------------------------------------
1) - [x]   Make SVM as ROS Action
2) - [x]   Make SVM trainer script as ROS node
3) - [X]   Make Python Based SVM Classifier
4) - [X]   FullyConnected Classifier using Tensorflow
5) - [x]   Normalize the descriptor.
6) - [ ]   Send a batch of VFH vectors to classifier than individual query.
7) - [ ]   Test with multiple voxel grid sizes.
8) - [ ]   Add detection and drawing of bounding box to common.
9) - [X]   Color in getBoundingBox as hex.

--------------------------------------------------------------------------------
[ TOTAL TASKS] 9
[ COMPLETED] 6
[ REMAINING] 3
--------------------------------------------------------------------------------
```
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
