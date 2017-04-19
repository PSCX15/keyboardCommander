import rospy
from std_msgs.msg import String
import Tkinter as tk

class controller:
    
    def __init(self):
        self.speedTab = [-50,-40,-30,-20,0,20,22,24,26]
        self.zeroIndex = 4
        self.angleStep = 5
        
        
        
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root, width=100, height=100)
        self.frame.bind("<Key>", self.key)
        self.frame.pack()
        
        self.start()
        
    def reset(self):
        self.speed = self.zeroIndex
        self.angle = 0

    def key(self, event):
        print("pressed", repr(event.char))
        key = event.char
        if(key == 'z'):
            print('devant')
        elif(key == 's'):
            print('derriere')
        elif(key == 'd'):
            print('droite')
        elif(key == 'q'):
            print('gauche')
        else:
            print("not recognized")

    def talker(self, ):
        pub = rospy.Publisher('servo_command', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()
            
    def start(self):
        self.root.mainloop()
        

if __name__ == '__main__':
    print("launched")
    c = controller()
