#coding:utf-8
word = 'word';
sentence = "sentence";
paragraph = """paragraph
    hhh """;

list_a = [1,2]
tuple_a = ('a','b')


a=1
b=1
if ( a > 0 ) or ( b / a > 2 ):
    print "yes"
else :
    print "no"

print word;
print sentence;
print paragraph;
print list_a;
print tuple_a;
# raw_input("\n\nPress the enter key to exit.")
import random;

create = random.randint(0,10)
print create

while 1:
    guess = input("guess 0 to 10：");
    print guess

    if int(guess) < create:
        print ('small')
    elif int(guess) > create:
        print ('large')
    elif int(guess) == create:
        print ('good')
        break
    pass
pass