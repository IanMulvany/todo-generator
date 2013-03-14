import glob

NOTES_DIR = "~/Dropbox/notes/.*"

notes = glob.glob("/Users/ian/Dropbox/notes/nv/*")

def is_done(line):
	if line.find("@done") >-1 :
		return True
	else:
		return False

def is_todo(line):
	if is_done(line) is False:
		if line.find("@later") > -1:
			return True
		else:
			return False		

def is_maybe(line):
	if line.find("-") ==0 :
		return True
	else:
		return False

def get_nvname(note_name):
	current = note_name.replace(".txt","")
	current2 = current.replace("/Users/ian/Dropbox/notes/nv/","")
	nvname = current2
	return nvname

def long_report():
	for note in notes:
		dones = []
		todos = []
		maybes = []
		lines = open(note,"r").readlines()
		for line in lines:
			test_line = line.strip()
			if is_todo(test_line):
				#print test_line
				todos.append(test_line)
			elif is_done(test_line):
				#print test_line
				dones.append(test_line)
			elif is_maybe(test_line):
				print test_line
				maybes.append(test_line)
			else:
				continue
	"""	
		if len(dones) > 0 or len(todos) > 0 or len(maybes) > 0:
			print "[["+note+"]]"
			print ""
			print "# Todos"
			for todo in todos: print todo
			print ""
			print "# maybes"
			for maybe in maybes: print maybe
			print ""
			print "# dones"
			for done in dones: print done 
			print ""
			print "---"
	"""

def todo_report():
	for note in notes:
		dones = []
		todos = []
		maybes = []
		lines = open(note,"r").readlines()
		for line in lines:
			test_line = line.strip()
			if is_todo(test_line):
				#print test_line
				todos.append(test_line)
			elif is_done(test_line):
				#print test_line
				dones.append(test_line)
			elif is_maybe(test_line):
				maybes.append(test_line)
			else:
				continue
		if len(todos) > 0:
			print "[["+get_nvname(note)+"]]"
			print ""
			print "# Laters"
			for todo in todos: print todo
			print ""
			print "---"


todo_report()