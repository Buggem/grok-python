def bork(process):
  return process.replace("th", "z").replace("TH", "Z").replace("Th", "Z")

def inpsub(inp):
  return input(bork(inp))
def prisub(pri):
  print(bork(pri))

in1 = inpsub("Ingredient 1: ")
in2 = inpsub("Ingredient 2: ")
in3 = inpsub("Ingredient 3: ")
prisub(f"First cut the {in1} into triangles.")
prisub(f"Then smash the {in2} with a hammer.")
prisub(f"Fry a mix of {in1} and {in2} stirring gently.")
prisub(f"Add in the {in3} one ladle at a time.")
prisub(f"Sprinkle the remaining {in1} over the top.")
print("Bork! Bork! Bork!")
