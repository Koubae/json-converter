json_datetime_complex = '''

{
  "datetime": {
    "_type": "datetime",
    "value": "2020-11-17T16:08:09.817444"
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

'''

json_schema_ok = '''

    {
      "decimal": {
        "_type": "decimal",
        "value": "Decimal(1.5)",
        "required": null
      },
      "fraction": {
        "_type": "fraction",
        "value": "Fraction(1, 2)",
        "required": null
      },
      "complex": {
        "_type": "complex",
        "value": "complex(2+2j)",
        "required": null
      },
      "datetime": {
        "_type": "datetime",
        "value": "2020-11-18T04:13:07.947272",
        "required": true
      },
      "date": {
        "_type": "date",
        "value": [
          3020,
          11,
          17
        ],
        "required": null
      },
      "_set": {
        "_type": "_set",
        "value": [
          1,
          2,
          3
        ],
        "required": null
      }
    }

'''

json_schema_with_class = '''

    {
      "decimal_num": {
        "_type": "decimal",
        "value": "Decimal(10.5)",
        "required": false
      },
      "fraction_num": {
        "_type": "fraction",
        "value": "Fraction(1, 2)",
        "required": false
      },
      "complex_num": {
        "_type": "complex",
        "value": "complex(1+2j)",
        "required": false
      },
      "date_time": {
        "_type": "datetime",
        "value": "2020-11-18T17:50:40.232856",
        "required": true
      },
      "_date": {
        "_type": "date",
        "value": [
          2020,
          11,
          18
        ],
        "required": false
      },
      "set_data": {
        "_type": "complex",
        "value": [
          1,
          2,
          3,
          4,
          5
        ],
        "required": false
      },
      "class_data": {
        "_type": "_class",
        "value": "MyClass",
        "required": false
      },
      "inst_data": {
        "_type": "class_instance",
        "value": "MyClass('first_arg', 'second_arg')",
        "required": false
      }
    }

'''
