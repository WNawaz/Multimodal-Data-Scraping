# Web Scraping and Processing Tool

This Python script provides a command-line tool for performing various web scraping and processing tasks. It supports static and dynamic web scraping, as well as extracting automated speech recognition (ASR) data and transcripts from YouTube.

## Features

- **Static Web Scraping**: Extract data from static web pages.
- **Dynamic Web Scraping**: Extract data from dynamically loaded web pages (requires a web driver).
- **YouTube ASR**: Extract automated speech recognition (ASR) data from YouTube videos.
- **YouTube Transcripts**: Extract transcripts from YouTube playlists.

**Install Dependencies**: Install any necessary Python libraries by running:
   ```
   pip install -r requirements.txt
   ```

### Usage

You can use this tool from the command line with various options depending on the action you want to perform. Here’s how to use each action:

#### 1. Static Web Scraping

To perform static web scraping:

```
python script.py --action static --outfile output_file.txt --base_url http://example.com --list_content content_list.txt
--outfile: Path to save the scraped data.
--base_url: The base URL of the website to scrape.
--list_content: A list of content to scrape.
```
#### 2. Dynamic Web Scraping
To perform dynamic web scraping:

```
python script.py --action dynamic --base_url http://example.com --episode 1 --total_pages 10 --outfile output_file.txt --driver_path /path/to/chromedriver
--base_url: The base URL of the website to scrape.
--episode: Episode name to scrape.
--total_pages: Total number of pages to scrape.
--outfile: Path to save the scraped data.
--driver_path: Path to the ChromeDriver.
```
#### 3. YouTube ASR
To extract ASR data from YouTube:
```
python script.py --action asr --channel my_channel --outfile output_file.txt --missed_reader path/to/missed_reader
--channel: YouTube channel name.
--outfile: Path to save the ASR data.
--missed_reader: Path to the missed reader file.
```

#### 4. YouTube Transcripts
To extract transcripts from YouTube playlists:

```
python script.py --action transcripts --playlists playlist1,playlist2 --channel my_channel --outfile output_file.txt --missed_reader path/to/missed_reader
--playlists: Comma-separated list of YouTube playlists.
--channel: YouTube channel name.
--outfile: Path to save the transcripts.
--missed_reader: Path to the missed reader file.
```
#### License
This project is licensed under the MIT License - see the LICENSE file for details.
