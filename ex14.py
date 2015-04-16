from sys import argv

script, user_name, appname = argv
prompt3 = '> '

print "Hi %s, I'm the %s script. I will use the %s application." %(user_name, script, appname)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt3)

print "Where do you live %s?" % user_name
lives = raw_input(prompt3)

print "What kind of computer do you have?"
computer = raw_input(prompt3)

print """
Alright, so you said %r about liking me.
You live in %r.Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
