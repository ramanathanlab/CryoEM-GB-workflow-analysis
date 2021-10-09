
path = Path("/lambda_stor/homes/heng.ma/Research/covid19/nsp_rna_comp/traj_save/frontera/")


positions_dir = Path("anda_sims_positions")
positions_dir.mkdir(exists_ok=True)

pdb_files = list(sorted(path.glob("*.pdb")))
dcd_files = list(sorted(path.glob("*.dcd")))
print(len(pdb_files))
save_dir = positions_dir/"perlmutter"
save_dir.mkdir(exists_ok=True)

from tqdm import tqdm

for pdb_file, traj_file in tqdm(zip(pdb_files, dcd_files)):
    positions = get_positions(pdb_file, traj_file)
    np.save(save_dir / pdb_file.with_suffix(".npy").name, positions)
    
