from generate_pages_recursive import generate_pages_recursive
from copy_dir import copy_dir


def main():
    copy_dir("static", "public")
    generate_pages_recursive("content", "template.html", "public")



if __name__ == "__main__":    main()