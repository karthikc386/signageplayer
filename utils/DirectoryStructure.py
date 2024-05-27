import os

def categorize_files(content_folder):
    images = []
    texts = []
    videos = []

    for root, dirs, files in os.walk(content_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(('.png', '.jpg', '.jpeg')):
                images.append(file_path)
            elif file.endswith('.txt'):
                with open(file_path, 'r') as text_file:
                    texts.extend(text_file.readlines())
            elif file.endswith('.mp4'):
                videos.append(file_path)

    return images, texts, videos
