from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    headers = { 'key': "66172e0d2280ae21f4e6e9ebd5e23dc5",
    'content-type': "application/x-www-form-urlencoded" }

    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        berat = request.form['weight']
        weight_convert = int(str(berat) + '000')
        weight = weight_convert
        courier = request.form['courier']
        
        payload  = "origin={}&destination={}&weight={}&courier={}".format(origin,destination,weight,courier)

        r = requests.post('https://api.rajaongkir.com/starter/cost/', payload, headers=headers)

        data = r.json()
        
        return render_template('stats.html', data=data, weight=berat,courier=courier)

    r = requests.get('https://api.rajaongkir.com/starter/city', headers=headers)

    data = r.json()

    # for key,value in data.items():
    #     for v in value['results']:
    #         print(v['province_id'],v['province'])
    return render_template('index.html', data=data)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 