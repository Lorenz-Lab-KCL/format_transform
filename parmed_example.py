import parmed as pmd

#Loading a pdb file using parmed, creating a structure that preserves the coordinates
str=pmd.load_file("test.pdb",structure=True)

#Saving it in mol2 file
str.save("test.mol2")
