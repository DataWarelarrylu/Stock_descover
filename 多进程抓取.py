from multiprocessing import Pool
def main(i):
    print(i)
if __name__ == '__main__':
    a =[1,2,3,4,5,6,7,8,9,10]
    pool = Pool ()
    pool.map(main,a)
