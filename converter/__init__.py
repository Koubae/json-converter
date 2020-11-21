from .json_converter import (json_serializer,
                            JSONDecodeError,
                            schema_struct,
                            MainEncoder,
                            MainDecoder, 
                            json)


def Encoder(data):
    return json.dumps(data, cls=MainEncoder, make_schema=True) 


def Decoder(data):
    return json.loads(data, cls=MainDecoder)


__all__ = [JSONDecodeError, Encoder, Decoder]