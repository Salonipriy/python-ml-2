#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().system('pip install dlib')


# In[29]:


get_ipython().system('pip install opencv-python')


# In[32]:


get_ipython().system('pip install opencv-python-headless')
get_ipython().system('pip install opencv-contrib-python')


# In[23]:


get_ipython().system(' pip install cmake')


# In[33]:


import cv2
import numpy as np 
import face_recognition


# In[18]:


path = 'file:///C:/Users/Saloni%20Priya/Pictures/img.jpeg'


# In[19]:


image = cv2.imread(path)


# In[20]:


window_name = 'Image'


# In[21]:


kernel = np.ones((5, 5), np.uint8) 


# In[22]:


#image = cv2.erode(image, kernel) 


# In[27]:


cv2.imshow(window_name, image)


# In[28]:


img = cv2.imread('img.jpeg')


# In[34]:


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[ ]:


edges = cv2.Canny(gray, 50, 150, apertureSize=3)


# In[ ]:


lines = cv2.HoughLines(edges, 1, np.pi/180, 200)


# In[ ]:


for r_theta in lines:
    arr = np.array(r_theta[0], dtype=np.float64)
    r, theta = arr
    # Stores the value of cos(theta) in a
    a = np.cos(theta)

    # Stores the value of sin(theta) in b
    b = np.sin(theta)

    # x0 stores the value rcos(theta)
    x0 = a*r

    # y0 stores the value rsin(theta)
    y0 = b*r


# In[ ]:


x1 = int(x0 + 1000*(-b))


# In[ ]:


y1 = int(y0 + 1000*(a))


# In[ ]:


x2 = int(x0 - 1000*(-b))


# In[ ]:


y2 = int(y0 - 1000*(a))


# In[ ]:


cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


# In[ ]:


cv2.imwrite('linesDetected.jpg', img)

