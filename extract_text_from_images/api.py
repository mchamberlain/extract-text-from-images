import cv2
import easyocr
from matplotlib import pyplot
from matplotlib import patches


def read_image(in_file_path):
    """ Open the image at ``file_path`` using OpenCV and return the image instance. """
    return cv2.imread(in_file_path)


def get_text_from_image(in_image, in_langlist=None):
    """ Read text from the image and return the results.
    Returns:
        results : list
            [bbox_tl, bbox_tr, bbox_br, bbox_bl, text, score]
    """
    langlist = in_langlist or ['en']
    reader = easyocr.Reader(langlist)
    return reader.readtext(in_image)


def filter_text_results(results, accuracy_limit=0.5):
    """ Generate results with greater than or equal to `accuracy_limit` accuracy. """
    for result in results:
        bounds, text, score = result
        if score < accuracy_limit:
            continue
        yield result


def plot_image_with_results(in_file_path, in_image, in_results):
    """ Plot the image along with the detected text and bounding boxes. """
    image_data = cv2.cvtColor(in_image, cv2.COLOR_BGR2RGB)
    fig, axes = pyplot.subplots()
    axes.imshow(image_data)
    if in_results:
        for bounds, text, score in in_results:
            width = bounds[2][0] - bounds[0][0]
            height = bounds[2][1] - bounds[0][1]
            axes.add_patch(patches.Rectangle(bounds[0], width, height, linewidth=1, edgecolor='r', facecolor='none'))
            axes.text(bounds[0][0], bounds[0][1], text, color='r')
    pyplot.show()
