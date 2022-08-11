class QssTool:
    @staticmethod
    def readqssfile(file_path,obj):
        with open(file_path, 'r',True) as f:
            content=f.read()
            obj.setStyleSheet(content)