from datetime import datetime, date
from decimal import Decimal
from fractions import Fraction


datatypes = {'fraction', 'decimal', 'complex', 'set', 'datetime', 'date'}


class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2



inst_class = MyClass('first_arg', 'second_arg')

complete_date_log = dict(
                datatype="datetime",
                iso=datetime.utcnow().isoformat(),
                date=datetime.utcnow().date().isoformat(),
                time=datetime.utcnow().time().isoformat(),
                year=datetime.utcnow().year,
                month=datetime.utcnow().month,
                day=datetime.utcnow().day,
                hour=datetime.utcnow().hour,
                minutes=datetime.utcnow().minute,
                seconds=datetime.utcnow().second
            )

dic_datetime_complex = {
        "datetime": {
            "_type": "datetime",
            "value": "2020-11-17T16:08:09.817444",
        },
        "date": {
            "_type": "date",
            "value": "2020-11-17"
        },
        "time": {
            "_type": "time",
            "value": "16:08:09.817444"
        },
        "year": {
            "_type": "year",
            "value": 2020
        },
        "month": {
            "_type": "month",
            "value": 11
        },
        "day": {
            "_type": "day",
            "value": 17
        },
        "hour": {
            "_type": "hour",
            "value": 16
        },
        "minutes": {
            "_type": "minutes",
            "value": 8
        },
        "seconds": {
            "_type": "seconds",
            "value": 9
        }
}


date_log = dict(date_=date(2020, 11, 16),
                date2=datetime(2030, 11, 16).year)


log_record = dict(time=datetime.utcnow(),
                  message='Created New point',
                  list=[1, 2, 3, 4],
                  myset={1, 2, 3},
                  my_complex=1+2j,
                  my_decimal=Decimal(0.5),
                  my_fraction=Fraction(1, 10))

all_data = dict(decimal_num=Decimal(10.5),
                fraction_num=Fraction(1,2),
                complex_num=1+2j,
                date_time=datetime.utcnow(),
                _date=date(2020, 11, 18),
                set_data={1, 2, 3, 4, 5},
                class_data=MyClass,
                inst_data=inst_class)

dict_schema = dict(decimal={'_type': 'decimal', 'value': Decimal(1.50), 'required': None},
                           fraction={'_type': 'fraction','value': Fraction(1, 2), 'required': None},
                           complex={'_type': 'complex','value': 2+2j, 'required': None},
                           datetime={'_type': 'datetime','value': datetime.utcnow().isoformat(), 'required': True},
                           date={'_type': 'date','value': date(3020, 11, 17), 'required': None},
                           _set={'_type': '_set', 'value': {1,2,3}, 'required': None}
                           )
# TODO check which kind of schema suits better this app
app_schema = dict(decimal={'_type': 'decimal', 'required': None},
                           fraction={'_type': 'fraction', 'required': None},
                           complex={'_type': 'complex', 'required': None},
                           datetime={'_type': 'datetime', 'required': True},
                           date={'_type': 'date', 'required': None},
                           _set={'_type': 'set', 'required': None}
                           )

schema_output_1 = {'decimal': {'_type': 'decimal', 'value': Decimal('1.5'), 'required': None},
                   'fraction': {'_type': 'fraction', 'value': Fraction(1, 2), 'required': None},
                   'complex': {'_type': 'complex', 'value': (2+2j), 'required': None},
                   'datetime': {'_type': 'datetime', 'value': datetime(2020, 11, 18, 4, 13, 7, 947272), 'required': True},
                   'date': {'_type': 'date', 'value': date(3020, 11, 17), 'required': None},
                   '_set': {'_type': '_set', 'value': {1, 2, 3}, 'required': None}}

schema_output_2 = {'decimal_num': {'_type': 'decimal', 'value': Decimal('10.5'), 'required': False},
                   'fraction_num': {'_type': 'fraction', 'value': Fraction(1, 2), 'required': False},
                   'complex_num': {'_type': 'complex', 'value': (1+2j), 'required': False},
                   'date_time': {'_type': 'datetime', 'value': datetime(2020, 11, 18, 17, 50, 40, 232856), 'required': True},
                   '_date': {'_type': 'date', 'value': date(2020, 11, 18), 'required': False},
                   'set_data': {'_type': 'complex', 'value': [1, 2, 3, 4, 5], 'required': False},
                   'class_data': {'_type': '_class', 'value': "<class 'dict_sample.MyClass'>", 'required': False},
                   'inst_data': {'_type': 'class_instance', 'value': "<dict_sample.MyClass object at 0x000001BBBBA437F0>",
                                 'required': False}}


