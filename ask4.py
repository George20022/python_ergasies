import random

penctutions = ".,;?()[]{}&_-@%<>:!~1234567890/*+$#^/"
newt = ""   #text without penctutions
index = 0
List2 = [] #λιστα με τις τριαδες
List3 = [] #τελικη λιστα
text = str("Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.")

for char in text:
    if char not in penctutions:
        newt += char


List1 = newt.split()

for i in range(1):
    for j in range(len(List1)-2):
        List2.append([List1[j],List1[j+1],List1[j+2]])
        j+=1
    i += 1

random.shuffle(List2)

while len(List3) < 200:
    for i inr range(len(List2)):
        if List2[i][1],List2[i][2] == List2[i+1][0],List2[i+1][1]:
            List3.append(List2[i][1])
            List3.append(List2[i][2])

print(List3)







print(List2)
