#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import datetime
import glob
import math
import os
import subprocess
import sys
sys.path.append('/Users/yuta/.pyenv/versions/lab/lib/python3.6/site-packages')
import tempfile

import cv2
import ffmpeg
import numpy as np
import pydub
from PIL import Image, ImageDraw, ImageFont
from pydub import AudioSegment
from pydub.utils import db_to_float, ratio_to_db

from lib import context_factory


def main(args):
    # コンテキストの作成
    c = context_factory.ContextFactory(args).create_context()

    # 作業フォルダ
    now = datetime.datetime.now()
    now_formatted = "{0:%Y%m%d%H%M%S}".format(now)
    work_dir = "work_" + now_formatted
    os.mkdir(work_dir)
    c['work_dir'] = work_dir

    # 全体の実行
    # print(str(c))

    # シーンごと
    # with open(c['work_dir'] + "/list.txt", mode="w") as f:
    width = 640
    height = 360
    sceneIndex = 0
    for scene in c['setting']['scenes']:
        # print(str(scene))
        # for imagefilter in scene['imagefilters']:
        #     print(str(imagefilter))


        # 指定されたファイルの拡張子で動画か静止画かを判断する
        extension = os.path.splitext(c['setting']['scenes'][sceneIndex]['src'])[1][1:]
        if(extension == 'png' or extension == 'jpeg'):
            # 静止画の場合は動画作成に必要なフレーム数を算出し、連番の静止画をコピー作成する
            fps = 30 # 現在固定設定
            starttime = c['setting']['scenes'][sceneIndex]['trimming']['starttime'] / 1000
            endtime = c['setting']['scenes'][sceneIndex]['trimming']['endtime'] / 1000
            startFrame = int(starttime * fps)
            endFrame = int(endtime * fps)
            frameCnt = endFrame - startFrame
            digit = len(str(frameCnt))
            img = Image.open('sample/' + c['setting']['scenes'][sceneIndex]['src'])
            num = frameCnt

            # トリミング指定された範囲分を連番の静止画として保存する
            for index in range(startFrame, endFrame):
                img.save((c['work_dir'] + "/" + str(sceneIndex) + "_frame_img_{0:0" + str(digit) + "d}.png").format(index))
        else:
            # 動画情報を取得する
            movie = cv2.VideoCapture('sample/' + c['setting']['scenes'][sceneIndex]['src'])
            fps = int(movie.get(cv2.CAP_PROP_FPS))
            frameCnt = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))

            # 動画をフレーム分割して連番の静止画として保存する
            digit = len(str(frameCnt))
            num = 0
            while True:
                ret, frame = movie.read()
                if ret:
                    cv2.imwrite("{}_{}.{}".format(work_dir + "/" + str(sceneIndex) + "_frame_img", str(num).zfill(digit), "png"), frame)
                    num += 1
                else:
                    num -= 1
                    break

            # 時間トリミング処理を行う
            if(c['setting']['scenes'][sceneIndex].get('trimming') and c['setting']['scenes'][sceneIndex]['trimming'].get('starttime')):
                # 時間トリミングする範囲を算する
                starttime = c['setting']['scenes'][sceneIndex]['trimming']['starttime'] / 1000
                endtime = c['setting']['scenes'][sceneIndex]['trimming']['endtime'] / 1000
                startFrame = int(starttime * fps)
                endFrame = int(endtime * fps)
                trimFrameCnt = endFrame - startFrame
                trimdigit = len(str(trimFrameCnt))
                trimnum = 0

                # トリミングした静止画を番号を振り直して別ファイル名にリネームして一時保存する
                for index in range(startFrame, endFrame):
                    regex = str(index).zfill(digit)
                    if(glob.glob(c['work_dir'] + '/' + str(sceneIndex) + '_frame_img_' + regex + '.png')):
                        filenamenum = str(trimnum).zfill(trimdigit)
                        os.rename(c['work_dir'] + '/' + str(sceneIndex) + '_frame_img_' + regex + '.png', c['work_dir'] + '/' + str(sceneIndex) + '_temp_frame_img_' + filenamenum + '.png')
                        trimnum += 1

                digit = trimdigit
                # 時間トリミング対象外のファイルは削除する
                dellist = glob.glob(c['work_dir'] + '/' + str(sceneIndex) + '_frame_img_*.png')
                for file in dellist:
                    os.remove(file)

                # 一時保存しておいたファイルを再リネームする
                filelist = glob.glob(c['work_dir'] + '/' + str(sceneIndex) + '_temp_frame_img_*.png')
                trimnum = 0
                for file in filelist:
                    filenamenum = str(trimnum).zfill(trimdigit)
                    os.rename(c['work_dir'] + '/' + str(sceneIndex) + '_temp_frame_img_' + filenamenum + '.png', c['work_dir'] + '/' + str(sceneIndex) + '_frame_img_' + filenamenum + '.png')
                    trimnum += 1

                num = trimnum - 1

        ## 映像トリミングを行う
        if(c['setting']['scenes'][sceneIndex].get('trimming') and c['setting']['scenes'][sceneIndex]['trimming'].get('tl')):
            # トリミングする位置を取得する
            trim_tlx = c['setting']['scenes'][sceneIndex]['trimming']['tl']['x']
            trim_tly = c['setting']['scenes'][sceneIndex]['trimming']['tl']['y']
            trim_brx = c['setting']['scenes'][sceneIndex]['trimming']['br']['x']
            trim_bry = c['setting']['scenes'][sceneIndex]['trimming']['br']['y']

            files = glob.glob(c['work_dir'] + '/' + str(sceneIndex) + '_*.png')
            for file in files:
                img = Image.open(file)
                # トリミングして上書き保存する
                img.crop((trim_tlx, trim_tly, trim_brx, trim_bry)).save(file)
                img = cv2.imread(file)
                img = cv2.resize(img, (width, height))
                cv2.imwrite(file, img)





        ## 各フィルタ処理を行う
        imagefilters = c['setting']['scenes'][sceneIndex]['imagefilters']
        imagefiltersCnt = len(imagefilters)

        for i in range(0, imagefiltersCnt):
            eventsCnt = len(c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'])
            for j in range(0, eventsCnt):
                filter = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['filter']

                # フレーム分割した静止画に字幕を入れる
                if(filter == 'caption'):
                    inputText = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['text']
                    starttime = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['starttime'] / 1000
                    endtime = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['endtime'] / 1000
                    startFrame = int(starttime * fps)
                    endFrame = int(endtime * fps)
                    position = (30, height / 2) # 現在固定設定
                    for k in range(startFrame, endFrame):
                        img = Image.open((c['work_dir'] + "/" + str(sceneIndex) + "_frame_img_{0:0" + str(digit) + "d}.png").format(k))
                        fontPath = "ipag00303/ipag.ttf"
                        font = ImageFont.truetype(fontPath, 20) # 現在固定設定
                        draw = ImageDraw.Draw(img)
                        fontColor = (255, 255, 255) # 現在固定設定
                        draw.text(position, inputText, fontColor, font=font)
                        img.save((c['work_dir'] + "/" + str(sceneIndex) + "_frame_img_{0:0" + str(digit) + "d}.png").format(k))

                #★修正　枠を追加する
                if(filter == 'frame'):
                    #jsonの情報
                    overImgPath = 'sample/' + c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['src']
                    #固定値
                    imgSize = (640, 360)
                    imgPosition= (0, 0)
                    overImg = cv2.imread(overImgPath, cv2.IMREAD_UNCHANGED)
                    overImg = cv2.resize(overImg, imgSize)
                    cv_rgb_ol_image = cv2.cvtColor(overImg, cv2.COLOR_BGRA2RGBA)
                    pil_rgb_ol_image = Image.fromarray(cv_rgb_ol_image)
                    pil_rgba_ol_image = pil_rgb_ol_image.convert("RGBA")

                    starttime = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['starttime'] / 1000
                    endtime = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['endtime'] / 1000
                    startFrame = int(starttime * fps)
                    endFrame = int(endtime * fps)

                    # 画像を挿入する範囲だけ、1枚ずつ背景画像を読み込んで画像を追加し、上書き保存する
                    for i in range(startFrame, endFrame):
                        # 背景画像を読み込み、PIL形式に変換する
                        bgImg = cv2.imread(wkDirPath + imgPath.format(i))
                        cv_rgb_bg_image = cv2.cvtColor(bgImg, cv2.COLOR_BGR2RGB)
                        pil_rgb_bg_image = Image.fromarray(cv_rgb_bg_image )
                        pil_rgba_bg_image = pil_rgb_bg_image.convert("RGBA")

                        pil_rgba_bg_temp = Image.new('RGBA', pil_rgba_bg_image.size, (255, 255, 255, 0))
                        pil_rgba_bg_temp.paste(pil_rgba_ol_image, imgPosition, pil_rgba_ol_image)
                        result_image = Image.alpha_composite(pil_rgba_bg_image, pil_rgba_bg_temp)
                        cv_bgr_result_image = cv2.cvtColor(np.asarray(result_image), cv2.COLOR_RGBA2BGRA)
                        cv2.imwrite(wkDirPath + imgPath.format(i), cv_bgr_result_image)
                    

                # フレーム分割した静止画に画像を挿入する
                if(filter == 'overlay'):
                    # 画像を挿入する位置を取得する
                    position_tlx = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['position']['tl']['x']
                    position_tly = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['position']['tl']['y']
                    position_brx = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['position']['br']['x']
                    position_bry = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['position']['br']['y']
                    position = (position_tlx, position_tly)

                    # 画像を挿入する座標から挿入後の画像サイズを算出する
                    size = (position_brx - position_tlx, position_bry - position_tly)
                    overImg = cv2.imread('sample/' + c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['src'], cv2.IMREAD_UNCHANGED)
                    overImg = cv2.resize(overImg, size)

                    # OpenCV形式からPillow形式に変換する
                    cv_rgb_ol_image = cv2.cvtColor(overImg, cv2.COLOR_BGRA2RGBA)
                    pil_rgb_ol_image = Image.fromarray(cv_rgb_ol_image)
                    pil_rgba_ol_image = pil_rgb_ol_image.convert("RGBA")

                    starttime = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['starttime'] / 1000
                    endtime = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['endtime'] / 1000
                    startFrame = int(starttime * fps)
                    endFrame = int(endtime * fps)

                    # 画像を挿入する範囲だけ、1枚ずつ背景画像を読み込んで画像を追加し、上書き保存する
                    for l in range(startFrame, endFrame):
                        # 背景画像を読み込み、PIL形式に変換する
                        bgImg = cv2.imread((c['work_dir'] + "/" + str(sceneIndex) + "_frame_img_{0:0" + str(digit) + "d}.png").format(l))
                        cv_rgb_bg_image = cv2.cvtColor(bgImg, cv2.COLOR_BGR2RGB)
                        pil_rgb_bg_image = Image.fromarray(cv_rgb_bg_image )
                        pil_rgba_bg_image = pil_rgb_bg_image.convert("RGBA")

                        # 合成用の背景画像を新規作成する
                        pil_rgba_bg_temp = Image.new("RGBA", pil_rgba_bg_image.size, (255, 255, 255, 0))
                        # 背景画像に挿入画像を貼り付ける
                        pil_rgba_bg_temp.paste(pil_rgba_ol_image, position, pil_rgba_ol_image)
                        result_image = Image.alpha_composite(pil_rgba_bg_image, pil_rgba_bg_temp)
                        # Pillow形式からOpenCV形式へ変換する
                        cv_bgr_result_image = cv2.cvtColor(np.asarray(result_image), cv2.COLOR_RGBA2BGRA)

                        cv2.imwrite((c['work_dir'] + "/" + str(sceneIndex) + "_frame_img_{0:0" + str(digit) + "d}.png").format(l), cv_bgr_result_image)

        # フレーム分割した連番の静止画を連結させて動画(音声なし)として作成する
        fourcc = cv2.VideoWriter_fourcc("M","P","4","V")
        video = cv2.VideoWriter(work_dir + "/" + str(sceneIndex) + "_tempMovie.mp4", fourcc, fps, (width, height))

        for i in range(0, num):
            img = cv2.imread((work_dir + "/" + str(sceneIndex) + "_frame_img_{0:0" + str(digit) + "d}.png").format(i))
            img = cv2.resize(img, (width, height))
            video.write(img)

        video.release()



        # ズーム処理を行う
        for i in range(0, imagefiltersCnt):
            eventsCnt = len(c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'])
            for j in range(0, eventsCnt):
                filter = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['filter']
                if(filter == 'zoom'):
                    zoomstart = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['starttime'] // 1000
                    zoomend = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['endtime'] // 1000
                    startFrame = zoomstart * fps
                    endFrame = zoomend * fps
                    duration = zoomend - zoomstart
                    tlx = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['tl']['x']
                    tly = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['tl']['y']
                    brx = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['br']['x']
                    bry = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['br']['y']
                    # ズームする範囲を算出する
                    trimWidth = brx - tlx
                    trimHeight = bry - tly
                    # ズームする最終的な画像の幅と高さを算出する
                    lastWidth = 640
                    lastHeight = 360
                    # 1フレームごとのズーム倍率を計算する(小数第2位まで算出)
                    zoomRate_w = round((lastWidth - trimWidth) // duration / fps, 2)
                    zoomRate_h = round((lastHeight - trimHeight) // duration / fps, 2)

                    # ズーム対象のフレーム数だけ処理する
                    zoomIndex = 0
                    for fileNum in range(startFrame, endFrame):
                        # ズームするサイズ幅を計算する
                        zoomIndex += 1
                        zoomSizeWidth = round(zoomRate_w * zoomIndex)
                        zoomSizeHeight = round(zoomRate_h * zoomIndex)
                        # 画像ファイルを読み込む
                        img = Image.open((c['work_dir'] + "/" + str(sceneIndex) + "_frame_img_{0:0" + str(digit) + "d}.png").format(fileNum))
                        img_width, img_height = img.size

                        # ズームする範囲のトリミング処理を行い、ズーム用にリサイズする
                        cropImg = img.crop((tlx, tly, brx, bry))
                        resizedImg = cropImg.resize((trimWidth + zoomSizeWidth, trimHeight + zoomSizeHeight))
                        # リサイズした画像をさらに動画用の大きさにトリミングする
                        img_width, img_height = resizedImg.size
                        temp_img = resizedImg.crop(((img_width - lastWidth) // 2, 
                                                   (img_height - lastHeight) // 2, 
                                                    (img_width + lastWidth) // 2, 
                                                    (img_height + lastHeight) // 2))
                        # トリミングした画像を上書き保存する
                        temp_img.save((c['work_dir'] + "/" + str(sceneIndex) + "_frame_img_{0:0" + str(digit) + "d}.png").format(fileNum))


        # フレーム分割した連番の静止画を連結させて動画(音声なし)として作成する
        fourcc = cv2.VideoWriter_fourcc("M","P","4","V")
        video = cv2.VideoWriter(work_dir + "/" + str(sceneIndex) + "_tempMovie.mp4", fourcc, fps, (width, height))

        for i in range(0, num):
            img = cv2.imread((work_dir + "/" + str(sceneIndex) + "_frame_img_{0:0" + str(digit) + "d}.png").format(i))
            img = cv2.resize(img, (width, height))
            video.write(img)

        video.release()

        # フェード処理を行う
        for i in range(0, imagefiltersCnt):
            eventsCnt = len(c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'])
            for j in range(0, eventsCnt):
                filter = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['filter']
                if(filter == 'fade'):
                    # フェードイン処理の命令をストリームに指定する
                    starttime = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['starttime'] // 1000
                    stream = ffmpeg.input(c['work_dir'] + "/" + str(sceneIndex) + "_tempMovie.mp4")
                    stream = stream.filter('fade', type='in', start_time=0, duration=starttime)

                    # フェードアウト処理の命令をストリームに指定する
                    endtime = c['setting']['scenes'][sceneIndex]['imagefilters'][i]['events'][j]['endtime'] // 1000
                    video_info = ffmpeg.probe(c['work_dir'] + "/" + str(sceneIndex) + "_tempMovie.mp4")
                    movieLength = float(video_info['streams'][0]['duration'])
                    duration = movieLength - endtime
                    stream = stream.filter('fade', type='out', start_time=endtime, duration=duration)

                    # フェード処理を実行したものを別ファイルとして保存する
                    stream = ffmpeg.output(stream, c['work_dir'] + '/' + str(sceneIndex) + '_tempMovie_fade.mp4')
                    ffmpeg.run(stream)

                    # フェード処理後のファイルを元のファイル名にリネームする
                    if(os.path.exists(c['work_dir'] + '/' + str(sceneIndex) + '_tempMovie.mp4')):
                        os.remove(c['work_dir'] + '/' + str(sceneIndex) + '_tempMovie.mp4')
                    os.rename(c['work_dir'] + '/' + str(sceneIndex) + '_tempMovie_fade.mp4', c['work_dir'] + '/' + str(sceneIndex) + '_tempMovie.mp4')


        # 音声作成処理を行う
        if(c['setting']['scenes'][sceneIndex].get('audiofilters')):
            audiofilters = c['setting']['scenes'][sceneIndex]['audiofilters']
            audiofiltersCnt = len(audiofilters)

            for i in range(0, audiofiltersCnt):
                eventsCnt = len(c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'])
                seFlg = False # 個別音声付与判定フラグ(True:個別音声付与あり/False:個別音声付与なし)
                # 個別音声を付与する
                for j in range(0, eventsCnt):
                    filter = c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'][j]['filter']

                    if(filter == 'soundeffect'):
                        # 個別音声ファイルを指定された再生時間分の長さのリピート音声ファイルとして作成する
                        starttime = c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'][j]['starttime']
                        endtime = c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'][j]['endtime']
                        during = (endtime -starttime) // 1000
                        cmd = "ffmpeg -stream_loop -1 -i sample/" \
                            + c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'][j]['src'] + " -t " + str(during) \
                            + " -c copy -fflags +genpts " + c['work_dir'] + "/se.mp4"
                        resp = subprocess.run(cmd, shell=True)

                        extension = os.path.splitext(c['setting']['audio_track'])[1][1:]
                        base_audio = AudioSegment.from_file("sample/" + c['setting']['audio_track'], format=extension)
                        effect_sound = AudioSegment.from_file(c['work_dir'] + "/se.mp4", format="mp4")
                        # 個別音声のボリューム調整を行う
                        volume = c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'][j]['volume']
                        delta = ratio_to_db(volume)
                        effect_sound = effect_sound + delta
                        result_audio = base_audio.overlay(effect_sound, starttime)
                        result_audio.export(c['work_dir'] + "/audio_se.mp4", format="mp4")
                        seFlg = True

                # 全体音声のボリューム調整処理を行う
                for j in range(0, eventsCnt):
                    filter = c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'][j]['filter']
                    if(filter == 'volume'):
                        starttime = c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'][j]['starttime']
                        endtime = c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'][j]['endtime']
                        volume = c['setting']['scenes'][sceneIndex]['audiofilters'][i]['events'][j]['volume']
                        delta = ratio_to_db(volume)

                        # 個別音声が付与済の場合はすでに作成済みの音声ファイルを使用する
                        if(seFlg):
                            base_audio = AudioSegment.from_file(c['work_dir'] + "/audio_se.mp4", format="mp4")
                        else:
                            extension = os.path.splitext(c['setting']['audio_track'])[1][1:]
                            base_audio = AudioSegment.from_file("sample/" + c['setting']['audio_track'], format=extension)

                        # 音声ファイルを分割し、対象箇所をボリューム調整後、音声ファイルを結合する
                        length = base_audio.duration_seconds * 1000
                        cut1 = base_audio[0:starttime]
                        cut2 = base_audio[starttime:endtime]
                        cut2 = cut2 + delta
                        cut3 = base_audio[endtime:length]

                        out = cut1 + cut2 + cut3
                        out.export(c['work_dir'] + "/temp_audio.mp4", format="mp4")

        sceneIndex += 1

    ## シーンごとに編集した動画を連結する
    fourcc = cv2.VideoWriter_fourcc("M","P","4","V")
    out = cv2.VideoWriter(c['work_dir'] + "/temp_movie.mp4", int(fourcc), fps, (width, height))

    for i in range(0, sceneIndex):
        movie = cv2.VideoCapture(c['work_dir'] + "/" + str(i) + "_tempMovie.mp4")
        # 最初の1フレームを読み込む
        if movie.isOpened() == True:
            ret,frame = movie.read()
        else:
            ret = False
            movie.close()
            # フレームの読み込みに成功している間フレームを書き出し続ける
        while ret:
            # 読み込んだフレームを書き込み
            out.write(frame)
            # 次のフレームを読み込み
            ret,frame = movie.read()

    out.release()

    ## 連結した動画に音声を付与する
    cmd = "ffmpeg -y -i " + c['work_dir'] + "/temp_movie.mp4 -i " + c['work_dir'] + "/temp_audio.mp4" \
        + " -async 1 -filter_complex amix=inputs=1:duration=first:dropout_transition=2 -vcodec libx264 " + c['setting']['output_file']
    resp = subprocess.run(cmd, shell=True)













if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(
        usage = '%(prog)s [options]',
        description = "Trireal movie composer.",
        add_help = True,
    )
    parser.add_argument(\
        '-f', '--file', required=True,\
        help="setting file path. (ex. sample.json)",\
        type=argparse.FileType('r', encoding='UTF-8'))

    args = parser.parse_args()

    print('#### tririal movie composer start')
    main(args)
    print('#### tririal movie composer successfully.')

    exit(0)
