import numpy as np

class Car:
    _g = 9.8
    
    def __init__(self, x0, params):
        self._x_1 = x0[0] # position (along the road)
        self._x_2 = x0[1] # velocity
        self._m, self._alpha, self._beta, self._gamma = params
        
    def step(self, dt, u, theta):
        self._theta = theta
        self._x_1 = self._x_1 + dt*self._x_2
        self._x_2 = self._x_2 + dt*(-self._alpha/self._m*abs(self._x_2)*self._x_2 - self._beta/self._m*self._x_2 + self._gamma/self._m*u - Car._g*np.sin(theta))
        
    def measure(self):
        x = self._x_1
        v = self._x_2
        return (x, v)  
    
    def sensor_i(self):
        # Rotation matrix to get back to the inertial frame..
        R = np.array(((np.cos(self._theta), -np.sin(self._theta)), (np.sin(self._theta), np.cos(self._theta))))
        x_i, y_i = R.dot(np.array([[self._x_1],[0]]))
        v = self._x_2
        return (x_i, y_i, v)
    
    
    
class LinearCar:
    _g = 9.8
    
    def __init__(self, x0, params):
        self._x_1 = x0[0] # position (along the road)
        self._x_2 = x0[1] # velocity
        self._m, self._alpha, self._beta, self._gamma = params
        
    def step(self, dt, u, theta):
        self._theta = theta
        A = np.array([[0, 1], [0, -self._beta/self._m]])
        B = np.array([[0, 0], [self._gamma, -LinearCar._g]])
        
        x = np.array([[self._x_1],[self._x_2]])
        U = np.array([[u],[theta]])
        self._x_1 = (self._x_1 + dt*(A[0,np.newaxis,:].dot(x) + B[0,np.newaxis,:].dot(U))).item()
        self._x_2 = (self._x_2 + dt*(A[1,np.newaxis,:].dot(x) + B[1,np.newaxis,:].dot(U))).item()
        
    def measure(self):
        x = self._x_1
        v = self._x_2
        return (x, v)
    
    def sensor_i(self):
        # Rotation matrix to get back to the inertial frame..
        R = np.array(((np.cos(self._theta), -np.sin(self._theta)), (np.sin(self._theta), np.cos(self._theta))))
        x_i, y_i = R.dot(np.array([[self._x_1],[0]]))
        v = self._x_2
        return (x_i, y_i, v)
    
        