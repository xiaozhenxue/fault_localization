from metric import Metric


class Program:

    def __init__(self, test_cases, faulty_stmt, total_stmt):
        self.test_cases = test_cases
        self.faulty_stmt = faulty_stmt
        self.total_stmt = total_stmt

    def localize_fault(self, score):
        maxm = 0
        for f in self.faulty_stmt:
            maxm = max(maxm, score[f - 1])
        top = 0
        for i in xrange(0, len(score)):
            if score[i] >= maxm and i not in self.faulty_stmt:
                top += 1
        return float(top)/self.total_stmt

    def compute_suspicious_score(self):
        scores = []
        for i in xrange(1, self.total_stmt + 1):
            cp, cf, np, nf = self.compute_statistics(i)
            metric = Metric(cp, cf, np, nf)
            scores.append(metric.odds_ratio())
        return scores

    def compute_statistics(self, stmt):
        cp = 0
        cf = 0
        np = 0
        nf = 0
        for tc in self.test_cases:
            if stmt in tc.cover and tc.status:
                cp += 1
            elif stmt in tc.cover and not tc.status:
                cf += 1
            elif stmt not in tc.cover and tc.status:
                np += 1
            elif stmt not in tc.cover and not tc.status:
                nf += 1
        return cp, cf, np, nf
