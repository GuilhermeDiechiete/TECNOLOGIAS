vel = int(input('Velocidade do Veiculo:'))

multa = (vel - 40) * 2.5

if vel >40:
    print('ATENÇÃO! Você está a {}KM/h, diminua a velocidade, você foi multado em {}'.format(vel, multa))
print('Dirija com cuidado, Boa Viajem!')

