# This work is related to our following funded project.

**Funded Project Title** 
A Trusted and Accessibility-Supported Islamic Knowledge Delivery Platform for Non-Arabic Speakers

**Research Team**
1.	Dr. Waqas Nawaz (Islamic University of Madinah) - PI
2.	Dr. Qaiser Abbas (Islamic University of Madinah) - CO-PI
3.	Dr. Abdallah Namoun (Islamic University of Madinah) - CO-PI
4.	Dr. Fazal Noor (Islamic University of Madinah) - CO-PI
5.	Dr. Toqeer Ali (Islamic University of Madinah) - CO-PI
6.	Dr. Fahad Alsisi (Islamic University of Madinah) - CO-PI
7.	Dr. Kifayat Ullah Khan (FAST-NU Islamabad, Pakistan | Birmingham City University, UK) - Consultant
8.	Mr. Rayan (MS Data science student at Islamic University of Madinah) – Student
9.	Mr. Zakariya (BS student at Islamic University of Madinah) - Student

**Acknowledgment Statement**
The authors extend their sincere gratitude to all those who contributed to this study, notably the Islamic University of Madinah, the National University of Computer and Emerging Sciences (FAST-NU), and Birmingham City University. The Deanship of Scientific Research at the Islamic University of Madinah, KSA, generously provided financial support for this research under the research groups (first) project no. 956.


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
python scraping.py --action static --outfile output_file --base_url https://binbaz.org.sa/ --list_content fatwas --total_pages 1
--outfile: Path to save the scraped data.
--base_url: The base URL of the website to scrape.
--list_content: content to scrape.
```
#### 2. Dynamic Web Scraping
To perform dynamic web scraping:

```
python scraping.py --action dynamic --base_url http://example.com --episode 1 --total_pages 10 --outfile output_file.txt --driver_path /path/to/chromedriver
--base_url: The base URL of the website to scrape.
--episode: Episode name to scrape.
--total_pages: Total number of pages to scrape.
--outfile: Path to save the scraped data.
--driver_path: Path to the ChromeDriver.
```
#### 3. YouTube ASR
To extract ASR data from YouTube:
```
python scraping.py --action asr --channel my_channel --outfile output_file.txt --missed_reader path/to/missed_reader
--channel: YouTube channel name.
--outfile: Path to save the ASR data.
--missed_reader: Path to the missed reader file.
```

#### 4. YouTube Transcripts
To extract transcripts from YouTube playlists:

```
#python scraping.py --action transcripts --playlists https://www.youtube.com/playlist?list=PLgaTRTylCbZDP43U58PFXNflz-8zzUwvJ --channel twjdm --outfile out_file --missed_reader missed_vids
--playlists: Comma-separated list of YouTube playlists.
--channel: YouTube channel name.
--outfile: Path to save the transcripts.
--missed_reader: Path to the missed reader file.
```
#### License
This project is licensed under the MIT License - see the LICENSE file for details.
