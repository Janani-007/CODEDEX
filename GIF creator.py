import imageio.v3 as iio
filenames =['gp1.png','gp2.png','gp3.png','gp4.png','gp5.png','gp6.png','gp7.png','gp8.png','gp9.png','gp10.png']
images =[ ]
for i in filenames:
  images.append(iio.imread(i))
iio.imwrite('haikyuu.gif',images,duration =500,loop=0)
