import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

# Données
I = 3  # Intensité
R = 0.45   # Résistance
Xs = 2  # Réactance synchrone (valeur arbitraire pour l'exemple)
V=10
phi_deg = 54
phi_rad = np.radians(phi_deg)

# V 
V_x = V
V_y = 0

# Vecteur I (référence pour les autres)
I_x = I * np.cos(phi_rad)
I_y = -I * np.sin(phi_rad)  # courant en retard -> vers le bas

# Vecteur RI (dans la direction de I)
RI_x = R * I_x
RI_y = R * I_y

# Vecteur jXsI (perpendiculaire à I vers la gauche car j = +90°)
XsI_x = -Xs * I_y
XsI_y = Xs * I_x



# E = V + jXsI
E_x = V_x +RI_x+ XsI_x
E_y = V_y +RI_y+ XsI_y

# Tracé
fig, ax = plt.subplots()
origin = np.array([0, 0])
RI_vec = np.array([RI_x, RI_y])
XsI_vec = np.array([XsI_x, XsI_y])
V_vec = np.array([V_x, V_y])
E_vec = np.array([E_x, E_y])
E=(E_x**2+E_y**2)**0.5

# Vecteur V à partir de l'origine
ax.quiver(*origin, *V_vec, color='deepskyblue', angles='xy', scale_units='xy', scale=1, label='V')

# Vecteur RI à partir du bout de V
ax.quiver(V_x, V_y, *RI_vec, color='green', angles='xy', scale_units='xy', scale=1, label='R·I')

# Vecteur jXsI à partir du bout de RI
ax.quiver(V_x + RI_x, V_y + RI_y, *XsI_vec, color='lime', angles='xy', scale_units='xy', scale=1, label='jXₛ·I')

# Vecteur E à partir de l'origine au bout de jXsI
ax.quiver(*origin,V_x + RI_x + XsI_x, V_y + RI_y + XsI_y ,color='red', angles='xy', scale_units='xy', scale=1, linestyle='--', label='E')

# Définir I_vec (vecteur I) ici avant de l'utiliser pour éviter l'erreur
I_vec = np.array([I_x, I_y])

# Vecteur I 
ax.quiver(*origin, *I_vec, color='blue', angles='xy', scale_units='xy', scale=1, label='I')

# Angle phi
angle_marker_radius = 0.2
arc = Arc((0, 0), 2*angle_marker_radius, 2*angle_marker_radius, angle=0,
          theta1=0, theta2=phi_deg, color='blue', linestyle='--')
ax.add_patch(arc)
ax.text(0.4, -0.1, r'$\varphi$', fontsize=12)
print(f"E_x : {E_x} | E_y : {E_y} | E: {E} V")

# Réglages
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlim(-1, E)
ax.set_ylim(-E/2, E/2)
ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.set_title("Diagramme vectoriel de Behn-Eschenburg ")
ax.legend()
plt.savefig("Behn-Eschenburg.png")
