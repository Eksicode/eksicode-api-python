import os


class AttrDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    @classmethod
    def from_data(cls, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = cls.from_data(value)
        return cls(**data)


def config(debug, cache={}):
    d = lambda _debug, _prod: _debug if debug else os.environ[_prod]
    if cache:
        return cache['config']
    else:
        cache['config'] = AttrDict.from_data(  # This is the actual configuration
            # The d functions' second parameter is the name of the alleged os.env variable to use on production
            {
                'DB': {
                    'name': d('eksicode', 'DB.name'),
                    'user': d('eksicode', 'DB.user'),
                    'password': d('eksicode', 'DB.password'),
                    'host': d('127.0.0.1', 'DB.host'),
                    'port': d('5432', 'DB.port'),
                },
                'SECRET_KEY': d('SECRET_KEY', 'SECRET_KEY')
            }
        )
        return cache['config']
