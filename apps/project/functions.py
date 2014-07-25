DATA = {
    'tissues': (('leg hand'), 
                ('hand leg'),
                ('knee eye '),
                ('kyeka dfasdf'),),

    'diseases': (('malaria fever'),
                 ('viral fever'),
                 ('typhiod '),
                 ('myophia '),)
}


"""
import json

def json_data(field, query):
    data = [query for query in Data[field] ]
    return json.dumps(data)

def json_data(field, query):
    data = []
    for q in Data[field]:
        if query.lower() in q.lower():
            data.append(q)
    return json.dumps(data)
"""
