
from pytube import Playlist
import csv
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
import re
import sqlite3

def get_video_urls_from_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    # Fetch all video URLs in the playlist
    video_urls = [video.watch_url for video in playlist.videos]
    return video_urls

def write_csv(target_file,write_data):#[channel_name,title,transcript,transcript_text,video_id]
    with open(target_file, 'a', newline='', encoding='utf-8') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow(write_data)
    return

def write_missed(target_file,write_data):#
    with open(target_file, 'a', newline='', encoding='utf-8') as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow(write_data)
    return


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
        transcript TEXT NOT NULL,
        transcript_text TEXT NOT NULL,
        video_id TEXT NOT NULL
      )
  ''')

  # Insert the data into the table
  cursor.execute('''
    INSERT INTO videos (channel_name, title, transcript, transcript_text, video_id)
    VALUES (?, ?, ?, ?, ?)
  ''', write_data)
  # Commit the transaction
  conn.commit()
  # Close the connection
  conn.close()
  return

def get_transcripts(target_file,video_urls,missed_reader):
 for video_id in video_urls[:]:
  try:
    response = requests.get(video_id,target_file)
    soup = BeautifulSoup(response.content,'html.parser',from_encoding='utf-8')#'lxml', 'html5lib' ,html.parser
    title = soup.title.string
    #title = re.sub(r'[^\w\s\d]', '', title)
    #title = soup.find('meta', property='og:title')['content']
    transcript = YouTubeTranscriptApi.get_transcript(video_id.split('v=')[1],languages=['ar'])
    transcript_text = " ".join([segment['text'] for segment in transcript]) #add back
    #print(title,'title ends',transcript_text)
    print('writing')
    #write_csv(target_file+'.csv',[channel_name,title,transcript,transcript_text,video_id]):#
    write_sql(target_file+'_transcripts.db',[channel_name,title,str(transcript),transcript_text,video_id])#videos.db' add back
    print('....wrote')
  except Exception as e:
    write_missed(missed_reader,[video_id])
    print(e)

def youtube_transcripts(playlists,channel_name,target_file,missed_reader):
 for playlist_url in playlists:
  video_urls = get_video_urls_from_playlist(playlist_url)
  print('fethced urls: ',len(video_urls))
  get_transcripts(target_file,video_urls)
