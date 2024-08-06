#**youtube ASR starts**

import csv
import os
from pytube import YouTube
from moviepy.editor import AudioFileClip
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment
import speech_recognition as sr
import wave
import requests
from bs4 import BeautifulSoup
import sqlite3

#Download YouTube video
def download_youtube_video(url):
    yt = YouTube(url)
    video = yt.streams.filter().first()#only_audio=True
    video.download(output_path='/', filename='audio.mp4')
    return

#Extract audio from video
def extract_audio(video_path, audio_path):
  video_clip = VideoFileClip(video_path)
  # Extract audio from the video clip
  audio_clip = video_clip.audio
  # Write the extracted audio to a new file
  audio_clip.write_audiofile(audio_path)
  video_clip.close()
  audio_clip.close()


def extract_segment(input_file, output_file, start_time, end_time):
    audio = AudioSegment.from_wav(input_file)
    segment = audio[start_time * 1000:end_time * 1000]  # Convert seconds to milliseconds
    segment.export(output_file, format="wav")

def convert_speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio, language='ar-SA')#language='ps-af')#
        return text

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def write_sql(target_file,write_data):#'videos.db'
  # Connect to the database (or create it if it doesn't exist)
  conn = sqlite3.connect(target_file)
  # Create a cursor object
  cursor = conn.cursor()
  # Create the videos table with specified columns
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_name TEXT NOT NULL,
        title TEXT NOT NULL,
        transcript_text TEXT NOT NULL,
        video_id TEXT NOT NULL
      )
  ''')

  # Insert the data into the table
  cursor.execute('''
    INSERT INTO videos (channel_name, title, transcript_text, video_id)
    VALUES (?, ?, ?, ?)
  ''', write_data)
  # Commit the transaction
  conn.commit()
  # Close the connection
  conn.close()
  return

def segmented_asr(f,segment_duration,start_time):
  while start_time < total_duration:  # audio_duration should be calculated based on audio file
    end_time = start_time + segment_duration

    # Extract segment from the original audio file
    segment_file = "segment.wav"  # replace with actual segment filename
    extract_segment('/audio.wav', segment_file, start_time, end_time)

    # Process the segment
    txt = convert_speech_to_text(segment_file)
    #print(f"Segment {start_time}-{end_time}: {txt}")
    try:
     f.write(txt+'\n')
    except TypeError:
     print('conversion complete')
     break
    # Move to the next segment
    start_time = end_time
  return

def youtube_asr(channel,out_path,missed_reader):
 with open(missed_reader, 'r') as csvfile:
  file_names = list(csv.reader(csvfile))
 print('read files: ',len(file_names))
 for i in range(480,len(file_names)):
  url=file_names[i][0]
  print('reading file number: ',str(i))
  try:
   download_youtube_video(url)
   extract_audio('audio.mp4', "audio.wav")
   with wave.open('/audio.wav', 'rb') as wav_file:
    total_duration=wav_file.getnframes() / float(wav_file.getframerate())
   print('file length in seconds: ',total_duration)
   print('recognizing text...')
   start_time,segment_duration = 0,180 # x seconds
   f=open('txtfile2.txt','w')
   segmented_asr(f,segment_duration,start_time)
   f.close()
   with open('txtfile2.txt', 'r') as file:
    content = file.read().replace('\n', ' ')
   print('asr complete_string length: ',len(content))
   response = requests.get(url)
   soup = BeautifulSoup(response.content,'html.parser',from_encoding='utf-8')#'lxml', 'html5lib' ,html.parser
   title = soup.title.string
   write_sql(out_path+channel+'_asr.db',[channel,title,content,url])
  except Exception as e:
    print('couldnt fetch video')
    print(e)
