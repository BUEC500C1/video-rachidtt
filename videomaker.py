import ffmpeg 
import subprocess



def convertToVideo():
	stream = ffmpeg.input(r'tweetimages/*.png', pattern_type='glob', framerate=1)
	stream = ffmpeg.output(stream,'tweetimages/movie.mp4')
	stream = ffmpeg.overwrite_output(stream)
	ffmpeg.run(stream)


if __name__ == '__main__':
	convertToVideo()