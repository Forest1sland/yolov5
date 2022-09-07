import cv2 as cv


def save_img(img, path, num):
    cv.imwrite(path + 'img_' + str(num) + '.jpg', img)


video_path = 'labelimg/videos/video3.mp4'
img_path = 'labelimg/images/'

i = 0
count = 1159
img_interval = 30

video = cv.VideoCapture(video_path)

while video.isOpened():
    i += 1
    ref, frame = video.read()
    if i % img_interval == 0:
        count += 1
        save_img(frame, img_path, count)
    c = cv.waitKey(1)
    if c == 27:
        break

video.release()
cv.destroyAllWindows()
