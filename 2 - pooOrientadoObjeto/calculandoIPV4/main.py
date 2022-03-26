from calcIPV4.classes import CalcIPv4

calc_ipv4 = CalcIPv4(ip='192.168.0.1', mascara='255.255.255.0')
calc2_ipv4 = CalcIPv4(ip='192.168.0.1', prefixo=24)

# Com Máscara
print(f'IP: {calc_ipv4.ip}')
print(f'Máscara: {calc_ipv4.mascara}')
print(f'Rede: {calc_ipv4.rede}')
print(f'Broadcast: {calc_ipv4.broadcast}')
print(f'Prefixo: {calc_ipv4.prefixo}')
print(f'Número de IPs da rede: {calc_ipv4.getNumeroIps()}')
print()
print()

# Com Prefixo
print(f'IP: {calc2_ipv4.ip}')
print(f'Máscara: {calc2_ipv4.mascara}')
print(f'Rede: {calc2_ipv4.rede}')
print(f'Broadcast: {calc2_ipv4.broadcast}')
print(f'Prefixo: {calc2_ipv4.prefixo}')
print(f'Número de IPs da rede: {calc2_ipv4.getNumeroIps()}')
