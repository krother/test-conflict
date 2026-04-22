import numpy as np
from PIL import Image

a = np.zeros((200, 200, 3), dtype=np.uint8)
a += 128
# lets add some green squares
a[50:100, 50:100] = (0, 255, 0)
a[100:150, 100:150] = (0, 255, 0)

a[50:150, 60:140] = 220

im = Image.fromarray(a)
im.save('gray.png')
