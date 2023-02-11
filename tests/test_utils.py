
from utils import getting_json_from_web, finding_ides

test_link = "https://www.jsonkeeper.com/b/MBOG"
main_link = "https://www.jsonkeeper.com/b/FGAS"


def test_getting_json_from_web():
    pass


def test_for_finding_ides():
    assert finding_ides(main_link, 10, False) == [317987878, 634356296, 260972664, 147815167, 893507143, 893507143,
                                                  286706711, 988276204, 361044570, 921286598]
    assert finding_ides(main_link, 2, True) == [863064926, 114832369]
    assert finding_ides(main_link, 1, False) == [317987878]
    assert finding_ides(main_link) == [863064926, 114832369, 154927927, 482520625, 801684332]