from pytube import YouTube

while True:
    # Get user's choice
    print("Enter What you want to Download:")
    print("1. Video\n2. Audio\n3. Playlist\n4. Exit")
    input_choice = int(input("Enter your choice (1/2/3/4): "))

    # Handle user's choice using match statement
    match input_choice:
        case 1:
            # Download video
            link = input("Enter the YouTube video link: ")
            youtube_1 = YouTube(link)
            videos = youtube_1.streams

            # Title of the video
            print(f"Title: {youtube_1.title}")

            # Display available video streams
            vid = list(enumerate(videos))
            for i in vid:
                print(i)

            # User input for video stream selection
            strm = int(input("Enter the index of the video stream to download: "))
            # Validate user input
            if 0 <= strm < len(videos):
                # Download selected video stream
                videos[strm].download()
                print('Video Downloaded Successfully')
            else:
                print('Invalid input. Please enter a valid index.')

        case 2:
            # Download audio
            link = input("Enter the YouTube video link for audio: ")
            youtube_1 = YouTube(link)
            audio = youtube_1.streams.filter(only_audio=True)

            # Title of the video
            print(f"Title: {youtube_1.title}")

            # Display available audio streams
            aud = list(enumerate(audio))
            for i in aud:
                print(i)

            # User input for audio stream selection
            strm = int(input("Enter the index of the audio stream to download: "))
            # Validate user input
            if 0 <= strm < len(audio):
                # Download selected audio stream
                audio[strm].download()
                print('Audio Downloaded Successfully')
            else:
                print('Invalid input. Please enter a valid index.')

        case 3:
            # Download playlist
            link = input("Enter the YouTube playlist link: ")
            playlist = YouTube(link)

            # Title of the video
            print(f"Title: {playlist.title}")

            # Iterate through playlist videos and download each one
            for video in playlist.videos:
                video.streams.get_highest_resolution().download()

            print('Playlist Downloaded Successfully')

        case 4:
            # Exit the program
            print("Exiting program. Goodbye!")
            break

        case _:
            print("Invalid choice. Please enter a valid option (1, 2, 3, or 4).")
