import numpy as np
import scipy.integrate as spln
import matplotlib.pyplot as plt

def system(y, t, a, b):
    y0, y1 = y;
    
    return [a*(y0-y0*y1), b*(-y1+y0*y1)];
    
if __name__ == "__main__":
  a = 1.0;
  b = 0.2;
  inity = [0.1, 1.0];
  t = np.linspace(0, 5, 100);
  sol = spln.odeint(system, inity, t, args=(a,b));
  
  #Plot the graph of y0 and y1 against t
  fig=plt.figure(1)
  plt.plot(t, sol[:,0], 'b', label='y0 against t');
  plt.plot(t, sol[:,1], 'r', label='y1 against t');
  plt.title('y against t graph(0.1)')
  plt.legend(loc='best');
  plt.xlabel('t');
  plt.ylabel('y');
  fig = plt.gcf();
  fig.set_size_inches(5,5);
  plt.grid();
  plt.show();
  
  #Plot the graph of y1 against y0
  fig=plt.figure(1)
  plt.plot(sol[:,0], sol[:,1], 'g', label='y1 against y0');
  plt.title('y1 against y0 graph(0.1)')
  plt.legend(loc='best');
  plt.xlabel('y0');
  plt.ylabel('y1');
  fig = plt.gcf();
  fig.set_size_inches(5,5);
  plt.grid();
  plt.show();
  
  #Sensitivity part
  a = 1.0;
  b = 0.2;
  inity = [0.11, 1.0];
  t = np.linspace(0, 5, 100);
  sol = spln.odeint(system, inity, t, args=(a,b));
  
  #New graph of y0 and y1 against t
  fig=plt.figure(1)
  plt.plot(t, sol[:,0], 'b', label='y0 against t');
  plt.plot(t, sol[:,1], 'r', label='y1 against t');
  plt.title('y against t graph(0.11)')
  plt.legend(loc='best');
  plt.xlabel('t');
  plt.ylabel('y');
  fig = plt.gcf();
  fig.set_size_inches(5,5);
  plt.grid();
  plt.show();
  
  #New graph of y1 against y0
  fig=plt.figure(1)
  plt.plot(sol[:,0], sol[:,1], 'g', label='y1 against y0');
  plt.title('y1 against  y0 graph(0.11)')
  plt.legend(loc='best');
  plt.xlabel('y0');
  plt.ylabel('y1');
  fig = plt.gcf();
  fig.set_size_inches(5,5);
  plt.grid();
  plt.show();
  
  
  





