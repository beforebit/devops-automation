# install package PyYaml to read yaml file

import yaml


def set_value( value):
    with open('example.yaml') as f:
        doc = yaml.load(f)

        # print(doc[0]['roles'])

    print(doc[0]['roles'])
    doc[0]['roles'].append({'role': value})
    print(doc[0]['roles'])

    # if want to change something else
    #doc['classes']['nfs::server']['exports'][1] = 'hello_replace_with_anything'

    with open('example.yaml', 'w') as f:
       yaml.dump(doc, f)


set_value('shubham')

