import json
import inspect

from functools import singledispatch
from datetime import datetime, date
from decimal import Decimal
from fractions import Fraction


JSONDecodeError = json.decoder.JSONDecodeError


def schema_struct(_type, value, required=False):
    return {'_type': _type, 'value': value, 'required': required}


@singledispatch
def json_serializer(arg, schema_flag=None):

    try:
        if inspect.isclass(arg):  # or isinstance(arg, type)
            value = arg.__name__  # Set value as name of class, to desirial use eval()
            _type = '_class'
        else:
            inst_arg = list(vars(arg).values())
            value = f'{arg.__class__.__name__}{tuple(inst_arg)}'
            _type = 'class_instance'
        if schema_flag:
            struct = schema_struct(_type, value, required=False)
            return struct
        return value
        # Check if is a Class or Instance of a Class
    except TypeError:
        return str(arg)


@json_serializer.register(datetime)
def _(arg, schema_flag=None):
    value = arg.isoformat()
    if schema_flag:
        struct = schema_struct('datetime', value, required=True)
        return struct
    return value


@json_serializer.register(date)
def _(arg, schema_flag=None):
    value = [int(item) for item in str(arg).split('-')]
    if schema_flag:
        struct = schema_struct('date', value, required=False)
        return struct
    return value


@json_serializer.register(set)
def _(arg, schema_flag=None):
    value = list(arg)
    if schema_flag:
        struct = schema_struct('complex', value, required=False)
        return struct
    return value


@json_serializer.register(Decimal)
def _(arg, schema_flag=None):
    value = f'Decimal({str(arg)})'
    if schema_flag:
        struct = schema_struct('decimal', value, required=False)
        return struct
    return value


@json_serializer.register(complex)
def _(arg, schema_flag=None):
    value = f'complex{arg}'
    if schema_flag:
        struct = schema_struct('complex', value, required=False)
        return struct
    return value


@json_serializer.register(Fraction)
def _(arg, schema_flag=None):
    value = f'Fraction{int(arg.numerator), int(arg.denominator)}'
    if schema_flag:
        struct = schema_struct('fraction', value, required=False)
        return struct
    return value


class MainEncoder(json.JSONEncoder):
    def __init__(self, *args,  **kwargs):
        super().__init__(skipkeys=False, ensure_ascii=True,
                         check_circular=True, allow_nan=True,
                         sort_keys=False, indent=2, separators=None,
                         default=None)
        self.args = args
        self.kwargs = kwargs
        self.schema_flag = True if kwargs.get('make_schema', None) else False

    def default(self, arg):

        try:
            return json_serializer(arg, self.schema_flag)
        except TypeError as err:
            print('==='*15 + '\n' + 'ERROR' + '\n' + '==='*15)
            print(err)
            return super().default(arg)

    def _schema_flag(self):
        if self.schema_flag:
            return


@singledispatch
def json_deserializer(arg):
    return arg

#TODO check how to implement singledispatch with decoding
@json_deserializer.register(datetime)
def _(obj): ...


class MainDecoder(json.JSONDecoder):

    date_time_map = {'date', 'datetime', 'day', 'hour', 'minutes', 'month', 'seconds', 'time', 'year'}
    num_type_data = {'fraction', 'decimal', 'complex'}

    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook,strict=False, *args, **kwargs)

    def object_hook(self, obj):
        if '_type' not in obj:
            return obj
        get_type = obj['_type']
        if get_type in self.date_time_map: # check if _type is a datetime type
            obj['value'] = self.date_deserialize(obj['value'], get_type)
        elif get_type in self.num_type_data:  # Checks for fractions, decimal and complex
            try:
                obj['value'] = self.eva_data(str(obj['value']))
            except ValueError as err:
                print('object_hook ---> in num_type_data eval', err)
        elif get_type == '_set':
            obj['value'] = set(obj['value'])
        elif get_type == "_class" or get_type == "class_instance":
            obj['value'] = obj['value']  # eval(obj['value'])
        return obj

    @staticmethod
    def eva_data(obj):
        """Eval fractions, Decimals and complex num types"""
        return eval(obj)

    @staticmethod
    def date_deserialize(obj, _type):

        # TODO deserialize date with other format types, for instance 2020/11/17
        if _type == 'date':
            try:
                if isinstance(obj, list):  # Date can be [2020, 11, 17] or '2020-11-17)
                    obj = date(*[int(item) for item in obj])
                else:
                    obj = date(*[int(item) for item in obj.split('-')])
            except ValueError as err:
                print('data_serialize -- data', err)

        elif _type == 'datetime':
            try:
                obj = datetime.strptime(str(obj), '%Y-%m-%d %H:%M:%S')
            except ValueError as err:
                try:
                    obj = datetime.fromisoformat(str(obj))
                except ValueError as err:
                    print('data_serialize -- datatime', err)
        return obj

