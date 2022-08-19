import os
import re
from typing import List, Dict

from werkzeug.exceptions import BadRequest

from constants import DATA_DIR


def do_cmd(cmd: str, value:  str, data: List[str]) -> List[str]:
    if cmd == 'filter':
        result: List[str] = list(filter(lambda record: value in record, data))
    elif cmd == 'map':
        col_num = int(value)
        result = list(map(lambda record: record.split()[col_num], data))
    elif cmd == 'unique':
        result = list(set(data))
    elif cmd == 'sort':
        reverse = value == 'desc'
        result = sorted(data, reverse=reverse)
    elif cmd == 'limit':
        result = data[:int(value)]
    elif cmd == 'regex':
        regex = re.compile(str(value))
        result = list(filter(lambda v: regex.search(v), data))
    else:
        raise BadRequest

    return result


def query(params: Dict[str, str]) -> list:
    with open(os.path.join(DATA_DIR, params['file_name'])) as f:
        file_data = f.readlines()

    res = file_data

    if 'cmd1' in params.keys():
        res = do_cmd(cmd=params['cmd1'], value=params['value1'], data=res)
    if 'cmd2' in params.keys():
        res = do_cmd(cmd=params['cmd2'], value=params['value2'], data=res)

    return res
