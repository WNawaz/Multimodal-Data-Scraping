# Multimodal-Data-Scraping
Text data scraping from multimodal data sources

# Web Scraping and Processing Tool

This tool provides functionalities for web scraping and processing different types of content. You can perform static web scraping, dynamic web scraping, YouTube ASR (Automatic Speech Recognition), and YouTube transcript extraction.

## Usage

### Install Dependencies

Ensure you have the required libraries installed. You can install them using `pip`:

```sh
pip install -r requirements.txt
```

### Running the Script

The `scraping.py` script uses command-line arguments to determine which function to execute. Use the `--action` argument to specify the type of operation you want to perform, and provide the necessary arguments for that operation.

#### Static Web Scraping

To perform static web scraping, use:

```sh
python scraping.py --action static --fname <filename> --base_url <base_url> --list_content <list_content>
```

#### Dynamic Web Scraping

To perform dynamic web scraping, use:

```sh
python scraping.py --action dynamic --prog_url <program_url> --episode <episode_number> --total_pages <total_pages> --outfile <output_file> [--driver_path <driver_path>]
```

#### YouTube ASR

To perform ASR on a YouTube channel, use:

```sh
python scraping.py --action asr --channel <channel_name> --out_path <output_path> --missed_reader <missed_reader_path>
```

#### YouTube Transcripts

To extract transcripts from YouTube, use:

```sh
python scraping.py --action transcripts --playlists <playlists> --channel_name <channel_name> --target_file <target_file> --missed_reader_transcripts <missed_reader_transcripts>
```

## Arguments

- `--action`: Specifies the action to perform. Choices are `static`, `dynamic`, `asr`, `transcripts`.
- `--fname`: Filename for static web scraping.
- `--base_url`: Base URL for static web scraping.
- `--list_content`: Content list for static web scraping.
- `--prog_url`: Program URL for dynamic web scraping.
- `--episode`: Episode number for dynamic web scraping.
- `--total_pages`: Total number of pages for dynamic web scraping.
- `--outfile`: Output file path for dynamic web scraping.
- `--driver_path`: Path to the ChromeDriver for dynamic web scraping (default: `/usr/lib/chromium-browser/chromedriver`).
- `--channel`: YouTube channel name for ASR.
- `--out_path`: Output path for ASR.
- `--missed_reader`: Path to missed reader for ASR.
- `--playlists`: Playlists for YouTube transcripts.
- `--channel_name`: YouTube channel name for transcripts.
- `--target_file`: Target file path for YouTube transcripts.
- `--missed_reader_transcripts`: Path to missed reader for transcripts.

## Notes

- Ensure that all required arguments for each action are provided.
- Adjust the `driver_path` if you are using a different path for ChromeDriver.

For further assistance, please  contact the maintainer.
```
