

class Cluster(object):

    def __init__(self):
        self.point = None
        self.cases = None
        self.close_in_space = None
        self.close_in_time = None
        self.close_space_and_time = None

    def get_case_count(self):
        if self.cases is not None:
            return len(self.cases)
