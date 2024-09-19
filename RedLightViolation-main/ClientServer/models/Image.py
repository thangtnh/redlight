class Image:
    def __init__(self, idImage = None, name = None, path = None, content = None, video = None):
        self.idImage = idImage
        self.name = name
        self.path = path
        self.content = content
        self.video = video

    def get_idImage(self):
        return self.idImage
    def set_idImage(self, idImage):
        self.idImage = idImage

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_path(self):
        return self.path
    def set_path(self, path):
        self.path = path

    def get_content(self):
        return self.content
    def set_content(self, content):
        self.content = content
    
    def get_video(self):
        return self.video
    def set_video(self, video):
        self.video = video