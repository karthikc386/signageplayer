import os
import json
from utils.Common import check_file_extension

config_file_path = os.path.join('config', 'config.json')

with open(config_file_path, 'r') as file:
    config = json.load(file)


def categorize_files(content_folder):
    images = []
    texts = []
    videos = []

    for root, dirs, files in os.walk(content_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if check_file_extension(file, config["image_supported_formats"]):
                images.append(file_path)
            elif check_file_extension(file, config["text_supported_formats"]):
                with open(file_path, 'r') as text_file:
                    texts.extend(text_file.readlines())
            elif check_file_extension(file, config["video_supported_formats"]):
                videos.append(file_path)

    return images, texts, videos
