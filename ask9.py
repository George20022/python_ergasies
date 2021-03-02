import random

ordleatters=[ord(a),ord(b),ord(c),ord(d),ord(e),ord(f),ord(g),ord(h),ord(i),ord(j),ord(k),ord(l),ord(m),ord(n),ord(o),ord(p),ord(q),ord(r),ord(s),ord(t),ord(u),ord(v),ord(w),ord(x),ord(y),ord(z)]
leatters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
penctutions = ".,;?()[]{}&_-@%<>:!~1234567890/*+$#^/"
newt = ""   #text without penctutions
List1=[]
odds=[]
text = str("Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.")

for char in text:
    if char not in penctutions:
        newt += char


for char in newt:
    y = ord(char)
    List1.append(y)

for i in List1:
    if List1[i] % 2 == 1:
        odds.append(List1[i])

def freq(index,letters,text):
    count = 0
    for i in range(le(text)):
        if text[i] == letters[index]:
            count += 1
    return count

for k in range(len(letters)):
    freq(k,ordletters,odds)

    print(letters[k],':',count*'*')


print(odds)
