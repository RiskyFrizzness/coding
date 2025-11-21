from orbitronomy.orbitCalcs import SimpleOrbit
from scipy.constants import G, pi
from collections import namedtuple
import tkinter as tk
from math import e
from tkinter import messagebox

Body = namedtuple("Body", ("name", "semiMajorAxis", "perihelion", "eccentricity", "inclination", "longitudeOfAscendingNode", "argumentOfPerihelion"))

earth = Body('Earth', 1, 0.98, 0, 0, 348.73, 113.20783)
mars = Body('Mars', 1.523680550622, 1.38136992882, 0, 0, 2, 0)

SOLAR_MASS = 1.9891 * 10 ** 30

def period(body):
    answer = body.semiMajorAxis * 1.496e+11
    answer **= 3
    answer /= G * SOLAR_MASS
    answer **= 0.5 
    answer *= 2 * pi
    return answer

def phase_angle(transfer, target):
    return 180 - (period(transfer) / 2) * (360 / period(target))

def dv(oragin , target):
    r1 = oragin.semiMajorAxis * 1.496e+11 #Covert au to M 
    r2 = target.semiMajorAxis * 1.496e+11 #Covert au to M 
    answer = r2 * 2
    answer /= r2 + r1
    answer **= 0.5
    answer -= 1
    answer *= ((G * SOLAR_MASS) / r1) ** 0.5 
    return answer 

def calculate_burned_fuel_mass(dv, isp, mass):
     print(isp * G * SOLAR_MASS)
     answer = dv / (isp * G * SOLAR_MASS)
     return mass / e ** answer

def hohmann_transfer(oragin, target):
    oragin_aphelion = oragin.semiMajorAxis * (1 + oragin.eccentricity)
    target_aphelion = target.semiMajorAxis * (1 + target.eccentricity)
    oragin_radius = (oragin.perihelion + oragin.semiMajorAxis * (oragin.eccentricity + 1)) / 2
    target_radius = target_aphelion #(target.perihelion + target.semiMajorAxis * (target.eccentricity + 1)) / 2

    aphelion = max(oragin.semiMajorAxis, target.semiMajorAxis)
    perihelion = min(oragin.semiMajorAxis, target.semiMajorAxis) 
    return Body(
        "transfer",
        (oragin_radius + target_radius) / 2,
        perihelion,
        (aphelion - perihelion) / (aphelion + perihelion),
        0, 
        0,
        0
    )

def calculate(oragin, target, isp, mass):
     burn_dv = dv(oragin, target)
     info = f"from: {oragin.name}\n"
     info += f"To: {target.name}\n"
     info += f"Eccentricity: {round(hohmann_transfer(oragin, target).eccentricity, 4)}\n"
     info += f"Δv: {round(burn_dv)} m/s\n"
    #  info += f"Fuel Burned: {int(calculate_burned_fuel_mass(burn_dv, isp, mass))} kg"
     messagebox.showinfo("Results", info)

def visulize(bodies):
        
        orbit: SimpleOrbit = SimpleOrbit(plot_title="Mars Planner", name="Mars Planner")

        orbit.faceColor('black')
        orbit.paneColor('black')
        orbit.gridColor('#222831')
        orbit.orbitTransparency(0.5)
        orbit.labelColor('white')
        orbit.tickColor('white')
        orbit.plotStyle(background_color="dark_background")

        # semiMajorAxis, perihelion, eccentricity, inclination, longitudeOfAscendingNode, argumentOfPerihelion
        #523680550622#
        # data = [earth]
        # data = [["object1", 1.00000101806, 0.983289891, 0.01671123, 90, 2, 0, "green"], 
        #     ["object2", 1.5, 0.483289891, 0.02671123, 6, 0, 0, "yellow"], 
        #     ["object3", 1.3, 0.683289891, 0.01671123, 2, 0, 0, "red"]]

        orbit.calculateOrbit(plot_steps = 1000, data = bodies, n_orbits = 1, trajectory = True)

        orbit.animateOrbit(dpi = 250, save=False, export_zoom = 3, font_size  = "xx-small", export_folder = "results")

def main():
     root = tk.Tk()
     root.title("Transfer")

     frame = tk.Frame(root)
     frame.pack(padx = 10, pady = 10)

     lables = ["Isp", "Wet mass", "Trust"]
     entries = []

     for i, text in enumerate(lables):
            lable = tk.Label(frame, text = text)
            lable.grid(row = i, column = 0, sticky = "e", padx = 5, pady = 5)
     
            entry = tk.Entry(frame)
            entry.grid(row = i, column = 1, padx = 5, pady = 5)
            entries.append(entry)
     calc_button = tk.Button(frame, text = "Calculate", command = lambda: calculate(earth, mars, int(entries[0].get()), int(entries[1].get())))
     calc_button.grid(row = len(lables) + 2, column = 0, padx = 5, pady = 5)
     calc_button = tk.Button(frame, text = "Visulize", command = lambda: visulize([earth, mars, hohmann_transfer(earth, mars)]))
     calc_button.grid(row = len(lables) + 2, column = 1, padx = 5, pady = 5)
     tk.mainloop()
main()