import matplotlib.pyplot as plt
import random

def create_plot(numbers):
    if len(numbers) == 0:
        return

    # Define themes
    themes = [
        {
            "bg": "#fde2e4",      # very light pink
            "line": "#d6336c"    # deep pink
        },
        {
            "bg": "#e3f2fd",     # very light blue
            "line": "#1e3a8a"    # dark blue
        }
    ]

    theme = random.choice(themes)

    plt.figure(facecolor=theme["bg"])
    ax = plt.gca()
    ax.set_facecolor(theme["bg"])

    if len(numbers) > 1:
        plt.plot(
            numbers,
            marker=".",
            color=theme["line"],
            linewidth=2,
            markersize=8
        )
        plt.title("Line Graph")
        plt.xlabel("Index")
        plt.ylabel("Value")
    else:
        plt.bar(
            ["Value"],
            numbers,
            color=theme["line"]
        )
        plt.title("Single Value")

    plt.show()
