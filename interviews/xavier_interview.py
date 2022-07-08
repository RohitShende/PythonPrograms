# Task 1
#
# If  -
# For -
#
#
# """
#
# """
#
#
# Task 2
#
# '\{\{(?:name)\}\}'
#
#
# <h1> {{ title }} </h1>
# <h1> {{ title2 }} </h1>
# <h1> {{ title3 }} </h1>
#
# [
#     {name: title},
#     {name: title2},
#     {name: title3},
# ]
#
# dict_keys = {
#     "title": "Rohit",
#
# }

"""
<h1>{{ title }}</h1>
<span>{{ inner }}</span>
{% for outer in nested %}
<div>
    <h2>{{ outer.1 }}</h2>
    <ul>
        {% for inner in outer.1 %}
        <li>{{ inner }}</li>
        {% endfor %}
    </ul>
</div>
{% endfor %}
"""

ctx = {
    'title': 'Some title',
    'inner': 'Some value',
    'nested': [
        ('heading 1', [10, 11, 12]),
        ('heading 2', [20, 21, 22]),
    ],
    'nested2':
    [
        {'name':"Rohit"},
        {'name':"Xavier"}

    ]
}

def search_for_for_loops(template):
    body, interator_variable, list_of_values = "use regex to fetch the body of for loop"
    N = len(list_of_values)
    output = ''
    for i in range(N):
        body.replace(interator_variable, list_of_values.__name__+'.'+i)
