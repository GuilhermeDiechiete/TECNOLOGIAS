medida = float(input('Digite a Distancia em KM:'))

# km hm dam m dm cm mm
mm = medida * 1000
cm = medida * 100
dm = medida * 10
m = medida
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('A medida de {} em mm é {}, cm {} dm{} m{} dam{} hm{} km{}'.format(medida, mm, cm, dm, m, dam, hm, km))
