
import numpy as np

lattice_parameter = 2.86

#basis (unit cell dimensions)
basis = np.array([[1.0,0.0,0.0],
                 [0.0,1.0,0.0],
                 [0.0,0.0,1.0]])*lattice_parameter

#define atom positions in unit cell

base_atoms = np.array([[0.0,0.0,0.0],
                       [1.0,0.0,0.0],
                       [0.0,1.0,0.0],
                       [1.0,1.0,0.0],
                       [0.0,0.0,1.0],
                       [1.0,0.0,1.0],
                       [1.0,1.0,1.0],
                       [0.0,1.0,1.0],
                       [0.5,0.5,0.5]])*lattice_parameter


system_size = 50

positions = []
for i in range(system_size):
    for j in range(system_size):
        for k in range(system_size):
            base_position = np.array([i,j,k])
            cart_position = np.inner(basis.T, base_position)
            for atom in base_atoms: 
                positions.append(cart_position + atom)



# Convert positions to numpy array for plotting
positions = np.array(positions)

unique_positions, unique_indices = np.unique(positions, axis=0, return_index=True)

num_atoms = len(unique_positions)

with open('bcc_ferrite.data','w') as fdata:
    fdata.write('BCC ferrite atoms - written to test crystalline metal generation\n\n')
    fdata.write('{} atoms\n'.format(num_atoms))
    fdata.write('{} atom types\n'.format(1))

    fdata.write('{} {} xlo xhi\n'.format(0.0, system_size*lattice_parameter))
    fdata.write('{} {} ylo yhi\n'.format(0.0, system_size*lattice_parameter))
    fdata.write('{} {} zlo zhi\n'.format(0.0, system_size*lattice_parameter))
    fdata.write('\n')

    fdata.write('Atoms\n\n')

    for i,pos in enumerate(unique_positions):
        fdata.write('{} 1 {} {} {}\n'.format(i+1,*pos))
