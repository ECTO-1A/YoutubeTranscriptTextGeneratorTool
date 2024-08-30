from yt_transcript_string import generate_filtered_transcript
video_id = "1kLLEyFeZq8"
# Without specifying time
full_transcript = generate_filtered_transcript(video_id)
for line in full_transcript:
    print(line)