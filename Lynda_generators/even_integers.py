def main():
    n=20
    gen_result=[i for i in range(n) if i%2==0]    #items
    even_result = (i for i in range(n) if i % 2 == 0)   #generator
    integers=even_integers_generator(n)
    #print (integers)
    #print(integers.__next__())
    #print(integers.__next__())
    #print(integers.__next__())
    #print(integers.__next__())
    #print (gen_result)
    #print (even_integers(n))
    #print (even_integers_generator(n))
    #print (items(even_integers_generator(n)))
    #print (even_result)
    #print (items(even_result))
    print(fibo_seq(10))
    fib=fibo_seq_gen()
    for i in range(10):
        print (fib.__next__())



#function solution
def even_integers(n):
    result=[]
    for i in range(n):
        if i%2==0:
            result.append(i)
    return result


#generator solution
def even_integers_generator(n):
    for i in range(n):
        if i%2==0:
            yield i


def fibo_seq(n):
    result=[1,1]
    for i in range(2,n):
        result.append(result[-1]+result[-2])
    return result



def fibo_seq_gen():
    first,second=0,1
    while True:
        yield second
        first,second=second, first+second


if __name__=='__main__':
    main()