from converter.json_converter import json_serializer, MainEncoder, MainDecoder
import inspect
import json
from converter import dict_sample, json_sample
import unittest
from datetime import datetime
from converter.dict_sample import MyClass, inst_class
import ast


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)


class TestSerializer(unittest.TestCase):

    def test_serialize(self):
        test_js = dict_sample.log_record
        test_ser = json.dumps(test_js, default=json_serializer, indent=2)
        self.assertTrue(test_ser)

    def test_encoder(self):

        test_js2 = dict_sample.log_record
        test_ser2 = json.dumps(test_js2, cls=MainEncoder)
        test_date = json.dumps(dict_sample.complete_date_log, cls=MainEncoder, schema=True, sort_keys=True)
        test_date = json.dumps(dict_sample.all_data, cls=MainEncoder, make_schema=True)
        test_date2 = json.dumps(dict_sample.date_log, cls=MainEncoder)
        self.assertTrue(test_ser2)
        self.assertTrue(test_date)
        self.assertTrue(test_date2)
        test_schema = json.dumps(dict_sample.dict_schema, cls=MainEncoder)
        self.assertTrue(test_schema)


    def test_class(self):
        self.assertTrue(inspect.isclass(MyClass))
        self.assertFalse(inspect.isclass(inst_class))

    def test_decode(self):
        def custom_decoder(arg):
            if 'objecttype' in arg and arg.get('objecttype', None) == 'datetime':
                return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
            else:
                return arg

        def obj_pais_hook(arg):
            return arg

        def obj_hook(arg):
            return arg

        weird_json = '{"x": 1, "x": 2, "x": 3}'
        self.assertTrue(json.loads(weird_json, object_pairs_hook=obj_pais_hook))

    def test_MainDecoder(self):
        self.assertTrue(json.loads(json_sample.json_datetime_complex, cls=MainDecoder))
        test_data_json = json.loads(json_sample.json_schema_ok, cls=MainDecoder)
        for i in test_data_json:
            for x in test_data_json[i]:
                if str(type(test_data_json[i][x]).__name__).lower() in dict_sample.datatypes:
                    self.assertIn(str(type(test_data_json[i][x]).__name__).lower(), dict_sample.datatypes)
        x = json.loads(json_sample.json_schema_with_class, cls=MainDecoder)

    # TODO Issue with the browser response User insert a Dictionary, returning a string (Not a JSON Object).
    # TODO Need to convert a Stringed Dict back to a dict and be able to then Jsonify it.
    def test_client_object(self):

        my_string =  "{'decimal_num': Decimal(10.5), 'fraction_num': Fraction(1, 2), 'complex_num': (1+2j), 'date_time': datetime(2020, 11, 21, 7, 3, 2, 582724), '_date': date(2020, 11, 18), 'set_data': {1, 2, 3, 4, 5}}"
        s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
        my_string = my_string.replace("'", '"')
        it = iter(my_string)
        print(next(it))
        l = []
        for i in it:
            l.append(i)
        z = ''.join(l[:-1])
        print(z)
        print(z.split(' '))
        f = [(i, v) for i, v in enumerate(z)]
        print(f)
        # d = my_string.split(':')
        # d_ = ''.join(d)
        # d_ = d_.strip('{')
        # d_ = d_.strip('}')
        # print(d_)
        # d_ = d_.split()
        # print(d_)
        # for i in d_:
        #     print(i)
        # f = [(i, v) for i,v in enumerate(d)]
        # l = []
        # s = []
        # for i in f:
        #     print(i)
        #     if i[0]%2 != 0:
        #         print(i[1])
        #         l.append(i[1])
        #     else:
        #         s.append(i[1])
        # print(l)
        # print(s)
        # d_ = dict(zip(l,s))
        # print(list(zip(l,s))[0])
        # # print(dict.fromkeys(d))


if __name__ == '__main__':
    run_tests(TestSerializer)
