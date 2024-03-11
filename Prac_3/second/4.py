import matplotlib.pyplot as plt
import numpy as np

# Define the pairs array
pairs = "..LEXEGEZACEBISO" \
        "USESARMAINDIREA." \
        "ERATENBERALAVETI" \
        "EDORQUANTEISRION"


# Define the plansys structure
class plansys:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.economy = 0
        self.govtype = 0
        self.techlev = 0
        self.population = 0
        self.productivity = 0
        self.radius = 0
        self.goatsoupseed = None
        self.name = ""


# Define the tweakseed function
def tweakseed(s):
    temp = (s.w0 + s.w1 + s.w2) & 0xFFFF
    s.w0 = s.w1
    s.w1 = s.w2
    s.w2 = temp


# Define the makesystem function
def makesystem(s):
    thissys = plansys()
    longnameflag = (s.w0 & 64) != 0

    thissys.x = s.w1 >> 8
    thissys.y = s.w0 >> 8

    thissys.govtype = (s.w1 >> 3) & 7

    thissys.economy = (s.w0 >> 8) & 7
    if thissys.govtype <= 1:
        thissys.economy |= 2

    thissys.techlev = (s.w1 >> 8) & 3 + (thissys.economy ^ 7)
    thissys.techlev += thissys.govtype >> 1
    if thissys.govtype & 1 == 1:
        thissys.techlev += 1

    thissys.population = 4 * thissys.techlev + thissys.economy
    thissys.population += thissys.govtype + 1
    thissys.productivity = ((thissys.economy ^ 7) + 3) * (thissys.govtype + 4)
    thissys.productivity *= thissys.population * 8

    thissys.radius = 256 * ((s.w2 >> 8) & 15) + 11 + thissys.x

    thissys.goatsoupseed = {
        'a': s.w1 & 0xFF,
        'b': s.w1 >> 8,
        'c': s.w2 & 0xFF,
        'd': s.w2 >> 8
    }

    pair1 = 2 * ((s.w2 >> 8) & 31)
    tweakseed(s)
    pair2 = 2 * ((s.w2 >> 8) & 31)
    tweakseed(s)
    pair3 = 2 * ((s.w2 >> 8) & 31)
    tweakseed(s)
    pair4 = 2 * ((s.w2 >> 8) & 31)
    tweakseed(s)

    thissys.name = pairs[pair1: pair1 + 2] + pairs[pair2: pair2 + 2] + pairs[pair3: pair3 + 2]

    if longnameflag:
        thissys.name += pairs[pair4: pair4 + 2]
    else:
        thissys.name += ""

    thissys.name = thissys.name.replace('.', '')

    return thissys


# Define the stripout function
def stripout(name, char):
    name = name.replace(char, '')


# Define the plot_map function
def plot_map(systems):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_title("Elite Galaxy Map", color='white')
    ax.set_xlabel("X", color='white')
    ax.set_ylabel("Y", color='white')
    ax.set_facecolor('black')  # Установка черного фона для области с точками
    ax.grid(color='white', linestyle='-', linewidth=0.5)

    for system in systems:
        ax.scatter(system.x, system.y, color='blue', marker='o', label=system.name)
        ax.text(system.x + 0.1, system.y + 0.1, system.name, color='blue')

    plt.show()


# Seed for the first galaxy
seed = {"w0": 0x5A4A, "w1": 0x0248, "w2": 0xB753}
seed = type('', (object,), seed)()

# Generate systems
num_systems = 100  # You can adjust the number of systems as needed
systems = []
for _ in range(num_systems):
    systems.append(makesystem(seed))
    tweakseed(seed)

# Plot the map
plot_map(systems)
