#C:/movie/movie/image.mp4 C:/movie/png (356, 369)
import cv2

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter('C:/movie/movieresult/video01.mp4', fourcc, 30.0, (640, 480))

for i in range(1, 210):
    img = cv2.imread('C:/movie/png/sample_video_img_{0:03d}.png'.format(i))
    img = cv2.resize(img, (640, 480))
    video.write(img)

video.release()