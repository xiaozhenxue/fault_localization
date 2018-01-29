

def read_file(file_name):
    target = open(file_name, 'r')
    text = target.read()
    target.close()
    return text


def covert_to_number(str):
    try:
        return int(str)
    except Exception:
        return -1
