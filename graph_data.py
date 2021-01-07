import sqlite3 
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import webbrowser

conn = sqlite3.connect('DHT_DB.db')
c = conn.cursor()  

c.execute('SELECT * FROM Data')


hum_list = []
temp_list = []
time_stamp_list = [] 

for row in c.fetchall(): 
	hum = row[0] 
	temp = row[1] 
	time_stamp = row[2]

	hum_list.append(hum)
	temp_list.append(temp)
	time_stamp_list.append(time_stamp) 


hum_min = []
hum_max = []
temp_min = []
temp_max = []
max_min_time_stamp = [] 
hum_data = []
temp_data = []
time_stamp_data = []
i = 0

c.execute('SELECT * FROM Data')

for row in c.fetchall(): 
	hum = row[0] 
	temp = row[1] 
	time_stamp = row[2]

	hum_data.append(hum)
	temp_data.append(temp)
	time_stamp_data.append(time_stamp) 

	if(i==20):
		hum_min.append(min(hum_data))
		hum_max.append(max(hum_data))
		hum_data = []
		temp_min.append(min(temp_data))
		temp_max.append(max(temp_data))
		temp_data = []
		max_min_time_stamp.append(time_stamp)

		i = 0 

	i+=1 


app = dash.Dash() 

app.layout = html.Div(children=[
	html.H1('DHT Dashboard', 
		    style = {'font-size' : '100px', 
		             'text-align' : 'center', 
		             'font-family' : 'Courier New'}),
	dcc.Graph(id='Hum_Data', 
		      style = {'display' : 'inline-block', 
		               'width' : '50%'}, 
		figure = {
			'data' : [{'x' : time_stamp_list, 
					   'y' : hum_list, 
					   'type' : 'line', 
					   'name' : 'Humedad', 
					   'line':dict(color='bleu de france')}],
			'layout' : {
				'title' : 'Humedad', 
				'xaxis' : {'title' : 'Tiempo'}, 
				'yaxis' : {'title' : 'Humedad'}
			} 
		
		}
	), 
	dcc.Graph(id='Temp_Data', 
		      style = {'display' : 'inline-block', 
		               'width' : '50%'}, 
		figure = {
			'data' : [{'x' : time_stamp_list, 
					   'y' : temp_list, 
					   'type' : 'line', 
					   'name' : 'Temperatura', 
					   'line':dict(color='coral')}],
			'layout' : {
				'title' : 'Temperatura', 
				'xaxis' : {'title' : 'Tiempo'}, 
				'yaxis' : {'title' : 'Temperatura'}
			} 
		
		}
	), 
	dcc.Graph(id='hum_temp_max', 
		      style = {'display' : 'inline-block', 
		               'width' : '50%'}, 
		figure = {
			'data' : [{'x' : max_min_time_stamp, 
			           'y' : hum_max, 
			           'type' : 'bar', 
			           'name' : 'Humedad', 
			           'marker' : dict(color='bleu de france')},
					  {'x' : max_min_time_stamp, 
					   'y' : temp_max, 
					   'type' : 'bar', 
					   'name' : 'Temperatura', 
					   'marker' : dict(color='coral')}],
			'layout' : {
				'title' : 'Máximos de Temperatura y Humedad'
			} 
		
		}
	),  
	dcc.Graph(id='hum_temp_min', 
		      style = {'display' : 'inline-block', 
		               'width' : '50%'}, 
		figure = {
			'data' : [{'x' : max_min_time_stamp, 
					   'y' : hum_min, 
					   'type' : 'bar', 
					   'name' : 'Humedad', 
					   'marker' : dict(color='bleu de france')},
					  {'x' : max_min_time_stamp, 
					   'y' : temp_min, 
					   'type' : 'bar', 
					   'name' : 'Temperatura', 
					   'marker' : dict(color='coral')}],
			'layout' : {
				'title' : 'Mínimos de Temperatura y Humedad'
			} 
		
		}
	),
	dcc.Graph(id='DHT_Data', 
		figure = {
			'data' : [{'x' : time_stamp, 
			           'y' : hum_list, 
			           'type' : 'line', 
			           'name' : 'Humedad', 
			           'line' : dict(color='bleu de france')},
					  {'x' : time_stamp_list, 
					   'y' : temp_list, 
					   'type' : 'line', 
					   'name' : 'Temperatura', 
					   'line' : dict(color='coral')}],
			'layout' : {
				'title' : 'DHT'
			} 
		
		}
	),
	html.H1('Creado por Sebastián Aliaga, Nicolás Benavides, Hernán Berrazueta', 
			style = {'text-align' : 'center', 
					 'font-family' : 'Courier New', 
					 'font-size' : '20px'
					}
		   )

	

]) 

if __name__ == '__main__':
	webbrowser.open("http://127.0.0.1:8050/")
	app.run_server(debug=True)
