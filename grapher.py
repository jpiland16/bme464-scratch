import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

NUM_OF_CHANNELS = 2

fig, ax = plt.subplots()

lines = []

for _ in range(NUM_OF_CHANNELS):
    ln, = ax.plot([], [])
    lines.append(ln)

def init():
    ax.set_xlim(0, 99)
    ax.set_ylim(-10, 1030)
    return ln,

def update(frame):
    with open("out.txt",  "r") as file:
        y_lines = file.read().splitlines()
    try:
        for j, ln in enumerate(lines):
            ln.set_data([i for i in range(len(y_lines))], [int(v.split(",")[j]) for v in y_lines])
    except:
        print("ERROR")
        pass
    return lines

ani = FuncAnimation(fig, update, cache_frame_data=False,
                    init_func=init, blit=True)
plt.show()
