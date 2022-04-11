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


def get_row_list(df,row):
    return df[row].to_list()

def get_col_list(df,col):
    result = []
    for i in range(0,9,1):
        result.append(df.iat[col,i])
    return result

def sum_of_section(df,r1,r2,c1,c2):
    print(df.iloc[r1:r2,c1:c2])
    return df.iloc[r1:r2,c1:c2].sum().sum()


def section_to_rows_and_columns(section_num):
    result = {'r':[0,0],'c':[0,0]}

    if section_num in [0,3,6]:
        result['r'] = [0,3]
    elif section_num in [1,4,7]:
        result['r'] = [3,6]
    elif section_num in [2,5,8]:
        result['r'] = [6,9]

    if section_num in [0,1,2]:
        result['c'] = [0,3]
    elif section_num in [3,4,5]:
        result['c'] = [3,6]
    elif section_num in [6,7,8]:
        result['c'] = [6,9]

    return result


def test(row_list,col_list,num):

    if num not in row_list:
        if num not in col_list:
            return True
        else:
            return False
    else:
        return False


def place_numbers(df,section_num,numbers):
    rc = section_to_rows_and_columns(section_num)

    c = rc['c']
    r = rc['r']

    for row in range(r[0],r[1]):
        for col in range(c[0],c[1]):
            for index,n in enumerate(numbers):
                rl = get_row_list(df,row)
                cl = get_col_list(df,col)
                t = test(rl,cl,n)
                print('section_num',section_num)
                print(n)
                print('row',rl,row)
                print('col',cl,col)
                print(t)
                # if test(get_row_list(df,row),get_col_list(df,col),n):
                if t:
                    df.iat[col,row] = n
                    del numbers[index]
                    break
    return df
                


def get_unsolved_board(fill_chance = 0.5):
    '''
    returns a 9x9 Dataframe with some filled in
    '''
    numbers = [1,2,3,4,5,6,7,8,9]
    # rand_numbers = [1,2,3,4,5,6,7,8,9]
    # print(rand_numbers)

    df = get_blank_board()

    sections = []
    for i in range(0,9,1):
        random.shuffle(numbers)
        rn = numbers.copy()
        sections.append(rn)
    

    order_sections = [4,0,8,2,6,7,1,3,5]
    for index,s in enumerate(order_sections):
        print(index,s,sections[s])
        df = place_numbers(df,s,sections[s])
        print(df)

    # for index,s in enumerate(sections):
    #     print(index,s)
    #     df = place_numbers(df,index,s)
    #     print(df)





    # df = place_numbers(df,4,sections[4])
    # print(df)

    # df = place_numbers(df,0,sections[0])
    # print(df)

    # df = place_numbers(df,8,sections[8])
    # print(df)


    


    # random.shuffle(rand_numbers)
    # n = rand_numbers.copy()
    # for c in range(3,6,1):
    #     for r in range(3,6,1):
    #         # print(c,r)
    #         df.iat[c,r] = n.pop()

    # random.shuffle(rand_numbers)
    # n = rand_numbers.copy()
    # for c in range(0,3,1):
    #     for r in range(0,3,1):
    #         # print(c,r)
    #         df.iat[c,r] = n.pop()

    # random.shuffle(rand_numbers)
    # n = rand_numbers.copy()
    # for c in range(6,9,1):
    #     for r in range(6,9,1):
    #         # print(c,r)
    #         df.iat[c,r] = n.pop()
    
    # print(get_column(df,3))
    # print(get_row(df,3))
    # print(sum_of_section(df,0,3,0,3))
    # print(sum_of_section(df,0,3,6,6))
    



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