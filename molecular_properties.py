from rdkit import Chem
from rdkit.Chem import Descriptors

scopolamine_smiles = 'CC1CN2CC[N+](C3CCC4(C3)CC(C4)OC1)C2'
d_amphetamine_smiles = 'CC(CC1=CC=CC=C1)N'

scopolamine = Chem.MolFromSmiles(scopolamine_smiles)
d_amphetamine = Chem.MolFromSmiles(d_amphetamine_smiles)

scopolamine_props = {
    'MolWeight': Descriptors.MolWt(scopolamine),
    'LogP': Descriptors.MolLogP(scopolamine)
}
d_amphetamine_props = {
    'MolWeight': Descriptors.MolWt(d_amphetamine),
    'LogP': Descriptors.MolLogP(d_amphetamine)
}

print("Scopolamine Properties:", scopolamine_props)
print("d-Amphetamine Properties:", d_amphetamine_props)
