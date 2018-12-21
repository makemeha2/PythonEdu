#정규식 연습
import re
# results = re.findall('[1-9]*th', '  11th\t12th\t13th\t')
# if results == None:
#     print("Nothing")
# else:
#     for item in results:
#         print(item)

result1 = re.sub("-", "", "820526-1042719") #주민등록번호 형식으로 변경
print(result1)

result2 = re.sub(r"[:,|\s]", ",", "Apple:Orange Banana|Tomato")
print(result2)

result3 = re.sub(r"\b(\d{4}-\d{4})\b", r"<I>\1</I>", "Copyright Derick 1990-2009")
print(result3)

result4 = re.sub(r"\b(?P<year>\d{4}-\d{4})\b", r"<I>\g<year></I>", "Copyright Derick 1990-2009")
print(result4)




