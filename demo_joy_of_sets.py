#! /use/bin/env python3

# howto demo create, and grow, and shrink

marvel_fans = {'donald','naoki','chris','isla','grace'}
dc_fans = set()

dc_fans.add('donald')
dc_fans.add('tom')
dc_fans.add('andrius')

#dc_fans.pop()# randomly remove a value

comic_fans = dc_fans.copy()
comic_fans.clear()

print(f'fans of marvel = {marvel_fans}')
print(f'fans of ds = {dc_fans}')
print('-'*60)
print(f'fans of either marvel or dc ={marvel_fans.union(dc_fans)}')
print(f'fans of both marvel or dc ={marvel_fans.intersection(dc_fans)}')
print(f'fans of only marvel ={marvel_fans.difference(dc_fans)}')
print(f'fans of only marvel or dc ={marvel_fans.symmetric_difference(dc_fans)}')

print('-'*60)
print(f'fans of either marvel or dc ={marvel_fans | dc_fans}')
print(f'fans of both marvel or dc ={marvel_fans & dc_fans}')
print(f'fans of only marvel ={marvel_fans - dc_fans}')
print(f'fans of only marvel or dc ={marvel_fans ^ dc_fans}')