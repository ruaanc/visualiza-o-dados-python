import matplotlib.pyplot as plt 

x = [1, 2, 5]
y = [2, 3, 7]

plt.title("Meu primeiro gráfico com python")

#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x, y)
plt.show()
