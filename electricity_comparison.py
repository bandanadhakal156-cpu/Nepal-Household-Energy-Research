import matplotlib.pyplot as plt

# Results from the 2026 household energy survey
locations = ["Ratnanagar", "Khairahani"]
percentages = [10.9, 24.0]

plt.figure(figsize=(8, 5))

plt.bar(locations, percentages, color=["steelblue", "seagreen"])

plt.title("Electricity in the Cooking-Fuel Mix")
plt.xlabel("Study Location")
plt.ylabel("Households (%)")
plt.ylim(0, 30)

for i, value in enumerate(percentages):
plt.text(i, value + 0.5, f"{value}%", ha="center")

plt.tight_layout()
plt.savefig("electricity_comparison.png", dpi=300)
plt.show()
