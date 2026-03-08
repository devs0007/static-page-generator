
import os

from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    for entry in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(content_path) and content_path.endswith(".md"):
            dest_path = dest_path[:-3] + ".html"
            generate_page(content_path, template_path, dest_path, basepath)
        elif os.path.isdir(content_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            generate_pages_recursive(content_path, template_path, dest_path, basepath)