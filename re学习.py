

import re
data='''

哀 āi

❶悲痛，伤心。屈原《离骚》：“～众芳之芜秽（huì）。”（芳：香草。芜秽：荒芜。） 父母之丧。《宋书·张敷传》：“居～毁灭，孝道淳至。”❷怜悯，同情。《韩非子·用人》：“忧悲不～怜。”【辨】哀，戚，悲，悼。四字都有悲伤的意思。但“戚”字一般是表示忧苦、悲哀；“哀”与“悲”有怜悯、同情的意思，“哀”的感情色彩要更重些；“悼”则是悲痛的意思，多用于对死者表示沉痛悼念。

'''.replace('\n', '')

x=data
x=re.sub(r'“.+?。”','。',x)
x=re.sub(r'（.+?）','',x)
x=x.replace('：','')
x='。'.join([i for i in x.split('。')
    if '《' not in i
           ])
print(x)
del x

x=re.findall(r'''[
⓿❶❷❸❹❺❻❼❽❾❿
⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴
].+?。.+?《'''.replace('\n',''),
             data)
print(x)








