#C:/movie/movie/image.mp4 C:/movie/png
import cv2
import os
#パス有無判定
print(os.path.exists("C://movie//movie//image.mp4"))

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

save_all_frames('C:/movie/movie/cup.mp4', 'C:/movie/jpg', 'image')
save_all_frames('C:/movie/movie/cup.mp4', 'C:/movie/png', 'sample_video_img', 'png')
