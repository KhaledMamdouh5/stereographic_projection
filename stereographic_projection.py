import numpy as np
import matplotlib.pyplot as plt

def solve_geometric_projection():
    # ==========================================
    # 1. SETUP PARAMETERS
    # ==========================================
    R = 5.0  # Radius of the sphere
    
    # Define a point on the "Unity Cube" (0 <= x,y,z <= 1)
    # This acts as our direction vector from the origin.
    # You can change these values. At least one value should be 1.0 for it to be "on" the surface.
    p_cube = np.array([1, 1, 1]) 

    print(f"1. Input Point on Cube: {p_cube}")

    # ==========================================
    # 2. INTERSECTION WITH HEMISPHERE
    # ==========================================
    # Calculate the magnitude (length) of the cube vector
    magnitude = np.linalg.norm(p_cube)
    
    if magnitude == 0:
        raise ValueError("The vector cannot be the zero vector (origin).")

    # Scale the vector to length R to find the intersection on the sphere surface
    # P_sphere = R * (P_cube / |P_cube|)
    p_sphere = (p_cube / magnitude) * R
    
    x_s, y_s, z_s = p_sphere
    
    print(f"2. Intersection with Hemisphere: ({x_s:.3f}, {y_s:.3f}, {z_s:.3f})")
    
    # Ensure it is on the upper hemisphere (z >= 0)
    if z_s < 0:
        print("Warning: The point is on the lower hemisphere. Projection logic remains valid but starts below Z=0.")

    # ==========================================
    # 3. PROJECTION TO XY-PLANE (Stereographic)
    # ==========================================
    # We define a line from South Pole S(0, 0, -R) through P_sphere(x_s, y_s, z_s).
    # We want to find where it intersects z = 0.
    
    # Derivation:
    # Vector V = P_sphere - South_Pole = (x_s, y_s, z_s - (-R)) = (x_s, y_s, z_s + R)
    # Line equation: L(t) = South_Pole + t * V
    # z(t) = -R + t * (z_s + R). 
    # We want z(t) = 0 => t = R / (z_s + R)
    
    # Avoid division by zero if z_s is -R (South Pole)
    if np.isclose(z_s, -R):
        raise ValueError("Point is at the South Pole; projection is at infinity.")

    t = R / (z_s + R)
    
    # Calculate x and y on the plane
    # x(t) = 0 + t * x_s
    # y(t) = 0 + t * y_s
    x_plane = t * x_s
    y_plane = t * y_s
    
    p_plane = np.array([x_plane, y_plane])
    print(f"3. Intersection with XY-Plane: ({x_plane:.3f}, {y_plane:.3f})")

    # ==========================================
    # 4. PLOTTING
    # ==========================================
    fig, ax = plt.subplots(figsize=(6, 6))

    # A. Plot the Reference Circle at z=0 (The Equator)
    # Note: x^2 + y^2 = 0 is a point. Assuming x^2 + y^2 = R^2 for context.
    circle = plt.Circle((0, 0), R, color='blue', fill=False, linestyle='--', label=f'Equator (R={R})')
    ax.add_patch(circle)

    # B. Plot the Origin
    ax.plot(0, 0, 'k+', label='Origin')

    # C. Plot the Calculated Intersection Point
    ax.plot(x_plane, y_plane, 'ro', label='Projected Intersection')
    ax.text(x_plane, y_plane, f'  ({x_plane:.2f}, {y_plane:.2f})', fontsize=9)

    # Formatting the plot
    ax.set_aspect('equal')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title(f'Projection on XY-Plane (z=0)\nInput Vector: {p_cube}')
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    ax.legend()
    
    # Set limits to ensure circle and point are visible with some padding
    max_limit = max(R, abs(x_plane), abs(y_plane)) * 1.2
    ax.set_xlim(-max_limit, max_limit)
    ax.set_ylim(-max_limit, max_limit)

    plt.show()

if __name__ == "__main__":
    solve_geometric_projection()
