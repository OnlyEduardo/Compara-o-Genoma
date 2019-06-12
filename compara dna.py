import os

entrada = open("16s_bacteria.fasta").read()
entrada2 = open("18s_human.fasta").read()

try:
	saida = open("saida_html.html", "r")
	saida.close()
	saida = open("saida_html.html", "w")
except FileNotFoundError:
	saida = open("saida_html.html", "w")

saida.write("<body background='background2.jpg'><br>")

counter = {}
counter2 = {}

entrada = entrada.replace("\n", "")
entrada = entrada.replace("N", "")
entrada2 = entrada2.replace("\n", "")
entrada2 = entrada2.replace("N", "")

def gera_pares(dict, entry):
	for i in ['A', 'T', 'C', 'G']:
		for j in ['A', 'T', 'C', 'G']:
			dict[i + j] = 0

	for y in range(len(entry) - 1):
		dict[entry[y] + entry[y + 1]] += 1

	return dict

counter = gera_pares(counter, entrada)
counter2 = gera_pares(counter2, entrada2)

saida.write("<div style='width:100px; height:100px; border:1px; float:left;'><font size='6' color='white'><b>"+ 'Bactéria:' +"</b></font></div>")
saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")
saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")
saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")
saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")

saida.write("<div style='width:100px; height:100px; border:1px; float:left;'><font size='6' color='white'><b>"+ 'Humano:' +"</b></font></div>")
saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")
saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")
saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")
saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")
saida.write("<div style='clear:both'><div>")

i = 1
vez = 1
for k in counter:
	transparencia = counter[k] / max(counter.values())

	saida.write("<div style='width:100px; height:100px; border:1px solid #111; float:left; background-color:rgba(0, 0, 0, " + str(transparencia) + "')><font color='yellow' size='4'><b>" + k + "</b></font></div>")

	if i % 4 == 0:
		saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")
		i += 1
		for l in counter2:
			transparencia2 = counter2[l] / max(counter2.values())
			saida.write("<div style='width:100px; height:100px; border:1px solid #111; float:left; background-color:rgba(0, 0, 0, " + str(transparencia2) + "')><font color='green' size='4'><b>" + l + "</b></font></div>")
			if i % 4 == 0:
				saida.write("<div style='width:100px; height:100px; border:1px; float:left;'></div>")
				if vez == 1:
					del(counter2['AA'])
					del(counter2['AT'])
					del(counter2['AC'])
					del(counter2['AG'])
					saida.write("<div style='clear:both'><div>")
					i += 1
					vez += 1
					break
				elif vez == 2:
					del(counter2['TA'])
					del(counter2['TT'])
					del(counter2['TC'])
					del(counter2['TG'])
					saida.write("<div style='clear:both'><div>")
					i += 1
					vez += 1
					break
				elif vez == 3:
					del(counter2['CA'])
					del(counter2['CT'])
					del(counter2['CC'])
					del(counter2['CG'])
					saida.write("<div style='clear:both'><div>")
					i += 1
					vez += 1
					break
				elif vez == 4:
					del(counter2['GA'])
					del(counter2['GT'])
					del(counter2['GC'])
					del(counter2['GG'])
					saida.write("<div style='clear:both'><div>")
					i += 1
					vez += 1
					break
			else:
				i += 1
	else:
		i += 1

saida.write("<br></body>")
saida.close()