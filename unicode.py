''''programme for UNICODE
creator : Avijit Maity   '''
S='mumbai'
for i in S:              #loop for printing the Unicode point of each character in the string#
    print('the Unicode code of the character '+ i + ' is' ,ord(i))      #printing the Unicode character#
#  computing the sum of the Unicode code points of the character in string S  #
sum=0
for i in S:
    sum=sum+ord(i)
print("the sum of the Unicode code points of the characters in S : ",sum)  # printing the sum #
#list that contains all the Unicode code points of the string S  #
Unicodes=[]
for i in S:
    Unicodes.append(ord(i))    #appending the values of the Unicode code points in the list #
print(Unicodes)                 # printing the list #
#by list comprehension method #
UNICODES=[ord(i) for i in S]    #making the list #
print(UNICODES)                  # printing the list #
#by map class method#
def unicode(a):
    return(ord(a))
b=map(unicode,S)
print('list of the unicodes by map class=',list(b))