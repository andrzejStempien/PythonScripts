batRegex = re.compile('rBat(wo)*man')
mo1 = batRegex.search('Adventures of Batman')
mo1.group()
// 'Batman'

mo2.batRegex.search('The Adventures of Batwoman')
mo2.group()
// 'Batwoman'

mo3 =batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
// 'Batwowowowoman'

//matching zero or more with the star
