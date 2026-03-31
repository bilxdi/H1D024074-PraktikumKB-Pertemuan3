import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

# himpunan Fuzzy
terjual = ctrl.Antecedent(np.arange(0, 100), 'terjual')
permintaan = ctrl.Antecedent(np.arange(0, 300), 'permintaan')
harga = ctrl.Antecedent(np.arange(0, 100000), 'harga')
profit = ctrl.Antecedent(np.arange(0, 4000000), 'profit')
stok = ctrl.Consequent(np.arange(0, 1000), 'stok')

# terjual
terjual['Rendah'] = fuzz.trimf(terjual.universe, [0, 0, 40])
terjual['Sedang'] = fuzz.trimf(terjual.universe, [30, 50, 70])
terjual['Tinggi'] = fuzz.trimf(terjual.universe, [60, 100, 100])

# permintaan
permintaan['Rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan['Sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['Tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])

# harga
harga['Murah'] = fuzz.trimf(harga.universe, [0, 0, 40000])
harga['Sedang'] = fuzz.trimf(harga.universe, [30000, 50000, 80000])
harga['Mahal'] = fuzz.trimf(harga.universe, [60000, 100000, 100000])

# profit
profit['Rendah'] = fuzz.trimf(profit.universe, [0, 0, 1000000])
profit['Sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 2500000])
profit['Banyak'] = fuzz.trapmf(profit.universe, [1500000, 2500000, 4000000, 4000000])

# stok
stok['Sedang'] = fuzz.trimf(stok.universe, [100, 500, 900])
stok['Banyak'] = fuzz.trimf(stok.universe, [600, 1000, 1000])

# aturan fuzzy
aturan1 = ctrl.Rule(terjual['Tinggi'] & permintaan['Tinggi'] & harga['Murah'] & profit['Banyak'], stok['Banyak'])
aturan2 = ctrl.Rule(terjual['Tinggi'] & permintaan['Tinggi'] & harga['Murah'] & profit['Sedang'], stok['Sedang'])
aturan3 = ctrl.Rule(terjual['Tinggi'] & permintaan['Sedang'] & harga['Murah'] & profit['Sedang'], stok['Sedang'])
aturan4 = ctrl.Rule(terjual['Sedang'] & permintaan['Tinggi'] & harga['Murah'] & profit['Sedang'], stok['Sedang'])
aturan5 = ctrl.Rule(terjual['Sedang'] & permintaan['Tinggi'] & harga['Murah'] & profit['Banyak'], stok['Banyak'])
aturan6 = ctrl.Rule(terjual['Rendah'] & permintaan['Rendah'] & harga['Sedang'] & profit['Sedang'], stok['Sedang'])

# engine dan system
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6])
system = ctrl.ControlSystemSimulation(engine)

# compute
system.input['terjual'] = 80
system.input['permintaan'] = 225
system.input['harga'] = 25000
system.input['profit'] = 3500000
system.compute()
print("Stok:", int(system.output['stok']))

# view
# kecepatan.view(sim=system)
# terjual.view()
# permintaan.view()
# harga.view()
# profit.view()
# stok.view()
# input("Tekan ENTER untuk selesai")