import cv2

#fadeout fadein
file_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/Café_22728.mp4"#編集したい動画のパス
save_path = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample.mp4"#fadeout
save_path1 = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample1.mp4"#fadeout
save_path2 = "C:/Users/masho/Desktop/work/python/Python/lib/movie/sample2.mp4"#fadeout
resultpath = "C:/Users/masho/Desktop/work/python/Python/lib/movie/result.mp4"#fadeout


#動画の連結無音
outputPath11 = save_path
outputPath12 = save_path1
outputPath13 = save_path2
outputPathresult = resultpath

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
movie = cv2.VideoCapture(outputPath11)    
fps    = movie.get(cv2.CAP_PROP_FPS)
height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
width  = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
print(fps, int(width), int(height))

out = cv2.VideoWriter(outputPathresult, int(fourcc), fps, (int(width), int(height)))

for i in range(1,4):
    if i==1:
        movie = cv2.VideoCapture(outputPath11)
        print(movie)
        print(i)
    elif i==2:
        movie = cv2.VideoCapture(outputPath12)
        print(movie)
        print(i)  
    elif i==3:
        movie = cv2.VideoCapture(outputPath13)
        print(movie)
        print(i)  

    # 最初の1フレームを読み込む
    print(movie.isOpened())
    if movie.isOpened() == True:
        ret,frame = movie.read()
        # フレームの読み込みに成功している間フレームを書き出し続ける
        while ret == True:
            cv2.putText(frame, '', (400,400), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)

            # 読み込んだフレームを書き込み
            out.write(frame)
            # 次のフレームを読み込み
            ret,frame = movie.read()
