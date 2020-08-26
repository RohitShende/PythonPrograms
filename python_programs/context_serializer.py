from python_programs import context
import pickle
import types
import json
import logging
import os


def serialize_context():
    all_attributes = dir(context)
    variable_attributes = {}

    for attr in all_attributes:
        attr_val = getattr(context, attr)
        if not attr.startswith('_') and not isinstance(attr_val, types.FunctionType)\
                and not isinstance(attr_val, types.ModuleType)\
                and not isinstance(attr_val, type):
            if any([isinstance(attr_val, x) for x in [logging.Logger, context.Monitor]]):
                attr_val = pickle.dumps(attr_val, 0).decode()

            variable_attributes[attr] = attr_val

    print(len(variable_attributes))
    print(*((i, type(getattr(context, i))) for i in variable_attributes), sep='\n')

    with open(context_serialize_file, 'w') as f:
        json_str = json.dumps(variable_attributes)
        f.write(json_str)
        print(f'Context serialized and written to {context_serialize_file} successfully')


def deserialize_context():
    variable_attributes = {}
    if os.path.exists(context_serialize_file):
        with open(context_serialize_file) as f:
            variable_attributes = json.load(f)
        for key, val in variable_attributes.items():
            try:
                val = pickle.loads(val.encode())
            except Exception as e:
                print(key, e)

            setattr(context, key, val)
        print('Context deserialized and copied to context.py')
    else:
        print(f'Context serialized file {context_serialize_file} not present')


context_serialize_file = 'serialized_context.json'


if __name__ == '__main__':
    serialize_context()
    deserialize_context()
    print(context.monitor)
    print(context.monitor_logger)
