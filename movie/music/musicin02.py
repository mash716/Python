# coding: utf-8
import sys
import cv2
import moviepy.editor as mp

class Test:
    def __init__(self):
        # Set video names.
        self.input_video = 'C:/movie/input/cup.mp4'
        self.output_video = 'C:/movie/output/output01.mp4'


    def main(self):
        self.set_audio()


    def set_audio(self):
        # Extract audio from input video.
        clip_input = mp.VideoFileClip(self.input_video).subclip()
        clip_input.audio.write_audiofile('C:/movie/output/audio.mp3')

        # Add audio to output video.
        clip_output = mp.VideoFileClip(self.output_video).subclip()
        clip_output.write_videofile(self.output_video.replace('.avi', '.mp4'), audio='audio.mp3')


if __name__ == "__main__":
    Test().main()