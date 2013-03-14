import glob
from collections import defaultdict
from optparse import OptionParser

NOTES_DIR = "~/Dropbox/notes/.*"

def isInFilter(s):
	filter_list = ["current-todos", "current-later", "current-dones"]
	for f in filter_list:
	    if s.find(f) != -1:
	        return False
	    else:
	    	continue
	return True

def get_notes():
	notes = glob.glob("/Users/ian/Dropbox/notes/nv/*")
	temp = filter(isInFilter, notes)
	return temp

def check_status(fn, test_tag):
	def checker(*args):
		tag = args[1]
		line = args[0]
		if tag == test_tag: 
			# if the tag we are testing
			# is the smdone, just eval the function
			return fn(line, tag)
		else:
			if line.find(test_tag) >-1 : 
				# if the tag is not @ done, return false if @done is in 
				# the line
				return False
			else:
				# else eval the function
				return fn(line, tag)
	return checker

def check_done_status(fn):
	return check_status(fn, "@done")

def check_later_status(fn):
	return check_status(fn, "@later")

@check_later_status
@check_done_status
def has_tag(line, tag):
	if line.find(tag) >-1 :
		return True
	else:
		return False	

def get_nvname(note_name):
	current = note_name.replace(".txt","")
	current2 = current.replace("/Users/ian/Dropbox/notes/nv/","")
	nvname = current2
	return nvname

tags = ["@todo", "@done", "@later"]

def parse_notes(notes):
	note_actions = []
	for note in notes:
		note_tags = defaultdict(list)
		lines = open(note,"r").readlines()
		for line in lines:
			test_line = line.strip()
			for tag in tags:
				if has_tag(test_line, tag):
					note_tags[tag].append(test_line)
		note_actions.append([note, note_tags])
#		print note
	return note_actions

def report_tag(note_actions, tag):
	for note in note_actions:
		note_name = note[0]
		actions = note[1]
		if len(actions) > 0:
			tag_actions = actions[tag]
			if len(tag_actions) > 0:
				print "# " + "[["+get_nvname(note[0])+"]]:"
				for action in tag_actions:
					print action
				print ""

parser = OptionParser()
parser.add_option("-t", "--type", dest="type", help="pick type of action to look for t - @todo, l @later, d @done", metavar="FILE")
(options, args) = parser.parse_args()
type = options.type 

notes = get_notes()
note_actions = parse_notes(notes)

if type == "t":
	report_tag(note_actions, "@todo")
elif type == "d":
	report_tag(note_actions, "@done")
elif type == "l":
	report_tag(note_actions, "@later")
else:
	print "no action type specified"