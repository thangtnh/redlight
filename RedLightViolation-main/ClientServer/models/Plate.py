class Plate:
    def __init__(self, idPlate = None, content = None, image = None):
        self.idPlate = idPlate
        self.content = content
        self.image = image

    def get_idPlate(self):
        return self.idPlate
    def set_idPlate(self, idPlate):
        self.idPlate = idPlate

    def get_content(self):
        return self.content
    def set_content(self, content):
        self.content = content

    def get_image(self):
        return self.image
    def set_image(self, image):
        self.image = image