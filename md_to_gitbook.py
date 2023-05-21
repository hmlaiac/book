import os

def convert_dir2title(dir):
    return dir.replace("_", " ").title()

if __name__ == "__main__":
    current_directory = os.getcwd()
    stack=[[current_directory, 0]] #
    indent = "  "
    book_list = "# Summary\n\n"
    while stack:
        data = stack.pop()
        current_directory = data[0]
        title_name = os.path.basename(current_directory)
        for name in os.listdir(current_directory):
            file = current_directory + "\\" + name
            if name == "README.md":
                template = "{indent}* [{title}]({href})"
                template = template.format(indent=indent*data[1], title=title_name, href=file)
                book_list = book_list + template + "\n"

            if os.path.isdir(file) and title_name != "docs":
                stack.append([file, data[1]+1])

    print(book_list)

    with open("SUMMARY.md", "w") as f:
        # Write text to the file
        f.write(book_list)


