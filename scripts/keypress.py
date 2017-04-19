import rospy
from keyboard_commander.msg import ordreAmiral

class controller:
	def __init__(self):
		self.speedTab = [-80,-70,-60,-50,-40,-30,-25,0,16,18,20,22,24,26,28,30]
		self.vitesseMax = len(self.speedTab) - 1
		self.zeroSpeedIndex = 7
		self.angleStep = 10
		self.angleMax = 100
		
		self.zeroVitesse = 2
		
		self.vitesse = self.zeroSpeedIndex
		self.angle = 0
		
		 
		#print("__init__")
		
		self.msg = ordreAmiral()
		self.msg.boiteDeVitesse = self.zeroVitesse
		
		self.pub = rospy.Publisher('ordreDeLAmiral', ordreAmiral, queue_size=10)
		rospy.init_node('keypress')
		self.rate = rospy.Rate(10) # 10hz
		
		self.start()
		
	def getch(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			return sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old)
			
	def stop(self):
		self.vitesse = self.zeroSpeedIndex
		self.angle = 0
		self.msg.header.stamp = rospy.Time.now()
		self.msg.vitesse = self.speedTab[self.vitesse]
		self.msg.direction = self.angle
		self.pub.publish(self.msg)
		rospy.loginfo("order %d %d",self.speedTab[self.vitesse], self.angle)
		return False

	def key(self):
		#print("key")
		key = self.getch()
		#zprint(key)
		if(key in ['z','q','s','d','k','r']):
			deltaVitesse = 0
			deltaAngle = 0
				
			if(key == 'z'):
				#print('devant')
				deltaVitesse = 1
			elif(key == 's'):
				deltaVitesse = -1
				#print('derriere')
			elif(key == 'd'):
				deltaAngle = self.angleStep
				#print('droite')
			elif(key == 'q'):
				deltaAngle = -self.angleStep
				#print('gauche')
			self.vitesse = max(min(self.vitesse + deltaVitesse , self.vitesseMax) , 0)
			self.angle = max(min(self.angle + deltaAngle, self.angleMax), -self.angleMax)
			
			if(key == 'r'):
				self.vitesse = self.zeroSpeedIndex
				self.angle = 0
				
			if(key == 'k'):
				#print('stop')
				return self.stop()
				
			self.msg.header.stamp = rospy.Time.now()
			self.msg.vitesse = self.speedTab[self.vitesse]
			self.msg.direction = self.angle
			self.pub.publish(self.msg)
			rospy.loginfo("order %d %d",self.speedTab[self.vitesse], self.angle)
		else:
			print("not recognized")
		return True

	def talker(self):
		hello_str = "hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
			
			
	def start(self):
		#print("start")
		while(self.key() and not rospy.is_shutdown()):
			#print('new attempt')
			self.rate.sleep()

if __name__ == '__main__':
	#print("main")
	c = controller()

