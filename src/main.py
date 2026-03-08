import sys
from generate_pages_recursive import generate_pages_recursive
from copy_dir import copy_dir


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_dir("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)



if __name__ == "__main__":    main()