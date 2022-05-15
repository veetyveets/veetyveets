import pandas


# Read from csv file, print from data frame
# df=pandas.read_csv("zillow.csv")
# print("df\n",df)

# print("columns",df.columns)

# Print the average of price column
# print("average price =",df["Price"].mean())

# # Write average to a file
# with open("test_file2.txt","a") as test_file:
#     test_str = "average price(file) =" + str(df["Price"].mean())+ "\n"
#     test_file.write(test_str)

# Example for loop (iterate over range)
# for i in range(1,11):
    # print(i)

# Example list
l = ["TEEK", "DK", "RAV", "FOUR"]

# Example for loop (iterate over list 1)
# for i in l:
    # print(i)

# Example for loop (iterate over list 2)
for index, value in enumerate(l):
    print(index,value)