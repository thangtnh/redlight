class Video:
    def __init__(self, idVideo = None, name = None, path = None, user = None, detectDate = None):
        self.idVideo = idVideo
        self.name = name
        self.path = path
        self.detectDate = detectDate
        self.user = user
    
    def get_idVideo(self):
        return self.idVideo
    def set_idVideo(self, idVideo):
        self.idVideo = idVideo

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_path(self):
        return self.path
    def set_path(self, path):
        self.path = path

    def get_detectDate(self):
        return self.detectDate
    def set_detectDate(self, detectDate):
        self.detectDate = detectDate

    def get_user(self):
        return self.user
    def set_user(self, user):
        self.user = user       