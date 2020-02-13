try:
  import pandas as pd
except:
    print('The pandas library was not found! \n Try \'$pip3 install pandas\'')
try:
  import matplotlib.pyplot as plt
except:
    print('The matplotlib library was not found! \n Try \'$pip3 install matplotlib.\'')


try:
  df = pd.read_excel(r'./data.xlsx')
except:
  print('Problem reading the file: data.xlsx, you should install xlrd package ')

print(df)




#converting the data_type of the column 0 of the dataframe in to str.
for i in df.index:
  print(df.iloc[i,0])
  df.iloc[i,0] = str(df.iloc[i,0])


t_r_lista = list() # this is a temporal list to count the repetition

#passing each technology separated  
for i in df.index:
  for e in df.iloc[i,0].split(','):
    t_r_lista.append(e)

# erasing the repeat pattern and saving in a dataframe
df_tech = pd.DataFrame(list(dict.fromkeys(t_r_lista)))
df_tech['Count']= int() 


#counting the freq of repetition
for i in df_tech.index: 
  #print(df_tech.loc[i,0]) 
  #print(t_r_lista.count(df_tech.loc[i,0]) ) 
  df_tech.iloc[i,1]=int(t_r_lista.count(df_tech.loc[i,0])) #count each "Tech" ans allocate

print(df_tech)


df_tech = df_tech.set_index(0) # fix this... rename 0 by Technology

df_tech.plot(kind='bar')     #plot using bar
#plt.show()                   # to show in the screen
plt.savefig('./1.png')

df_tech.sort_values('Count').plot(kind='bar') #plot using bar but sorting before ascending 
plt.savefig('./2.png')




#exporting area. 'Just in case'
df.describe()
df.corr().to_csv('./corr.csv', sep='\t')
df.describe().transpose().to_csv('./describe.csv',sep='\t')


#df['Challenge Stats Technology List'] = df['Challenge Stats Technology List'].to_string() # una de estas dos lineas hace que se repita la info en cada celda
#df['Challenge Stats Technology List'] = df['Challenge Stats Technology List'].astype(str) #

#df['Challenge Stats Challenge Name'] = df['Challenge Stats Challenge Name'].astype(str)
#df['Challenge Stats Challenge Copilot'] = df['Challenge Stats Challenge Copilot'].astype(str)
#df['Challenge Stats Project Category Name'] = df['Challenge Stats Project Category Name'].astype(str)
#df['Challenge Stats Status Desc'] = df['Challenge Stats Status Desc'].astype(str)
#df['Challenge Stats Tco Track'] = df['Challenge Stats Tco Track'].astype(str)
