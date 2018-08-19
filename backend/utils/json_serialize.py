import time


def obj_json_serialize(obj):
    obj.create_time = time.mktime(obj.create_time.timetuple()) * 1000
    obj.update_time = time.mktime(obj.update_time.timetuple()) * 1000
    obj.__dict__.pop('_sa_instance_state')
    return obj.__dict__


def list_json_serialize(list):
    result = []
    for element in list:
        result.append(obj_json_serialize(element))
    return result


