# Extract text from images

This is just a small project where I tried out easyocr.

## Dependencies
This project uses [poetry](https://python-poetry.org) for dependency management. With poetry installed on your system, run the following command from the repo root to install the project's dependencies:

    $ poetry install

## Running
To search for text in an image and display a plot of the image and the discovered text, run:

    $ poetry run extract_text_from_images.cli --show images/nascar_small.jpg

To see the help/command line options:

    $ poetry run extract_text_from_images.cli --help

## References

1. https://youtu.be/9_SRXdO9EC4