import numpy as np
from PIL import Image

a = np.zeros((200, 200), dtype=np.uint8)
a += 128

a[50:150, 60:140] = 220

im = Image.fromarray(a)
im.save('gray.png')
