# FFMPEG


## Part 1
For Part 1, I studied the following:
Python processes and subprocesses
Python Threads
Python Threads Versus Processes

Then ran tested the code provided in (Python Threads Versus Processes) and  compared processes and threads, details are in the readme of /Part1


## Part 2

In part 2, I have made the daily video summarizing tool. By entering a twitter handle, the program will use Tweepy to fetch the n most recent tweets(currently 100, can be changed in twittervideo.py, variable 'num'), and seperate them by day, it will then create a video of each day, with frames being the tweets converted from text to image.
The FFMPEG video making is done by multithreading, using a pool of 4 threads (because I have 4 cores, can aslo be adjusted). These 4 workerThreads each open a folder contain the tweets of an entire day and convert them to a video, then open another one until all jobs are done


### Requirements
-tweepy
-ffmpeg-python
-Pillow


### Instructions 

Clone the repo:
```
git clone https://github.com/BUEC500C1/video-rachidtt.git
```


Install requirements:
```
pip3 install -r requirements.txt
```

Install ffmpeg
```
sudo apt update
sudo apt-get install ffmpeg
```

In the main directory, Create file 'keys', and enter your keys in this format:

```
[auth]
consumer_key = ****
consumer_secret = ****
access_token = ****
access_secret = ****
```


Run twittervideo and enter the handle:

```
python3 twittervideo.py
```

The folder tweetimages will have folders named handle_day_mon_dd, and inside those folders will be the tweet activity that day in png images

The folder videos will have have the .mp4 video filed, named handle_day_mon_dd. Your media player might have some trouble with framerates this low (3sec per image) so the first few seconds might be blank and the last few tweets may go faster, experiment with cache settings to try fixing that.


Task 1: 
Estimate the processing power need to execute such operations on your computer
Estimate the maximum number of such operations that can run on your system
Task 2:
Design a module that can queue and process videos and notify the caller when the videos are ready
Implement the module
Include tracking interface to show how many processes are going on and success of each


Extra:  Using the twitter feed, construct a daily video summarizing a twitter handle day
Convert text into an image in a frame
Do a sequence of all texts and images in chronological order.
Display each video frame for 3 seconds
