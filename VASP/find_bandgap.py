import numpy as np

filename = "EIGENVAL"

file_open = open(filename, "r")

lines = file_open.readlines()

#homo = 118
#lumo = 119

en_homo = []
en_lumo = []
homo_band_list = []
lumo_band_list = []

for i in range(4, len(lines)):
#    break
    criteria = lines[i].find("1.000000")
    if criteria == -1:
        criteria2 = lines[i - 1].find("1.000000")
        if criteria2 != -1:
            homo_split = lines[i - 1].split()
            homo_band_list.append(homo_split[0])
            homo_band = set(homo_band_list)
#            print(lines[i - 1])
            lumo_split = lines[i].split()
            lumo_band_list.append(lumo_split[0])
            lumo_band = set(lumo_band_list)
#            print(lines[i])
            i += 25
print(f"LUMO at band {lumo_band}")
print(f"HOMO at band {homo_band}")

homo_list = list(homo_band)
lumo_list = list(lumo_band)

#print(homo_list)
#print(lumo_list)

for line in lines:
    for homo in homo_list:
        criteria1 = line.find(f" {homo}      ")
        if criteria1 != -1:
            line_split = line.split()
            en_homo.append(line_split[1])
#        print(line_split)
    for lumo in lumo_list:
        criteria2 = line.find(f" {lumo}      ")
        if criteria2 != -1:
            line_split = line.split()
            en_lumo.append(line_split[1])
#        print(line_split)

print(en_lumo)
print(en_homo)

homo_arr = np.array(en_homo, dtype=float)
lumo_arr = np.array(en_lumo, dtype=float)

homo_arr_new = [] #homo_arr
lumo_arr_new = [] #lumo_arr
print(len(homo_arr_new))
if len(homo_arr) <= len(lumo_arr):
    for i in range(0, len(homo_arr)):
        if homo_arr[i] <= lumo_arr[i]:
            lumo_arr_new.append(lumo_arr[i])
            homo_arr_new.append(homo_arr[i])
#            continue
#        else:
#            lumo_arr_new = np.delete(lumo_arr, i)
else:
#    homo_arr = homo_arr[:len(lumo_arr)]
    for i in range(0, len(lumo_arr)):
        if homo_arr[i] <= lumo_arr[i]:
            homo_arr_new.append(homo_arr[i])
            lumo_arr_new.append(lumo_arr[i])
#            continue
#        else:
#            homo_arr_new = np.delete(homo_arr, i)
#            print(homo_arr_new)
#            print(len(homo_arr_new))


homo_arr_new = np.array(homo_arr_new)
lumo_arr_new = np.array(lumo_arr_new)

homo_max = np.max(homo_arr_new)
homo_max_index = np.argmax(homo_arr_new)

lumo_min = np.min(lumo_arr_new)
lumo_min_index = np.argmin(lumo_arr_new)

print(f"MAX HOMO: {homo_max} (band {homo_list}) at KPOINT {homo_max_index + 1}")
print(f"MIN LUMO: {lumo_min} (band {lumo_list}) at KPOINT {lumo_min_index + 1}")
print(f"BAND GAP: {lumo_min - homo_max} eV")
file_open.close()
