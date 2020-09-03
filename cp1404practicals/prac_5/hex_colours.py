COLOUR_DICT = {"black": "#000000", "blue1": "#0000ff", "blueviolet": "#8a2be2", "chocolate": "#d2691",
               "coral1": "#ff7256", "cornsilk1": "#fff8dc", "darkgoldenrod1": "#ffb90f", "darkgreen": "#006400",
               "darkorange": "#ff8c00", "firebrick": "#b22222"}

colour_selection = input("Please enter a colour name (with no spaces >>> ").lower()
while colour_selection != "":
    try:
        print(COLOUR_DICT[colour_selection])
    except KeyError:
        print("Colour selection must appear in the list {}".format(COLOUR_DICT.keys()))
    colour_selection = input("Please enter another colour name >>> ").lower()