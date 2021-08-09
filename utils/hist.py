from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np


def get_style():
    plt.rcdefaults()
    plt.rcParams.update({
        "xtick.major.size": 5,
        "xtick.major.pad": 7,
        "xtick.labelsize": 15,
        "grid.color": "0.5",
        "grid.linestyle": "-",
        "grid.linewidth": 5,
        "lines.linewidth": 2,
        "lines.color": "g",
    })
    fig, ax = plt.subplots()

    # Example data
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')
    plt.grid(axis='x', which='both', linewidth=.4, zorder=1)

    return [fig, ax]
# # Define a 1st position to annotate (display it with a marker)
# xy = (1, 2)
# ax.plot(xy[0], xy[1], ".r")

# # Annotate the 1st position with a text box ('Test 1')
# offsetbox = TextArea("Test 1")

# ab = AnnotationBbox(offsetbox, xy,
#                     xybox=(-20, 40),
#                     xycoords='data',
#                     boxcoords="offset points",
#                     arrowprops=dict(arrowstyle="->"))
# ax.add_artist(ab)

# # Annotate the 1st position with another text box ('Test')
# offsetbox = TextArea("Test")

# ab = AnnotationBbox(offsetbox, xy,
#                     xybox=(1.02, xy[1]),
#                     xycoords='data',
#                     boxcoords=("axes fraction", "data"),
#                     box_alignment=(0., 0.5),
#                     arrowprops=dict(arrowstyle="->"))
# ax.add_artist(ab)

# # Define a 2nd position to annotate (don't display with a marker this time)
# xy = [2, 3]

# # Annotate the 2nd position with a circle patch
# da = DrawingArea(20, 20, 0, 0)
# p = Circle((10, 10), 10)
# da.add_artist(p)

# ab = AnnotationBbox(da, xy,
#                     xybox=(1.02, xy[1]),
#                     xycoords='data',
#                     boxcoords=("axes fraction", "data"),
#                     box_alignment=(0., 0.5),
#                     arrowprops=dict(arrowstyle="->"))

# ax.add_artist(ab)

# # Annotate the 2nd position with an image (a generated array of pixels)
# arr = np.arange(100).reshape((10, 10))
# im = OffsetImage(arr, zoom=2)
# im.image.axes = ax

# ab = AnnotationBbox(im, [performance[0]-.5, 0],
#                     xybox=(0, 0),
#                     xycoords='data',
#                     boxcoords="offset points",)

# ax.add_artist(ab)

# # Annotate the 2nd position with another image (a Grace Hopper portrait)
# with get_sample_data("grace_hopper.jpg") as file:
#     arr_img = plt.imread(file)

# imagebox = OffsetImage(arr_img, zoom=0.03)
# imagebox.image.axes = ax

# ab = AnnotationBbox(imagebox, [performance[1], 1],
#                     xybox=(0, 0.),
#                     xycoords='data',
#                     boxcoords="offset points",
#                     )

# ax.add_artist(ab)

# # Fix the display limits to see everything
# # ax.set_xlim(0, 1)
# # ax.set_ylim(0, 1)

# plt.show()


if __name__ == "__main__":
    get_style()
