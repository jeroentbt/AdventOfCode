from toboggan_trajectory import move


def test_report_tree_after_single_horizontal_move():
    slope = (3, 0)
    landscape = "...#"
    assert "tree" == move(landscape, slope)
