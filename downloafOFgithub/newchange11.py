import os
import shutil
import random
# change POSCAR1 file
file_path = "/home/baran/Desktop/VMoWS2num17/test3/POSCAR1"
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, content):
    with open(file_path, 'w', newline='\r\n') as file:
        file.writelines(content)

def generate_new_POSCAR(lines):
    poscar_A = random.sample(lines[8:17], 3)
    poscar_B = random.sample([line for line in lines[8:17] if line not in poscar_A], 3)
    poscar_C = [line for line in lines[8:17] if line not in poscar_A + poscar_B]
    
    new_POSCAR = lines[:8] + poscar_A + poscar_B + poscar_C + lines[17:]
    return new_POSCAR

def compare_and_save(new_POSCAR, result_folder):
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    
    for root, dirs, files in os.walk(result_folder):
        for file in files:
            if file == 'POSCAR':
                existing_POSCAR = read_file(os.path.join(root, file))
                if existing_POSCAR == new_POSCAR:
                    return False
    
    write_file(os.path.join(result_folder, 'POSCAR'), new_POSCAR)
    return True

def main():
    base_dir = '/home/baran/Desktop/VMoWS2num17/test3'
    poscar1 = read_file(os.path.join(base_dir, 'POSCAR1'))
    incar = read_file(os.path.join(base_dir, 'INCAR'))
    kpoint = read_file(os.path.join(base_dir, 'KPOINTS'))
    potcar = read_file(os.path.join(base_dir, 'POTCAR'))
    walk = read_file(os.path.join(base_dir, 'walk_account'))
    
    result_folders = [f'/home/baran/Desktop/VMoWS2num17/test3/result{i}' for i in range(1, 1001)]
    current_result = 1

    while current_result < 1001:
        new_POSCAR = generate_new_POSCAR(poscar1)
        result_folder = result_folders[current_result - 1]
        
        if compare_and_save(new_POSCAR, result_folder):
            shutil.copyfile(os.path.join(base_dir, 'INCAR'), os.path.join(result_folder, 'INCAR'))
            shutil.copyfile(os.path.join(base_dir, 'KPOINTS'), os.path.join(result_folder, 'KPOINTS'))
            shutil.copyfile(os.path.join(base_dir, 'POTCAR'), os.path.join(result_folder, 'POTCAR'))
            shutil.copyfile(os.path.join(base_dir, 'walk_account'), os.path.join(result_folder, 'walk_account'))
            current_result += 1

if __name__ == "__main__":
    main()

print("Process completed successfully.")     
    
