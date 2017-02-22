import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#Cell

y_data = pd.read_csv('responses.csv')
#Cell

y_data.head()
#Cell

f_data = y_data[y_data['Gender'] == 'female']
f_data.shape
#Cell

m_data = y_data[y_data['Gender'] == 'male']
m_data.shape
#Cell

f_data.plot(y = 'Height')
plt.show()
#Cell

It looks like someone's height is an outlier. Lets take a look at this height
#Markdown

f_data['Height'].min()
#Cell

It seems like someone's height is 62cm. This is probably a mistake. We will assume it is 162cm and change this height to 162cm.
#Markdown

f_data.loc[f_data[f_data['Height'] == f_data['Height'].min()].index.tolist(),'Height'] = 162.0
#Cell


bins = np.linspace(140, 210, 60)

plt.hist(f_data['Height'].tolist(), bins, range=(bins.min(), bins.max()), alpha = 0.7, label = 'Female')
plt.hist(m_data['Height'].tolist(), bins, range=(bins.min(), bins.max()), alpha = 0.7, label = 'Male')
plt.legend(loc = 'upper right')
plt.xlabel('Height (cm)')
plt.ylabel('Frequency of Height')
plt.title('Height Frequency between Male and Female')
plt.show()
#Cell


