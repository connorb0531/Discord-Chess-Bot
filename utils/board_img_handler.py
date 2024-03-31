import os
from wand.image import Image
from wand.color import Color
import chess.svg


def convert_svg_to_png(board, output_file_name):
    svg_content = chess.svg.board(board)
    # Project root directory (assuming this script is in the 'utils' directory)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Full path to the output file within the resources/boards directory
    output_path = os.path.join(project_root, "resources", "boards", output_file_name)

    # Convert the SVG string to bytes
    svg_bytes = svg_content.encode('utf-8')

    # Save the image to the project root directory
    with Image(blob=svg_bytes, format='svg', background=Color('white')) as image:
        image.format = 'png'
        image.save(filename=output_path)


# Deletes png file of board associated with user and their board type
def delete_png(user_id, board_type):
    file_name = 'resources/boards/' + str(user_id) + board_type + '.png'
    if os.path.exists(file_name):
        os.remove(file_name)
