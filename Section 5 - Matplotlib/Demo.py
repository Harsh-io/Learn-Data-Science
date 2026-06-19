#Homework/ Practice
import matplotlib.pyplot as plt
years = [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
Dhoni =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
Michal = [700, 500, 100, 200, 800, 1600, 1700, 1100, 1200, 1400]

plt.style.use('bmh')
plt.plot(years, kohli, color='orange',linestyle='--', label="Virat Kohli")
plt.plot(years, sehwag, color='green', linestyle='--', label="Virender Sehwag")
plt.plot(years, Dhoni, color='blue', linestyle='--', label="Dhoni")
plt.plot(years, Michal, color='red', linestyle='--', label="Michal")

plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Performance Comparison")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
