from __future__ import division
from math import radians, cos, sin, pi, sqrt, ceil
import threading
import time
import thread_template
import Queue
import socket
import cPickle

class v_data(thread_template.ThreadTemplate):
	""" The visual data object is used to proccess visual data recieved from a
		camera or a streem. At the moment this doesnt do much, but the idea is
		to eventually get it to recognise objects around it and decide how to
		react to them.
	"""

	def __init__(self, s_queues, s_connects, s_conds, s_locks, s_sema):
		""" Standard initialisation creating a seperate thread. Note that we
			use two queues here. One to handle the thread commands, and one to
			handle our sensory data.
		"""
		thread_template.ThreadTemplate.__init__(self, s_queues, s_connects, s_conds, s_locks, s_sema)
		self.s_queues.create('v_data')

	def run(self):
		""" We run our system in a loop to catch socket connections from the
			client program, and to handle our internal events generated by the
			system itself.
		"""
		self.setName('v_data')
		self.display('%s:\t\t\t\tStarting thread' % self.getName(), level=10)

		# Loop in the thread and wait for items in the queue
		while 1:
			self.parse_queue()

		# All done. Close the thread
		self.display('%s:\t\t\t\tClosing thread' % self.getName(), level=10)