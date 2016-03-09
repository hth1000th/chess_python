class Knight:
  def rule_to_move(from_x, from_y, to_x, to_y):
    slope = (to_y - from_y) / float((to_x - from_x))
    if (slope == -0.5) | (slope == 0.5):
      true
    elif (slope == -2) | (slope == 2):
      true
    else:
      false