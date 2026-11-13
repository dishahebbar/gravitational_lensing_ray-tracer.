# Gravitational Lensing Ray-Tracer

A Python simulation of gravitational lensing by a point mass, using backward ray-tracing.

## How this code works
- Each pixel on the image plane is traced back to the source plane using the lens equation: β = θ − θ/|θ|² (angles in units of the Einstein radius).
- The source is a Gaussian blob. A pixel is bright if its ray came from near the source.
- A source directly behind the lens gives an Einstein ring. An offset source gives two images.

## Usage
pip install numpy matplotlib
python lensing_raytracer.py

Enter the source position (keep the distance from the lens at 2 or less) and the source size (0.03 to 0.3 works well).
