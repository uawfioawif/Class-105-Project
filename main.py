import os, cv2

path = 'images'
images = []

for file in os.listdir(path):
  name, ext = os.path.splitext(file)

  if ext in ['.jpg', '.png']:
    file_name = path+'/'+file
    print(file_name)
    images.append(file_name)

frame = cv2.imread(images[0])
h, w, c = frame.shape
size = (w, h)

output = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'XVID'), 5, size)
for i in range(len(images) - 1, 0, -1):
  frame = cv2.imread(images[i])
  output.write(frame)

output.release()
