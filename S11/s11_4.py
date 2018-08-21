field_names = 'asdf,vds dasdf fsaf ,fsd vds'
try:
    field_names = field_names.replace(',', ' ').split()
except AttributeError as e:
    print(e)
print(field_names)
field_names = tuple(field_names)
print(field_names)
field_names = set(field_names)
print(field_names)