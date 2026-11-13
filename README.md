# Gravitational Lensing Ray-Tracer

A Python simulation of gravitational lensing by a point mass, using backward ray-tracing.

## How this code works
- Each pixel on the image plane is traced back to the source plane using the lens equation: β = θ − θ/|θ|² (angles in units of the Einstein radius).
- The source is a Gaussian blob. A pixel is bright if its ray came from near the source.
- A source directly behind the lens gives an Einstein ring. An offset source gives two images.

## Usage
```bash
pip install numpy matplotlib
python lensing_raytracer.py
```
Enter the source position (keep the distance from the lens at 2 or less) and the source size (0.03 to 0.3 works well).

## The Einstein Radius
Einstein radius is the angular size of the ring you see when a source sits exactly behind the lens. It is the natural length scale of lensing.
Gravity bends light by α = 4GM / (c²b)
The bending depends on how close the ray passes to the mass. For a source exactly behind the lens, the rays that reach you from all around the lens must be bent by just the right amount to arrive at you. That happens at one special angle, and it is the Einstein radius:

```
θ_E = √( 4GM / c² × D_LS / (D_L × D_S) )
```
`M` is the mass of the lens.
`D_L` is the distance from you to the lens.
`D_S` is the distance from you to the source.
`D_LS` is the distance from the lens to the source.

### About the 2 uploaded results
1. Figure_1 is the source offset by 0.5 θ_E: two images at x ≈ 1.28 and x ≈ −0.78
2. Figure_2 is the non-offset source at 0.0, 0.0 (Due to no offset we see it as a ring!)
