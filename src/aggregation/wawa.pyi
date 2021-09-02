__all__ = [
    'Wawa',
]
import crowdkit.aggregation.base_aggregator
import pandas.core.frame
import pandas.core.series
import typing


class Wawa(crowdkit.aggregation.base_aggregator.BaseAggregator):
    """Worker Agreement with Aggregate

    Calculates the considers the likelihood of coincidence of the performers opinion with the majority
    Based on this, for each task, calculates the sum of the agreement of each label
    The correct label is the one where the sum of the agreements is greater

    After predicting stored different data frames (details in BaseAggregator):
        tasks_labels: Predicted labels for each task
        probas: Probabilities for each label for task
        performers_skills: Predicted labels for each task
    Attributes:
        skills_ (typing.Optional[pandas.core.series.Series]): Performers' skills
            A pandas.Series index by performers and holding corresponding performer's skill
        probas_ (typing.Optional[pandas.core.frame.DataFrame]): Tasks' label probability distributions
            A pandas.DataFrame indexed by `task` such that `result.loc[task, label]`
            is the probability of `task`'s true label to be equal to `label`. Each
            probability is between 0 and 1, all task's probabilities should sum up to 1

        labels_ (typing.Optional[pandas.core.frame.DataFrame]): Tasks' most likely true labels
            A pandas.Series indexed by `task` such that `labels.loc[task]`
            is the tasks's most likely true label.
    """

    def fit(self, data: pandas.core.frame.DataFrame) -> 'Wawa':
        """Args:
            data (DataFrame): Performers' labeling results
                A pandas.DataFrame containing `task`, `performer` and `label` columns.
        Returns:
            Wawa: self
        """
        ...

    def predict(self, data: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
        """Args:
            data (DataFrame): Performers' labeling results
                A pandas.DataFrame containing `task`, `performer` and `label` columns.
        Returns:
            DataFrame: Tasks' most likely true labels
                A pandas.Series indexed by `task` such that `labels.loc[task]`
                is the tasks's most likely true label.
        """
        ...

    def predict_proba(self, data: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
        """Args:
            data (DataFrame): Performers' labeling results
                A pandas.DataFrame containing `task`, `performer` and `label` columns.
        Returns:
            DataFrame: Tasks' label probability distributions
                A pandas.DataFrame indexed by `task` such that `result.loc[task, label]`
                is the probability of `task`'s true label to be equal to `label`. Each
                probability is between 0 and 1, all task's probabilities should sum up to 1
        """
        ...

    def fit_predict(self, data: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
        """Args:
            data (DataFrame): Performers' labeling results
                A pandas.DataFrame containing `task`, `performer` and `label` columns.
        Returns:
            DataFrame: Tasks' most likely true labels
                A pandas.Series indexed by `task` such that `labels.loc[task]`
                is the tasks's most likely true label.
        """
        ...

    def fit_predict_proba(self, data: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
        """Args:
            data (DataFrame): Performers' labeling results
                A pandas.DataFrame containing `task`, `performer` and `label` columns.
        Returns:
            DataFrame: Tasks' label probability distributions
                A pandas.DataFrame indexed by `task` such that `result.loc[task, label]`
                is the probability of `task`'s true label to be equal to `label`. Each
                probability is between 0 and 1, all task's probabilities should sum up to 1
        """
        ...

    def __init__(self) -> None:
        """Method generated by attrs for class Wawa.
        """
        ...

    skills_: typing.Optional[pandas.core.series.Series]
    probas_: typing.Optional[pandas.core.frame.DataFrame]
    labels_: typing.Optional[pandas.core.frame.DataFrame]
