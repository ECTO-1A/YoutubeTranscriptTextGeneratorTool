from youtube_transcript_api import YouTubeTranscriptApi

# Function to generate a filtered transcript for a YouTube video and return it as a list of strings
# You need to pass in the following parameters:
# video_id: The YouTube video ID example: "1kLLEyFeZq8" (REQUIRED)
# start_time: The start time in seconds for the transcript range you want to filter example: 0 * 60
# end_time: The end time in seconds for the transcript range you want to filter example: 17 * 60

# The function will save the filtered transcript to a CSV file with the following format:
def generate_filtered_transcript(video_id, start_time=None, end_time=None):
    # Fetch transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # If start_time and end_time are not specified, return the entire transcript
    if start_time is None and end_time is None:
        filtered_transcript = transcript
    else:
        # Filter transcript between the desired time range
        filtered_transcript = [
            entry for entry in transcript if start_time <= entry['start'] <= end_time
        ]

    # Format the filtered transcript as a list of strings or as a single string
    formatted_transcript = [
        f"{entry['start']}: {entry['text']}" for entry in filtered_transcript
    ]

    # Return the formatted transcript as a list of strings
    return formatted_transcript

    # Return the formatted transcript as a single string
    # return "\n".join(formatted_transcript)
