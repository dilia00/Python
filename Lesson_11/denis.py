import matplotlib.pyplot as plt

# # Задача 1.
# def trendMean(list_):
#     a = list_[-1]
#     b = list_[0]
#     c = len(list_)-1
#     return (a - b) / c


# firstComp = [1743, 1648, 1650, 1622, 1581, 1490]
# secondComp = [743, 648, 711, 780, 805, 846]


# firstMean = trendMean(firstComp)
# secondMean = trendMean(secondComp)

# period = 10
# for i in range(period):
#     firstComp.append(firstComp[-1] + firstMean)
#     secondComp.append(secondComp[-1] + secondMean)

# plt.plot(firstComp)
# plt.plot(secondComp)
# plt.show()


# # Задача 2
# n = [4, 6, 10, 4, 2, 8, 10, 7, 1, 5]
# a = [3, 3, 10, 5, 10, 10, 4, 3, 6, 1]
# p = [2, 2, 1, 1, 3, 7, 9, 9, 2, 8]

# max_value = 10
# n_invert = list(max_value - i for i in n)
# a_invert = list(max_value - i for i in a)
# p_invert = list(max_value - i for i in p)

# ax = plt.subplot(131, polar=True)
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_ticks([0, 2, 4, 6, 8, 10])
# ax.get_yaxis().set_ticklabels(['10', '8', '6', '4', '2', '0'])
# plt.plot(n_invert, 'ro')

# ax = plt.subplot(132, projection='polar')
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_ticks([0, 2, 4, 6, 8, 10])
# ax.get_yaxis().set_ticklabels(['10', '8', '6', '4', '2', '0'])
# plt.plot(a_invert, 'bo')

# ax = plt.subplot(133, polar=True)
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_ticks([0, 2, 4, 6, 8, 10])
# ax.get_yaxis().set_ticklabels(['10', '8', '6', '4', '2', '0'])
# plt.plot(p_invert, 'go')
# plt.show()


# Задача 3.
x = [120, 205]


plt.title("Зависимость спроса от количества сахара")
ax = plt.subplot(211)
plot1 = list(5500 for i in range(0, 7))
line, = plt.plot(plot1)
line.set_label("требуемый спрос")
ax.legend()
people = list(x[0]*a*a + 3000 for a in range(0, 7))
line, = plt.plot(people)
line.set_label("прогнозируемый спрос")
ax.legend()


ax = plt.subplot(212)
plot2 = list(6500 for i in range(0, 7))
line, = plt.plot(plot2)
line.set_label("требуемый спрос")
ax.legend()
people = list(x[1]*a*a + 3000 for a in range(0, 7))
line, = plt.plot(people)
line.set_label("прогнозируемый спрос")
ax.legend()


plt.xlabel("Количество сахара")
plt.ylabel("Спрос")
plt.show()
