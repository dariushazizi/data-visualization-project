# import required packages 
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'
from die_module import Die

#creating random values
lucky = Die()
lucks = lucky.roll(10000)
print(f'results of rolling a die for {lucky.rolls_number} times')

# analyze the results
freqs = []
POSS_results = range(1,lucky.sides+1)
for value in POSS_results:
    freq = lucks.count(value)
    freqs.append(freq)
    print(f'the counts for {value} is {freq}')
    
# print counting result
print(freqs)

# visualize the result
title = f'results of rolling a die for {lucky.rolls_number} times'
labels = {'x': 'Die Side', 'y': 'Count of Sides in rolls'}
fig = px.line(x=POSS_results, y=freqs, title=title, labels=labels)
fig.show()

#roll two dies
rolling_number = 100000
ddie_result = []
for i in range(rolling_number):
    final_die = 0
    die = lucky.roll(2)
    for result in die:
        final_die += result
    ddie_result.append(final_die)
    
# analyze the results of double dies (ddie)
ddie_freqs = []
ddie_POSS_results = range(2,(lucky.sides*2)+1)
for ddie_value in ddie_POSS_results:
    ddie_freq = ddie_result.count(ddie_value)
    ddie_freqs.append(ddie_freq)
    print(f'the counts for {ddie_value} is {ddie_freq}')
    
# visualize the result of ddie
ddie_title = f'results of rolling double dies for {rolling_number} times'
ddie_labels = {'x': 'Die Side', 'y': 'Count of Sides in rolls'}
ddie_fig = px.line(x=ddie_POSS_results, y=ddie_freqs, title=ddie_title, labels=ddie_labels)
# Further customize chart.
fig.update_layout(xaxis_dtick=1)
ddie_fig.show()
