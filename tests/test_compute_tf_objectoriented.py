"""Test cases for the object-oriented implementation"""
import pytest
from termfrequency import compute_tf_objectoriented


@pytest.mark.parametrize(
    "expected_output",
    [
        (
            [
                "white",
                "tigers",
                "live",
                "mostly",
                "in",
                "india",
                "wild",
                "lions",
                "live",
                "mostly",
                "in",
                "africa",
            ]
        )
    ],
)
def test_read_file_populates_data_0(expected_output):
    """ Checks that the reading of the small text file works """
    storage_manager = compute_tf_objectoriented.DataStorageManager("inputs/input.txt")
    word_list = storage_manager.words()
    assert word_list == expected_output


def test_stop_words():
    """Checks that the stop_words method removes stop words"""
    stop_manager = compute_tf_objectoriented.StopWordManager()
    word = "car"
    stop_list = stop_manager.is_stop_word(word)
    assert stop_list is False


def test_word_frequency():
    """Checks that the frequency method works correctly"""
    frequency_manager = compute_tf_objectoriented.WordFrequencyManager()
    frequency_manager.increment_count("mostly")
    frequency_manager.increment_count("wild")
    frequency_manager.increment_count("mostly")
    frequency_manager.increment_count("white")
    frequency_list = []
    frequency_list = frequency_manager.sorted()
    expected_list = [("mostly", 2), ("wild", 1), ("white", 1)]
    assert frequency_list == expected_list


def test_frequency_controller():
    """tests that frequency controller works correctly"""
    frequency_controller = compute_tf_objectoriented.WordFrequencyController(
        "inputs/input.txt"
    )
    program_output = frequency_controller.run()
    expected = [
        ("live", 2),
        ("mostly", 2),
        ("white", 1),
        ("tigers", 1),
        ("india", 1),
        ("wild", 1),
        ("lions", 1),
        ("africa", 1),
    ]
    assert program_output == expected


def test_word_frequency_info():
    """tests that the info function of word_frequency works correctly"""
    info_frequency = compute_tf_objectoriented.WordFrequencyController(
        "inputs/input.txt"
    )
    info_output = info_frequency.info()
    wordspace = "WordFrequencyController"
    assert wordspace == info_output


def test_stop_words_info():
    """tests that the info function of stop words works correctly"""
    info_stop = compute_tf_objectoriented.StopWordManager()
    info_outputS = info_stop.info()
    wordspace = "StopWordManager: My major data structure is a list"
    assert wordspace == info_outputS
