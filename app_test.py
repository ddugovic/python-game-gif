import app


def test_board_to_png():
  assert app.create_splash(64, {}, '1') is None
