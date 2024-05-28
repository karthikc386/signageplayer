# Offline Digital Signage Player

## Overview

This offline digital signage player allows you to display images, videos, and text files by copying them into the designated content folder. The player supports specific formats for images and videos, ensuring smooth playback and display.

## Supported Formats

### Images
- .png
- .jpg
- .jpeg

### Videos
- .mp4

## Setup and Usage

1. **Copy Content**:
   - Place your image, video, or text files into the `content` folder.

2. **Run the Player**:
   - Ensure all dependencies are installed (see below for installation instructions).
   - Execute the main script to start the signage player.

## Installation

To install the necessary packages, you can use pip:

```sh
pip install numpy==1.26.4
pip install opencv-python==4.9.0.80
pip install pygame==2.5.2
```

## Dependencies

The following packages are required for the digital signage player to function correctly:

- **numpy==1.26.4**: A fundamental package for scientific computing with Python.
- **opencv-python==4.9.0.80**: OpenCV (Open Source Computer Vision Library) for image and video processing.
- **pygame==2.5.2**: A set of Python modules designed for writing video games, used here for display purposes.

## Notes

- Ensure that the files you want to display are in the supported formats listed above.
- The content folder must contain the files you wish to display before running the player.

## Contact

For further assistance, please contact Karthik Chakravarthi at [karthikc386@gmail.com].

---

By following these instructions, you can easily set up and run your offline digital signage player. Enjoy seamless playback of your content!
