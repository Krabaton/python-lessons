dom = {'div', 'span', 'ol'}

dom1 = set(['div', 'span', 'ol'])
dom1.add('li')
print(type(dom1))

# Объединение
dom4 = dom.union(dom1)
print(dom4)
print(dom.intersection(dom1))
print(dom1.difference(set(dom)))