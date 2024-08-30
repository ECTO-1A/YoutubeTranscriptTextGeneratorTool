from yt_transcript_string import generate_filtered_transcript


video_id = "1kLLEyFeZq8"
start_time = 0 * 60  # 0 minutes in seconds
end_time = 2 * 60  # 17 minutes in seconds

transcript = generate_filtered_transcript(video_id, start_time, end_time)
for line in transcript:
    print(line)