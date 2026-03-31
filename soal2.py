import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

# himpunan Fuzzy
informasi = ctrl.Antecedent(np.arange(0, 100), 'informasi')
persyaratan = ctrl.Antecedent(np.arange(0, 100), 'persyaratan')
petugas = ctrl.Antecedent(np.arange(0, 100), 'petugas')
sarpras = ctrl.Antecedent(np.arange(0, 100), 'sarpras')
pelayanan = ctrl.Consequent(np.arange(0, 400), 'pelayanan')

# informasi
informasi['Tidak'] = fuzz.trapmf(informasi.universe, [0, 0, 60, 75])
informasi['Cukup'] = fuzz.trimf(informasi.universe, [60, 75, 90])
informasi['Memuaskan'] = fuzz.trapmf(informasi.universe, [75, 90, 100, 100])

# persyaratan
persyaratan['Tidak'] = fuzz.trapmf(persyaratan.universe, [0, 0, 60, 75])
persyaratan['Cukup'] = fuzz.trimf(persyaratan.universe, [60, 75, 90])
persyaratan['Memuaskan'] = fuzz.trapmf(persyaratan.universe, [75, 90, 100, 100])

# petugas
petugas['Tidak'] = fuzz.trapmf(petugas.universe, [0, 0, 60, 75])
petugas['Cukup'] = fuzz.trimf(petugas.universe, [60, 75, 90])
petugas['Memuaskan'] = fuzz.trapmf(petugas.universe, [75, 90, 100, 100])

# sarpras
sarpras['Tidak'] = fuzz.trapmf(sarpras.universe, [0, 0, 60, 75])
sarpras['Cukup'] = fuzz.trimf(sarpras.universe, [60, 75, 90])
sarpras['Memuaskan'] = fuzz.trapmf(sarpras.universe, [75, 90, 100, 100])

# pelayanan
pelayanan['Tidak'] = fuzz.trapmf(pelayanan.universe, [0, 0, 50, 75])
pelayanan['Kurang'] = fuzz.trapmf(pelayanan.universe, [50, 75, 100, 150])
pelayanan['Cukup'] = fuzz.trapmf(pelayanan.universe, [100, 150, 250, 275])
pelayanan['Memuaskan'] = fuzz.trapmf(pelayanan.universe, [250, 275, 325, 350])
pelayanan['Sangat'] = fuzz.trapmf(pelayanan.universe, [325, 350, 400, 400])

# aturan fuzzy
aturan1 = ctrl.Rule(informasi['Tidak'] & persyaratan['Tidak'] & petugas['Tidak'] & sarpras['Tidak'], pelayanan['Tidak'])
aturan2 = ctrl.Rule(informasi['Tidak'] & persyaratan['Tidak'] & petugas['Tidak'] & sarpras['Cukup'], pelayanan['Tidak'])
aturan3 = ctrl.Rule(informasi['Tidak'] & persyaratan['Tidak'] & petugas['Tidak'] & sarpras['Memuaskan'], pelayanan['Tidak'])
aturan4 = ctrl.Rule(informasi['Tidak'] & persyaratan['Tidak'] & petugas['Cukup'] & sarpras['Tidak'], pelayanan['Tidak'])
aturan5 = ctrl.Rule(informasi['Tidak'] & persyaratan['Tidak'] & petugas['Cukup'] & sarpras['Cukup'], pelayanan['Tidak'])
aturan6 = ctrl.Rule(informasi['Tidak'] & persyaratan['Tidak'] & petugas['Cukup'] & sarpras['Memuaskan'], pelayanan['Cukup'])
aturan7 = ctrl.Rule(informasi['Tidak'] & persyaratan['Tidak'] & petugas['Memuaskan'] & sarpras['Tidak'], pelayanan['Tidak'])
aturan8 = ctrl.Rule(informasi['Tidak'] & persyaratan['Tidak'] & petugas['Memuaskan'] & sarpras['Cukup'], pelayanan['Cukup'])
aturan9 = ctrl.Rule(informasi['Tidak'] & persyaratan['Tidak'] & petugas['Memuaskan'] & sarpras['Memuaskan'], pelayanan['Cukup'])
aturan10 = ctrl.Rule(informasi['Cukup'] & persyaratan['Cukup'] & petugas['Cukup'] & sarpras['Memuaskan'], pelayanan['Memuaskan'])
aturan11 = ctrl.Rule(informasi['Cukup'] & persyaratan['Cukup'] & petugas['Memuaskan'] & sarpras['Memuaskan'], pelayanan['Memuaskan'])
aturan12 = ctrl.Rule(informasi['Cukup'] & persyaratan['Memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], pelayanan['Sangat'])
aturan13 = ctrl.Rule(informasi['Memuaskan'] & persyaratan['Memuaskan'] & petugas['Memuaskan'] & sarpras['Memuaskan'], pelayanan['Sangat'])

# aturan14 = ctrl.Rule(informasi['Cukup'] & persyaratan['Tidak'] & petugas['Tidak'] & sarpras['Memuaskan'], pelayanan['Kurang']) # aturan 14 untuk menghilangkan error

# engine dan system
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9, aturan10, aturan11, aturan12, aturan13]) # <- tambah aturan14 untuk fix error
system = ctrl.ControlSystemSimulation(engine)

# compute
system.input['informasi'] = 80
system.input['persyaratan'] = 60
system.input['petugas'] = 50
system.input['sarpras'] = 90
system.compute()
print("Pelayanan:", int(system.output['pelayanan']))

# view
# pelayanan.view(sim=system)
# informasi.view()
# persyaratan.view()
# petugas.view()
# sarpras.view()
# pelayanan.view()
# input("Tekan ENTER untuk selesai")