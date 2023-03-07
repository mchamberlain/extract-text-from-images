import argparse
import sys

from . import api


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('images', nargs='+', help='An image to perform text recognition on.')
    parser.add_argument('--show', action='store_true', help='Show a plot of each image with the recognized text.')
    parser.add_argument('--min-score', type=float, default=0.5, help='The minimum score a detection must have to be included in the results. [0,1]')

    args = parser.parse_args(argv)

    for image_path in args.images:
        img_data = api.read_image(image_path)
        if not image_path:
            print('Empty image: f{image_path}')
            continue
        results = list(api.filter_text_results(api.get_text_from_image(img_data), args.min_score))
        print(results)
        if args.show:
            api.plot_image_with_results(image_path, img_data, results)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
