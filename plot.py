import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('istherecorrelation.csv', delimiter=';', decimal=',')

time = df['Year']
WO = df['WO [x1000]']
beer = df['NL Beer consumption [x1000 hectoliter]']
print(WO)

fig, ax1 = plt.subplots()
fig.set_size_inches(8, 4)

ax1.plot(time, WO*1000, 'b')
ax1.set_xlabel('Year')
ax1.set_ylabel('WO', color='blue')
ax1.set_yticks([2.2*1e5, 2.5*1e5, 2.8*1e5])
ax1.tick_params(axis='y', labelcolor='blue')
ax1.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

ax2 = ax1.twinx()
ax2.plot(time, beer, 'r')
ax2.set_ylabel('Beer consumption', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
ax2.set_yticks([1.15*1e4, 1.18*1e4, 1.21*1e4])
ax2.set_title('WO and Beer consumption in the Netherlands')

fig.savefig('Beer_correlation', dpi=300)
