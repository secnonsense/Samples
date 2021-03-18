from fuzzywuzzy import fuzz,process

print(fuzz.ratio("Let’s do a simple test", "Let us do a simple test"))

choices = ["Data Visualisation", "Data Visualization", "Customised Behaviours", "Customized Behaviors"]
print(process.extract("data visulisation", choices, limit=2))
print(process.extract("custom behaviour", choices, limit=2))
