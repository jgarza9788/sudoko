import pandas as pd
import random 

def get_blank_board():
    '''
    returns a 9x9 Dataframe filled with None
    '''
    return pd.DataFrame(
        [
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None],
        ],
    )

def rand_to_bool(chance):
    r = random.randrange(0,1)

    if r <= chance:
        return True
    else:
        return False



def get_unsolved_board(fill_chance = 0.5):
    '''
    returns a 9x9 Dataframe with some filled in
    '''
    numbers = [1,2,3,4,5,6,7,8,9]
    rand_numbers = [1,2,3,4,5,6,7,8,9]
    random.shuffle(rand_numbers)

    print(rand_numbers)

    df = get_blank_board()

    n = rand_numbers.copy()
    for c in range(3,6,1):
        for r in range(3,6,1):
            # print(c,r)
            df.iat[c,r] = n.pop()
    
    



    # for col,column in enumerate(df):
    #     for row,value in enumerate(df[column]):
    #         print(col,row,value)
            

    # for index, row in df.iterrows():
    #     for c in row:
    #         c = 0

    return df

    # for index, row in df.iterrows():
        # print('index',type(index),index)
        # print('row',type(row),row)
        # print(df.at[index,row])
        # for c in row:
            # print(index,c)
        
        # print(index, row)
        # print(type(index), type(row))








if __name__ == "__main__":

    # print(get_blank_board())
    print(get_unsolved_board())

    # b = get_unsolved_board()