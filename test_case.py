from utility import covert_to_number


class TestCase:

    def __init__(self, trace, status):
        self.trace = trace
        self.status = status
        self.cover = set()
        for e in self.trace.split(','):
            stmt = covert_to_number(e)
            if stmt >= 0:
                self.cover.add(stmt)



