import path
a = path.Path('G:\python\BaiVeNha\log.txt','log.txt')
b = path.Path('G:\python\dcl\.gitignore','.gitignore')
c = path.Path('G:\python\BaiVeNha\README.md','README.md')
a.write_to_file('path.json')
b.write_to_file('path.json')
c.write_to_file('path.json')