#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from yolo import YOLO
from PIL import Image
yolo = YOLO()

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = yolo.detect_image(image)
        r_image_name = '%s'%(img)
        r_image_name = r_image_name.replace(".jpg","_new")
        r_image_name = r_image_name.replace("img/","")
        r_image.save('newimages/%s.jpg'%(r_image_name))
