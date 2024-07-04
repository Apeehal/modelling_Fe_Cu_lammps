import numpy as np

num_atoms = 1000

system_size = 20.0

positions = []

for i in range(num_atoms):
    positions.append(np.random.rand(3)*system_size)

with open('random.data','w') as fdata:
    fdata.write('Random atoms - written as a test\n\n')
    fdata.write('{} atom\n'.format(num_atoms))
    fdata.write('{} atom types\n'.format(1))

    fdata.write('{} {} xlo xhi\n'.format(0.0, system_size))
    fdata.write('{} {} ylo yhi\n'.format(0.0, system_size))
    fdata.write('{} {} zlo zhi\n'.format(0.0, system_size))
    fdata.write('\n')

    fdata.write('Atom\n\n')

    for i,pos in enumerate(positions):
        fdata.write('{} 1 {} {} {}\n'.format(i+1,*pos))
