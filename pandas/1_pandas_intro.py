"""

Pandas is a Python package that provides data structures and tools for data analysis and manipulation

-> pip3 list
Package            Version
------------------ -----------
apple-certifi      2.3.1
awsappleconnect    3.0.12
backoff            2.2.1
bcrypt             4.1.2
beautifulsoup4     4.12.3
boto3              1.34.81
botocore           1.34.81
certifi            2024.2.2
cffi               1.16.0
charset-normalizer 3.3.2
click              8.1.7
coloredlogs        15.0.1
cryptography       42.0.5
docutils           0.21
filelock           3.15.1
humanfriendly      10.0
idna               3.6
jmespath           1.0.1
numpy              1.26.4
pandas             2.2.3  ==> Pandas installed
paramiko           3.4.0
pip                24.3.1
prettytable        3.12.0
prettyTables       1.1.5
pycparser          2.22
pyjavaproperties   0.7
PyNaCl             1.5.0
pyotp              2.9.0
python-dateutil    2.9.0.post0
pytz               2024.1
PyYAML             6.0.1
radarclient        12.2
recertifi          1.2.0
requests           2.31.0
s3transfer         0.10.1
setuptools         56.0.0
six                1.16.0
soupsieve          2.5
statistics         1.0.3.5
tabulate           0.9.0
tzdata             2024.1
urllib3            1.26.18
wcwidth            0.2.13
wheel              0.45.1

"""


# importing pandas package
# Use command : 'pip/pip3 list' on terminal and confirm if pandas package is installed in your local computer 


import pandas as pd


def main():
    df = pd.read_csv('/Users/Arunkumar_Mathe/Documents/python_practise/pandas/exercises.csv', sep=',', index_col=0)
    print(df)
    print()
    print(df.columns)
    
    print()
    # It will print first 2 lines in data frame
    print(df.head(2))

    print()
    # It will print last 2 lines in data frame
    print(df.tail(2))

if __name__ == "__main__":
    main()