import csv
from youtube_transcript_api import YouTubeTranscriptApi

# Function to generate a filtered transcript for a YouTube video and save it to a CSV file
# You need to pass in the following parameters:
# video_id: The YouTube video ID example: "1kLLEyFeZq8"
# start_time: The start time in seconds for the transcript range you want to filter example: 0 * 60
# end_time: The end time in seconds for the transcript range you want to filter example: 17 * 60

# The function will save the filtered transcript to a CSV file with the following format:
def generate_filtered_transcript(video_id, start_time, end_time):
    # Fetch transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # Filter transcript between the desired time range
    filtered_transcript = [
        entry for entry in transcript if start_time <= entry['start'] <= end_time
    ]

    # Save the filtered transcript to a CSV file
    csv_filename = f"yt_transcript_{video_id}.csv"

    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Start Time (s)", "Text"])

        for entry in filtered_transcript:
            writer.writerow([entry['start'], entry['text']])

    print(f"Filtered transcript saved to {csv_filename}")

# Example usage
# video_id = "1kLLEyFeZq8"
# start_time = 0 * 60  # 0 minutes in seconds
# end_time = 17 * 60  # 17 minutes in seconds

# generate_filtered_transcript(video_id, start_time, end_time)
