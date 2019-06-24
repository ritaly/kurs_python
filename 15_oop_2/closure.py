def closure():
  a = "closure"

  def nested(b):
    return a * b

  return nested


new_function = closure()
print(new_function(4))