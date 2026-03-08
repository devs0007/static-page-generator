
from markdown_html import markdown_to_html_node
from inline_markdown import extract_title

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    title = extract_title(markdown)

    html = template.replace("{{ Content }}", html_node.to_html())
    html = html.replace("{{ Title }}", title)
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    with open(dest_path, "w") as f:
        f.write(html)
