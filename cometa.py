# Fatima Ximena Nava Araujo

import numpy as np
import matplotlib.pyplot as plt

# Parámetros orbitales del cometa Halley
a = 17.8                    # semieje mayor (UA)
e = 0.967                   # excentricidad
b = a * np.sqrt(1 - e**2)   # semieje menor
c = a * e                   # distancia del centro al foco

# Coordenadas de la elipse (x desplazado para que el Sol esté en el foco)
theta = np.linspace(0, 2 * np.pi, 1000)
x = a * np.cos(theta) + c  # desplazamos la elipse hacia la derecha
y = b * np.sin(theta)

# Dibujar la órbita
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Órbita del cometa Halley", color='blue')
plt.scatter(0, 0, color='orange', label="Sol", s=100, zorder=5)  # Sol en el foco
plt.axis('equal')

# Mejorar visualización
plt.title("Órbita del cometa Halley (aproximación elíptica)")
plt.xlabel("x (UA)")
plt.ylabel("y (UA)")
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
