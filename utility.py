

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

    
def write_file(str, file_name):
    text_file = open(file_name, "w")
    text_file.write(str)
    text_file.close()   
