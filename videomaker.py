import ffmpeg 
import subprocess
from PIL import Image, ImageDraw, ImageFont

def convertToImage(User,Text,number):
	img = Image.new('RGB', (740, 460), color = (0, 177, 237))
	#fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
	d = ImageDraw.Draw(img)
	d.multiline_text((0,0), Text, fill=(255, 255, 255),align='left',spacing=15)
	name = 'tweetimages/tweet'+ str(number)+'.png'
	img.save(name)
	return



def convertToVideo():
	stream = ffmpeg.input(r'tweetimages/*.png', pattern_type='glob', framerate=1)
	stream = ffmpeg.output(stream,'tweetimages/movie.mp4')
	stream = ffmpeg.overwrite_output(stream)
	ffmpeg.run(stream)


if __name__ == '__main__':
	#convertToVideo()
	convertToImage("a", "Hellott, this is a very long text qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqaaaabbbbxccc",1)