import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"   #윈도우는Malgun Gothic, 맥은 AppleGothic

prices = [15000, 20000, 10000, 80000, 5000]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)
for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points", xytext=(0, 8), ha="center")

ax.set_title("일일 소비금액 변화")
fig.savefig("my_first_chart.png")