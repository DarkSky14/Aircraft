class ImportControl:
    def __init__(self, module):
        self.module = module

    def set_import(self, module):
        self.module = module

    def get_import(self):
        return self.module

absolute_import = ImportControl("None")