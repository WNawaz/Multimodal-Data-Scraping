import argparse
from static import static_web
from dynamic import dynamic_web_content
from asr import youtube_asr
from transcripts import youtube_transcripts

def main():
    parser = argparse.ArgumentParser(description="Web scraping and processing tool.")
    
    # Define available options
    parser.add_argument('--action', choices=['static', 'dynamic', 'asr', 'transcripts'], required=True,
                        help="The action to perform: 'static' for static web scraping, 'dynamic' for dynamic web scraping, 'asr' for YouTube ASR, 'transcripts' for YouTube transcripts.")
    
    # Arguments for static web scraping
    parser.add_argument('--fname', type=str, help="Filename for static web scraping.")
    parser.add_argument('--base_url', type=str, help="Base URL for static web scraping.")
    parser.add_argument('--list_content', type=str, help="Content list for static web scraping.")
    
    # Arguments for dynamic web scraping
    parser.add_argument('--prog_url', type=str, help="Program URL for dynamic web scraping.")
    parser.add_argument('--episode', type=int, help="Episode number for dynamic web scraping.")
    parser.add_argument('--total_pages', type=int, help="Total number of pages for dynamic web scraping.")
    parser.add_argument('--outfile', type=str, help="Output file path for dynamic web scraping.")
    parser.add_argument('--driver_path', type=str, default='/usr/lib/chromium-browser/chromedriver',
                        help="Path to the ChromeDriver for dynamic web scraping.")
    
    # Arguments for ASR
    parser.add_argument('--channel', type=str, help="YouTube channel name for ASR.")
    parser.add_argument('--out_path', type=str, help="Output path for ASR.")
    parser.add_argument('--missed_reader', type=str, help="Path to missed reader for ASR.")
    
    # Arguments for transcripts
    parser.add_argument('--playlists', type=str, help="Playlists for YouTube transcripts.")
    parser.add_argument('--channel_name', type=str, help="YouTube channel name for transcripts.")
    parser.add_argument('--target_file', type=str, help="Target file path for YouTube transcripts.")
    parser.add_argument('--missed_reader_transcripts', type=str, help="Path to missed reader for transcripts.")
    
    args = parser.parse_args()
    
    # Call functions based on the action
    if args.action == 'static':
        if all([args.fname, args.base_url, args.list_content]):
            static_web(args.fname, args.base_url, args.list_content)
        else:
            print("For static web scraping, --fname, --base_url, and --list_content are required.")
    
    elif args.action == 'dynamic':
        if all([args.prog_url, args.episode, args.total_pages, args.outfile]):
            dynamic_web_content(args.prog_url, args.episode, args.total_pages, args.outfile, args.driver_path)
        else:
            print("For dynamic web scraping, --prog_url, --episode, --total_pages, and --outfile are required.")
    
    elif args.action == 'asr':
        if all([args.channel, args.out_path, args.missed_reader]):
            youtube_asr(args.channel, args.out_path, args.missed_reader)
        else:
            print("For ASR, --channel, --out_path, and --missed_reader are required.")
    
    elif args.action == 'transcripts':
        if all([args.playlists, args.channel_name, args.target_file, args.missed_reader_transcripts]):
            youtube_transcripts(args.playlists, args.channel_name, args.target_file, args.missed_reader_transcripts)
        else:
            print("For transcripts, --playlists, --channel_name, --target_file, and --missed_reader_transcripts are required.")
    
if __name__ == "__main__":
    main()
