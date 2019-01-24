import redis as redis
from tabulate import tabulate

redis_host = "localhost"
redis_port = 6379
redis_password = ""

def hello_redis():
    try:
        redis_data = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        input_string = 'word'
        i = 1
        word_result = """\
        Please select a work format of the system as yoy want.
            1.If you want to add data on the system,Please input 'Add'
            2.If you want to remove data on the system,Please input 'Delete'
            3.If you want to view all data of the system,Please input 'Show'
            4.When yor want exit from add and delete data,Please input 'Exit'
        """
        print(word_result)
        while input_string != None:
            msg_select_task = input("What do you do? ")
            if msg_select_task == 'Add':
                while msg_select_task != '':
                    get_key = input("Key:")
                    if get_key != '':
                        redis_data.set(f'{get_key}', f'{input("name:")}')
                        msg_insert = redis_data.get(f'{get_key}')
                        msg_insert_list = redis_data.rpush(f'user_add_chore', msg_insert)
                        insert_result = """\
                        Insert successfuly
                        Result data of you
                        """
                        print(f'{insert_result}{msg_insert}')
                        get_key = ''
                    elif get_key == 'Exit':
                        break
                    else:
                        break

            elif msg_select_task == 'Delete':
                while msg_select_task != '':
                    input_key = input("Please input your key:")
                    if input_key != '':
                        keys_selete = redis_data.keys(input_key)
                        print('qqq', keys_selete[0])
                        question = input('Do you want to delete dta of key?:')
                        if question.lower().startswith("y"):
                            print('Deleting:', keys_selete[0], 'result is', redis_data.delete(keys_selete[0]))
                            keys_all = redis_data.keys('*')
                            Delete_result = """\
                            Delete successfuly
                            Result data of you
                            """
                            print(Delete_result)
                            for k in keys_all:
                                print(keys_all)
                            input_key = ''
                        elif question.lower().startswith("n"):
                            break
                    elif input_key == 'Exit':
                        break
                    else:
                        print('Key is not null,Please input your key')

            elif msg_select_task == '':
                for k in keys_all:
                    redis_data.delete(k)

            else:
                print('Please input your task')
                break
            i+=1
    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()

