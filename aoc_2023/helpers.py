class ContentLoader():
    def __init__(self, filename = "") -> None:
        self.filename = filename

    def load(self):
        if self.filename != "":
            content = []
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            for line in lines:
                line = line.strip()
                content.append(line)
        
            return content
        else:
            print("please set a valid filename.")
            return None
    
    def set_filename(self, filename):
        self.filename = filename
