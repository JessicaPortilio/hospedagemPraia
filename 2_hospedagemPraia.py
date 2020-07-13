def calcularHospedagem(hospedagem, dias):
    valorTotal = 0.0
    if (hospedagem == "individual") or (hospedagem == "Individual"):
        valorTotal = dias * 125
    elif hospedagem == "suíte Dupla":
        valorTotal = dias * 140
    elif hospedagem == "Suíte tripla":
        valorTotal = dias * 180
    if dias >= 3:
        valorTotal = valorTotal - valorTotal * 0.15
    return valorTotal


tipoHospedagem = input()
totalDias = int(input())
aPagar = calcularHospedagem(tipoHospedagem, totalDias)
print(f"{aPagar:.2f}")