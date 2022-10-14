from typing import Set
import irisclassifier
import pytest


@pytest.fixture(scope="class")
def test_evaluation(self):
    i = irisclassifier.IrisClassifier
    i.ingestion()
    i.segregation()
    i.train()
    res = i.evaluation()
    assert res > 0.56
