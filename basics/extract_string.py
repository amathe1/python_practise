import re

# Multiline input (you can read this from a file too)
data = """
./dailydev40/cassandracfg.properties:mme.cassandracfg.alias.cassandra_version = cie-cassandra-4.0.0.90

"""

# Pattern to extract key and value
#pattern = r'cassandracfg\.alias\.(cassandra_version)\s*=\s*(cie-cassandra-[\d\.]+)'
pattern = r'\./([^/]+)/cassandracfg\.properties:.*?cassandra_version\s*=\s*(cie-cassandra-[\d\.]+)'

# Extract and print
for line in data.strip().split('\n'):
    match = re.search(pattern, line)
    if match:
        key = match.group(1)
        value = match.group(2)
        print(f"{key} = {value}")
