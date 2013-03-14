import glob
from collections import defaultdict


"""
# some example decorator code

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

"""


NOTES_DIR = "~/Dropbox/notes/.*"

notes = glob.glob("/Users/ian/Dropbox/notes/nv/*")

"""
def check_later_status(fn):
	def checker(*args):
		tag = args[1]
		line = args[0]
		check_tag = "@later"
		return check_status(fn, line, tag, check_tag)
	return checker"""


def check_done_status(fn):
	# if the tag we are testing is "@done" then ignore this function. 
	test_tag = "@done"
	def checker(*args):
		tag = args[1]
		line = args[0]
		if tag == test_tag: # if the tag is done, just eval the function
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

# @check_later_status
@check_done_status
def has_tag(line, tag):
	if line.find(tag) >-1 :
		return True
	else:
		return False	

"""def is_maybe(line):
	if line.find("-") ==0 :
		return True
	else:
		return False
"""

def get_nvname(note_name):
	current = note_name.replace(".txt","")
	current2 = current.replace("/Users/ian/Dropbox/notes/nv/","")
	nvname = current2
	return nvname

tags = ["@todo", "@done", "@later"]

def parse_notes():
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

note_actions = parse_notes()
print len(note_actions)
report_tag(note_actions, "@todo")
