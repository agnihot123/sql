import argparse
import pandas as pd
import os

def get_params() -> dict:
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="./input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="./input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="./input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="./output_data/outputs/")
    return vars(parser.parse_args())



def main():
    params = get_params()
    customers = pd.read_csv('C:\\Users\\agnihotrip\\PycharmProjects\\SQL-Assignment\\input_data\\starter\\customers.csv')
#    print(customers)
#        customer_id  loyalty_score
    products = pd.read_csv('C:\\Users\\agnihotrip\\PycharmProjects\\SQL-Assignment\\input_data\\starter\\products.csv')
#    print(products)
#   product_id product_description product_category

#    path = 'C:\\Users\\agnihotrip\\PycharmProjects\\SQL-Assignment\\input_data\\starter\\transactions'
#    temp = pd.DataFrame()
#    for file in os.listdir(path):
        #print(file)
        #print(path + "/" +file + "/transactions.json")
#        df = pd.read_json(path + "/" +file + "/transactions.json", lines=True)
#        temp = pd.concat(temp,df)

#    print(temp)
#    transactions = pd.DataFrame(temp)
#    print(transactions)
    transactions = pd.read_json('C:\\Users\\agnihotrip\\PycharmProjects\\SQL-Assignment\\input_data\\starter\\transactions/d=2018-12-01/transactions.json', lines=True)
#    print(transactions)
    cust_trans = pd.merge(customers, transactions, on='customer_id')
    print(cust_trans)
    product_trans =cust_trans['basket'].to_csv()
    print(product_trans)


####

if __name__ == "__main__":
    main()

