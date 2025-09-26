class Ranker:
    def __init__(self):
        self.vendor_scores = {}

    def rank(self, scores):
        self.vendor_scores = scores
        ranked_vendors = sorted(self.vendor_scores.items(), key=lambda item: item[1], reverse=True)
        ranked_results = {vendor: rank + 1 for rank, (vendor, _) in enumerate(ranked_vendors)}
        return ranked_results