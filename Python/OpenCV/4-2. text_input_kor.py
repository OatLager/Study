# 텍스트 삽입 : 한글 우회 

## OpenCV에서 사용하는 글꼴 종류
# cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산 세리프(sans-serif) 글꼴
# cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산 세리프 글꼴
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
# cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 세리프 글꼴
# cv2.FONT_ITALIC : 기울임(이탤릭체), 다른 폰트와 함께 사용.

import cv2
import numpy as np
# PIL(Python Image Library)
from PIL import ImageFont, ImageDraw, Image

def myPutText(src,text,pos,font_size,font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc',font_size)
    draw.text(pos,text,font=font, fill=font_color)
    return np.array(img_pil)

img = np.zeros((480,640,3), dtype=np.uint8)

FONT_SIZE = 30 # 크기
COLOR = (255,255,255) # 색깔 (흰색)


# 그릴 위치, 텍스트 내용, 시작 위치, 크기, 색깔
img = myPutText(img, "한글한글", (20,50), FONT_SIZE, COLOR)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()