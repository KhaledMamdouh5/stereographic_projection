# Stereographic Projection Tool

This project provides a Python implementation for mapping 3D coordinates from a "Unity Cube" onto a 2D $XY$-plane. It uses a spherical intermediary and a mathematical line-plane intersection to perform a **Stereographic Projection**.



## 📐 The Geometric Pipeline

The script transforms a 3D direction vector into a 2D coordinate using the following three-step logic:

### 1. Vector Normalization (Cube to Sphere)
The input is a direction vector $P_{cube}$ (where $0 \le x, y, z \le 1$). This vector is scaled to a sphere of radius $R$:
$$P_{sphere} = R \cdot \frac{P_{cube}}{\|P_{cube}\|}$$

### 2. Line-Plane Intersection
A line is projected starting from the **South Pole** $S(0, 0, -R)$ and passing through the point $P_{sphere}(x_s, y_s, z_s)$.

### 3. Final Projection
The tool calculates where this line intersects the plane at $z=0$. 
* **Time Parameter ($t$):** Determined by: $$t = \frac{R}{z_s + R}$$
* **Projected Coordinates:** * $x_{plane} = t \cdot x_s$
    * $y_{plane} = t \cdot y_s$

---

## 💻 Features

* **Flexible Inputs**: Modify the sphere radius ($R$) or the direction vector ($P_{cube}$) directly in the code.
* **Safety Checks**: Includes logic to handle the "Origin" error and prevents division by zero if a point is at the South Pole.
* **Visual Representation**: Automatically generates a 2D plot showing the projected point relative to the sphere's equator.



---

## 🚀 Getting Started

### Prerequisites
You will need Python 3.x and the following libraries:
```bash
pip install numpy matplotlib
