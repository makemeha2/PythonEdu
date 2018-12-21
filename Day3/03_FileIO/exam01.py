import sys

#input 유형 1
#print("welcome to", "python", sep="~", end="!", file=sys.stderr)

#input 유형 2
#print("http://www.credu.com/?page=" + str(0))

#input 유형 3
# f = open("C:\\examples\\Day3\\03_FileIO\\test.txt", "wt", encoding="UTF-8")
# f.write("한글로 데이터를 출력\nabcd\n")
# print("file write", file=f)
# f.close()

f = open("C:\\examples\\Day3\\03_FileIO\\test.txt", "r", encoding="UTF-8")
result = f.readlines()
for item in result:
    print(item.replace("\n", ""))
f.close()

f = open("C:\\examples\\Day3\\03_FileIO\\test.txt", "a+", encoding="UTF-8")
f.write("--첨부하기시작--\n한글로 데이터를 출력\nabcd\n--첨부하기끝--\n")
f.close()



