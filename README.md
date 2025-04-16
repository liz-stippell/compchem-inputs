# compchem-inputs
Input files for various calculations for various computational chemistry software programs

## VASP (Vienna ab initio Simulation Package)
<b>Types of calculations:</b>
- Geometry optimization
- Single point calculation
  - PBE functional
  - HSE hybrid functional
- Molecular dynamics
  - Temperature ramp (0 K to desired temp, usually 300 K)
  - Equilibrate (NVT)
  - NVE
<b>Other necessary input files:</b>
- KPOINTS file
- submit file

## CP2K
<b>Types of calculations:</b>
- Geometry optimization
  - Atomic position optimization
  - Cell optimization
- Single point calculation
<b>Other necessary input files:</b>
- POTENTIAL
- BASIS_MOLOPT
- dft3d.dat
  
## LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator)
<b>Types of calculations:</b>
- Lattice constant and heat capacity calculations
- Energy calculation
- Elastic constants calculation
