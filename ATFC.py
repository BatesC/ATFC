# Need to find a way to remove text when restarting the game after a fail state so multiple paragraphs don't pile up. Might already have it need to test in dropbox / wherever ill be linking it
# Luxury feature: Add a user prompt to the death scene asking if they would like to try again, rather than simply exiting
# Understand print Death.quips[randint(0, len(self.quips)-1)] and why it didn't work
# Add a "play again" feature after death
# Edit the text to better imply the time period

from sys import exit
from random import randint
import time
import os

clear = lambda: os.system('cls')

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		current_scene.enter()
		
class Death(Scene): # Whole death sequence is boned

	quips = "You have failed."
	#[]

	#def Skip1(self):
		#time.sleep(3)
		#print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
	
	def enter(self):
		#print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
		clear()
		print Death.quips
		raw_input()
		clear()
		exit(1)
	
class Introduction(Scene):
	
	def enter(self):
		clear()
		print "\n   Your people know you as Ung, the untested. Chosen as a child"
		print "by the village elder, you were groomed for most of your life to"
		print "be Chief of the Valley (valleytribe.png). A role promised to the boy"
		print "with the sanest mind and most courageous demeanour. Fortunately,"
		print "or unfortunately, for you though the previous Chief contracted the Rot"
		print "and unceremoniously passed when you were at the tender age of 16. Since"
		print "that day your people have known you to be their leader, following your"
		print "direction both dutifully and dubiously; remaining weary of your ability"
		print "to lead under real pressure.\n"
		
		play = raw_input("Do you have what it takes?: ")
				
		if play == "y" or play == "yes":
			clear()
			print "\n   Two full moons and three suns have passed since your rise, your"
			print "people will begin preparations for the seasonal harvest tomorrow. With"
			print "nothing left to address, you find your way to your hut and lay down."
			raw_input()
			clear()
			
			print "\n   Day one"
			raw_input()
			clear()
			
			print "\n   The morning is darkened with clouds and threatens to storm."
			print "You are stood on a dais with the son of one of the shepherds,"
			print "discussing the merit of a potential hunt in the distant woods."
			print "The plan would involve using the leather from recently butchered"
			print "cattle to hurl stones at elusive game. The conversation goes"
			print "on for several minutes until you hear a shout from the herdsman"
			print "overseer, Jykm, from the group of huts to the East."
			raw_input()
			clear()
			
			print '\n   "Ung!", he roared, "A woman has arrived from the Thicketmen'
			print 'tribe and is frantically begging for help!"'
			raw_input()
			print '1) Our most reliable trade partners are the Thicketmen. I shall come to'
			print '   her aid hastily and learn the problem there.\n'
			print '2) You'"'"'re keeping her with the herd at the crest of the ramp I assume?'
			print '   Leave her there for now, we have more important matters to look after.\n'
			print '3) Have her brought down here, we may need the elder'"'"'s wisdom and medicines.\n'
			
			PlayThrough = raw_input("What do you tell Jykm?: ")
			
			if PlayThrough == "1":
				# Neutral
				clear()
				return 'neutral_play'
				
			elif PlayThrough == "2":
				# Bad
				clear()
				return 'bad_play'
				
			elif PlayThrough == "3":
				# Good
				clear()
				return 'good_play'
			
			else:
				clear()
				print "\nThat isn't an option."
				time.sleep(.5)
				print '\nPress enter to restart the section.'
				raw_input()
				return 'Introduction'
			
		elif play == "n" or play == "no":
			return 'death'
			exit(1)
			
		else:
			clear()
			print "\nThat isn't an option."
			time.sleep(.5)
			print '\nPress enter to try again.'
			raw_input()
			return 'Introduction'
			# The 'return_classname' is really useful for resetting certain areas
		
class GoodPlay(Scene):

	def enter(self):
		print ""
		
		"""code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses <10:
			print "BZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
		
		if guess == code:"""
			
class NeutralPlay(Scene):

	def enter(self):
		print "You burst onto the Bridge with the neutron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship. Each of them has an even uglier"
		print "clown costume than the last. They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door. Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'
			
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons start to sweat."
			print "You inch backward to the door and open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'BadPlay'
		else:
			print "DOES NOT COMPUTE!"
			return "neutral_play"
		
class BadPlay(Scene):

	def enter(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes. It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference. You get to the chamber with the escape pods, and "
		print "now need to pick one to take. Some of them could be damaged"
		print "but you don't have time to look. There's 5 pods, which one"
		print "do you take?"
		
		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print "You jump pod %s and hit the eject button."
			print "The pod escapes out into the void of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below. As it flies to the planet, you look"
			print "back and see your ship imploade then explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time. You won!"
			
			return 'finished'
			
class Finished(Scene):

	def enter(self):
		print "You won! Good job."
		return 'finished'
		
class Map(object):

	scenes = {
		'Introduction': Introduction(),
		'good_play': GoodPlay(),
		'neutral_play': NeutralPlay(),
		'bad_play': BadPlay(),
		'death': Death(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
a_map = Map('Introduction')
a_game = Engine(a_map)
a_game.play()
