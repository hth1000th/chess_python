class Queen:
  def rule_to_move(from_x, from_y, to_x, to_y):
    if (to_x - from_x) == (to_y - from_y):
      true
    elif (to_x - from_x) == (from_y - to_y):
      true
    elif from_x == to_x :
      true
    elif from_y == to_y :
      true
    else:
      false