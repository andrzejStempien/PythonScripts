batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
// 'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
// 'Batwoman'


// optional matching with question mark
