class CharDetectModel:
    def __init__(self, idModel = None, name = None, createDate = None, path = None, \
                 accuracy = None, precision = None, recall = None, f1score = None, isActive = None,\
                    quantitySample = None, idDataset = None):
        self.idModel = idModel
        self.name = name
        self.createDate = createDate
        self.path = path
        self.accuracy = accuracy
        self.precision = precision
        self.recall = recall
        self.f1score = f1score
        self.isActive = isActive
        self.quantitySample = quantitySample
        self.idDataset = idDataset

    def get_idModel(self):
        return self.idModel
    def set_idModel(self, idModel):
        self.idModel = idModel

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_createDate(self):
        return self.createDate
    def set_createDate(self, createDate):
        self.createDate = createDate

    def get_path(self):
        return self.path
    def set_path(self, path):
        self.path = path

    def get_accuracy(self):
        return self.accuracy
    def set_accuracy(self, accuracy):
        self.accuracy = accuracy

    def get_precision(self):
        return self.precision
    def set_precision(self, precision):
        self.precision = precision

    def get_recall(self):
        return self.recall
    def set_recall(self, recall):
        self.recall = recall

    def get_f1score(self):
        return self.f1score
    def set_f1score(self, f1score):
        self.f1score = f1score

    def get_isActive(self):
        return self.isActive
    def set_isActive(self, isActive):
        self.isActive = isActive

    def get_quantitySample(self):
        return self.quantitySample
    def set_quantitySample(self, quantitySample):
        self.quantitySample = quantitySample

    def get_idDataset(self):
        return self.idDataset
    def set_idDataset(self, idDataset):
        self.idDataset = idDataset