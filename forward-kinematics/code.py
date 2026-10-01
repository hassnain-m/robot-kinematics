import numpy as np

class Robot:
    def __init__(self, q1, q2, l1, l2):
        self.q1 = q1
        self.q2 = q2
        self.l1 = l1
        self.l2 = l2

    def get_joints(self): #return the coordinates of joints a and b
        a = [np.cos(self.q1)*self.l1, np.sin(self.q1)*self.l1]
        b = [a[0]+np.cos(self.q1 + self.q2) * self.l2, a[1]+np.sin(self.q1 + self.q2) * self.l2]
        return a,b

    def change_q1(self, new_q1):
        self.q1 = new_q1

    def change_q2(self, new_q2):
        self.q2 = new_q2