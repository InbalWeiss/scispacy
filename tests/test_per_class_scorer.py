

import unittest

from SciSpaCy.per_class_scorer import PerClassScorer

class TestPerClassScorer(unittest.TestCase):

    def test_per_class_scorer_counts_correctly(self):

        scorer = PerClassScorer()

        predicted = [(1, 3, "PER"), (5, 7, "ORG")]
        gold = [(1, 3, "PER"), (10, 12, "ORG")]

        scorer(predicted, gold)

        correct_metrics = {'precision-PER': 1.0,
                           'recall-PER': 1.0,
                           'f1-measure-PER': 1.0,
                           'precision-ORG': 0.0,
                           'recall-ORG': 0.0,
                           'f1-measure-ORG': 0.0,
                           'precision-overall': 0.5,
                           'recall-overall': 0.5,
                           'f1-measure-overall': 0.5}
        metrics = scorer.get_metric()

        assert set(metrics.keys()) == set(correct_metrics.keys())
        for metric, value in metrics.items():
            self.assertAlmostEqual(value, correct_metrics[metric])

        scorer.get_metric(reset=True)

        # Check reseting.
        assert scorer._true_positives == {} # pylint: disable=protected-access
        assert scorer._false_positives == {} # pylint: disable=protected-access
        assert scorer._false_negatives == {} # pylint: disable=protected-access
