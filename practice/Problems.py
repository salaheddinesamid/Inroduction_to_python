import csv
import logging
logging.basicConfig(level=logging.DEBUG,
                    format= "%(asctime)s - %(levelname)s - %(message)s")
users  =[{

    "first_name": "Helen",
    "age" : 39
},
    {
        "first_name" : "Buck" ,
        "age" : 10
    },
    {
        "first_name" : "anni",
        "age" : 9
    }
]
data = [20,1,0,4,8,3]
def get_user_name(list_of_users):
    """
    This function takes users and return their user_name with lower case
    :param users:
    :return: Users name with lower case
    """
    logging.info("The function takes the list of users")
    logging.info("Iterating over each user")
    for user in users:
        return(user["first_name"].lower())


def sort_data(arr):
    """
    This function will take an unsorted array, and return the sorted version.
    :param arr:
    :return: sorted array:
    :method: insertion sort
    """
    logging.info("The unsorted data:" + str(arr))
    seq_len = len(arr)
    for index in range(1,seq_len):
        to_insert = arr[index]
        j = index
        while j > 0:
            if to_insert >= arr[j-1]:
                break
            arr[j] = arr[j-1]
            j -=1
        arr[j] = to_insert
    logging.info("The sorted data:" + str(arr))

def read_my_csv(path):
    try:
        with open(path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    logging.info(f'Column names are: {",".join(row)}')
                line_count += 1
    except FileNotFoundError as r:
        logging.info(r)

def filter_data(data):
    """
    Here we will filter a list of users, and return the adults.
    :param data:
    :return: Adult users
    """
    filtered_data = []
    for user in data:
        if user["age"] < 18:
            continue
        else:
            filtered_data.append(user)

    logging.info("Adults are:" + str(filtered_data))

def only_vowels(char_list):
    vowels = ['a','e','i','o','u']
    result = [item for item in char_list if item in vowels]

def convert_matrix(matrix):
    result = [[matrix[row][col] for row in range(0,3)] for col in range(0,3)]
    logging.info(str(result))

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
          ]

convert_matrix(matrix)