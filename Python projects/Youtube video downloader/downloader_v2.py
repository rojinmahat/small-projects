import subprocess
import sys

# Ask for video URL
url = input("Enter the URL of the YouTube video:\n").strip()

# Ask for resolution
res = input('Select resolution (e.g. 720, 480, 360, 240, 144):\n').strip()

# Build format string (e.g., best[height=720])
format_str = f'bestvideo[height={res}]+140'

#select the output format
output_format = "mp4"

# Download command using yt-dlp
command = [
    'yt-dlp',
    '-f', format_str,
    url,
    "--merge-output-format",output_format
]

try:
    print("Downloading...")
    subprocess.run(command, check=True)
    print("\nDownload completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"\nDownload failed: {e}")
