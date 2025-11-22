class ModelSelector:
    def __init__(self, candidates, names):
        self.candidates = candidates
        self.names = names

    def select(self, metric_scores, higher_is_better=True):
        if len(metric_scores) != len(self.candidates):
            raise ValueError("metric_scores와 candidates 길이가 다릅니다")

        best_idx = metric_scores.index(
            max(metric_scores) if higher_is_better else min(metric_scores)
        )
        return self.candidates[best_idx], self.names[best_idx], metric_scores[best_idx]