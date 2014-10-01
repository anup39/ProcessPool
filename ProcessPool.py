import multiprocessing
import Queue
import sys
import os
import wmi
import psutil
import time

queue = Queue.Queue()
list = []
pids = []

class ProcessPool(object):
	def __init__(self):
		super(ProcessPool, self).__init__()


	def dequeue_list(self,list, pids, scheduling_interval, wait_time):
		global queue
		self.pids = pids
		self.scheduling_interval = scheduling_interval
		self.wait_time = wait_time
		duration = 0
		while True:
			flag = 0
			process = multiprocessing.Process(target = None)
			for i in range(len(list)):
				if queue.qsize() == 0:
					return "All processes in this instance have ended!"
				else:
					if not list[i].is_alive():
						flag = 1
						process = queue.get()
						process.start()
						start_time = time.time()
						print "%s with process id %s has started" % (process.name, process.pid)
						print "Currently running python processes :" 
						print self.current_processes()
						print '\n'
				if flag == 1:
					list.pop(i)
					list.append(process)
					pids.append(process.pid)
				for i in list:
					if i.is_alive():
						if wait_time == 0:
							pass
						elif wait_time <= time.time() - start_time  :
							self.kill_process(i.pid)
						else:
							pass
			time.sleep(scheduling_interval)
			#duration = duration + scheduling_interval


	def start(self, process_list, size, scheduling_interval):
		global list
		global queue
		global pids
		self.process_list = process_list
		self.size = size
		self.scheduling_interval = scheduling_interval
		i = 0
		while i < size:
			wait_time = process_list[i][2]
			process = multiprocessing.Process(target = process_list[i][0], args = process_list[i][1])
			process.start()
			list.append(process)
			pids.append(process.pid)
			print "%s with process id %s has started" % (process.name, process.pid)
			print "Currently running python processes :" 
			print self.current_processes()
			print '\n'
			i  = i + 1
		while i < len(process_list):
			wait_time = process_list[i][2]
			queue.put(multiprocessing.Process(target = process_list[i][0], args = process_list[i][1]))
			i = i + 1
		self.dequeue_list(list, pids, scheduling_interval, wait_time)

	# Starts all the processes at once
	def start_all(self, process_list):
		global list
		self.process_list = process_list
		i = 0
		while i < len(process_list):
			process = multiprocessing.Process(target = process_list[i][0], args = process_list[i][1])
			process.start()
			list.append(process)
			pids.append(process.pid)
			print "%s with process id %s has started" % (process.name, process.pid)
			print "Currently running python processes :" 
			print self.current_processes()
			print '\n'
			i = i + 1
		return "All processes in this instance have ended."

	# Returns the set of currently running python processes
	def current_processes(self):
		c = wmi.WMI()
		for process in c.Win32_Process(name = "python.exe"):
			print process.ProcessId, process.Name
			#print self.process_exists(process.ProcessId)

	# Checks if the process exits using pid as input
	def process_exists(self, pid):
		self.pid = pid
		return psutil.pid_exists(pid)

	# Kills the process with pid as input
	def kill_process(self, pid):
		self.pid = pid
		process = psutil.Process(pid)
		process.terminate()

	# Returns the status of process with pid as input
	def status(self, pid):
		self.pid = pid
		process = psutil.Process(pid)
		process.status()

	#def start(self, process_list, size):
	#	global list
	#	global queue
	#	self.process_list = process_list
	#	self.size = size
	#	i = 0
	#	while i < size:
	#		process = multiprocessing.Process(target = process_list[i][0], args = process_list[i][1])
	#		process.start()
	#		self.listing(process)
	#		print "%s has started" % process
	#		i  = i + 1
	#	while i < len(process_list):
	#		queue.put(multiprocessing.Process(target = process_list[i][0], args = process_list[i][1]))
	#		i = i + 1
	#	print self.dequeue_list(list)