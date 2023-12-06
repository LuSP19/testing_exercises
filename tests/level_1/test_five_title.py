from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item('title', 5) == 'title'
    assert change_copy_item('title') == 'Copy of title'
    assert change_copy_item('Copy of title') == 'Copy of title (2)'
    assert change_copy_item('Copy of title (2)') == 'Copy of title (3)'
