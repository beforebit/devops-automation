from flask import Flask, request
import yaml
import json
app = Flask(__name__)


@app.route("/devops")
def home_page():
    s_length = request.args.get("s_length")
    return str("Hello DevOps " + s_length)


def clear_value():
    with open('example.yaml') as f:
        doc = yaml.load(f)

    doc[0]['roles'] = []
    with open('example.yaml', 'w') as f:
       yaml.dump(doc, f)

def set_value(value):
    with open('example.yaml') as f:
        doc = yaml.load(f)

    if doc[0]['roles'] == None:
        doc[0]['roles'] = []

    doc[0]['roles'].append({'role': value})

    with open('example.yaml', 'w') as f:
       yaml.dump(doc, f)


@app.route("/json_file", methods=['POST'])
def json_file():
    clear_value()
    input_data=request.get_json("input")
    #
    # tasks_name= input_data[0]["tasks"]
    for item in input_data:
        # counter = 0
        arr = ['SCM', 'CI', 'DATABASE', 'APP']
        for key in arr:
            if key in item:
                for task in item[key]:
                    if item[key][task]:
                        set_value(task)


    return 'success'
if __name__=='__main__':
   app.run(port=8080)