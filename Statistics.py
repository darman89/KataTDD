class Statistics:
    def values(self, string):
        if string == "":
            return []
        elif ',' in string:
            return [int(string[0]), int(string[2])]
        else:
            return [int(string)]
