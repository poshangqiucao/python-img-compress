import cv2
import os
import time

dir_path = r'./img/'
save_path = r'./compress-img/'
items = os.listdir(dir_path)
for item in items:
    path = os.path.join(dir_path, item)
    before_compress = os.path.getsize(path)
    img=cv2.imread(path,1)
    ext = item.split(".")[1]
    save_compress_path = os.path.join(save_path,item)
    if ext == 'jpg' or ext == 'jpeg':
        cv2.imwrite(save_compress_path,img,[cv2.IMWRITE_JPEG_QUALITY,40])
    if ext == 'png':
        cv2.imwrite(save_compress_path,img,[cv2.IMWRITE_PNG_COMPRESSION,7])
    after_compress = os.path.getsize(save_compress_path)
    compress_size = before_compress - after_compress
    compress_ratio = compress_size / before_compress * 100
    print(item+'-图片减小了{}字节,压缩率为{:.2f}%'.format(compress_size,compress_ratio))
    time.sleep(1)
    