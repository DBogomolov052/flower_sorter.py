import cv2
import numpy as np

# Задаем пороги для цветов
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Читаем изображение
img = cv2.imread("flowers.jpg")

# Конвертируем в HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Ищем цвета
mask_red = cv2.inRange(hsv_img, lower_red, upper_red)
mask_green = cv2.inRange(hsv_img, lower_green, upper_green)
mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)
# Объединяем маски
mask = cv2.bitwise_or(mask_red, mask_green)
mask = cv2.bitwise_or(mask, mask_blue)

# Находим контуры
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Рисуем контуры на исходном изображении
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# Сохраняем результат
cv2.imwrite("flower_sorter_result.jpg", img)
