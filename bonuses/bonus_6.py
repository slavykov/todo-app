contents = ["All carr"
            "ots", "The carr"
            "ots", "The slic"
            "ing"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)
