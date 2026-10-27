import numpy as np
import random

n = 100000
scale1 = 0.3
scale2 = 0.6

rainStart = random.randint(int(n * 0.1), int(n * 0.8))
rainEnd = random.randint(rainStart + int(n * 0.1), int(n * 0.9))

print(rainStart, rainEnd)

sent = np.random.randint(0, 1000, n)

error = np.random.normal(scale=scale1, size=n).astype(int)
error2 = np.random.normal(scale=scale2, size=rainEnd - rainStart).astype(int)
error[rainStart : rainEnd] = error2
received = sent + error

with open("Übertragungskanal.csv", "w") as f:
    f.write("n;sent;received\n")
    for n, (s, r) in enumerate(zip(sent, received)):
        f.write(f"{n};{s};{r}\n")

# Diagramm
from matplotlib import pyplot as plt

bin_len = 1000

error = np.where(error != 0, 1, 0)
error = np.reshape(error, (-1, bin_len))
error = np.sum(error, axis=1) / bin_len
print(error)

plt.plot(error)
plt.ylabel("Fehlerwahrscheinlichkeit (verfälscht)")
plt.xlabel("Zeit im Experiment")
plt.show()
