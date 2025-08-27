# Operador E (and)
saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite

# Operador OU (or)
saldo = 1000
saque = 200
limite = 100
saldo >= saque or saque <= limite

# Operador Negação
contatos_emergencia = [ ]
not 1000 > 1500

not contatos_emergencia

not "saque 1500;"

not " "

# Parênteses
saldo = 1000
saque = 250
limite = 200

conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

#OBS:  AND para ser True todos tem que ser True
    #  OR para ser True apanas um tem que ser True