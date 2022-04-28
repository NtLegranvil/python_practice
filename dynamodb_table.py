"""
Creating a DynamoDB table 
"""
import boto3

#get service
dynamodb = boto3.resource('dynamodb',region_name='us-west-1')
    
#create table
table = dynamodb.create_table(
    TableName='Shows',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

#prints while table is loading
print('Table Loading...')

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='Shows')

#specifies table items will be loaded to
table = dynamodb.Table('Shows')

#adds items to table
table.put_item(
        Item={
            'year': 2008,
            'title': 'True Blood',
            'Genre': ["Drama", "Fantasy", "Mystery", "Romance", "Thriller"],
            'Description': 'Telepathic waitress Sookie Stackhouse encounters a strange new supernatural world when she meets the mysterious Bill Compton, a southern Louisiana gentleman and vampire.',
            'Seasons': '7 seasons',
            'Rating': '7.9'
            }
)

table.put_item(
   Item={
        'year': 2013,
        'title': 'The Originals',
        'Genre': ["Drama", "Fantasy", "Horror"],
        'Description': 'A family of power-hungry thousands-year-old vampires look to take back the city that they built and dominate all those who have done them wrong.',
        'Seasons': '5 seasons',
        'Rating': '8.3'
        }
)

table.put_item(
   Item={
        'year': 2010,
        'title': 'The Walking Dead',
        'Genre': ["Drama", "Horror", "Thriller"],
        'Description': 'The Walking Dead tells the story of the months and years that follow after a zombie apocalypse. It follows a group of survivors, led by former police officer Rick Grimes, who travel in search of a safe and secure home.',
        'Seasons': '11 seasons',
        'Rating': '8.2'
        }
)

table.put_item(
   Item={
        'year': 2017,
        'title': 'Ozark',
        'Genre': ["Crime", "Drama", "Thriller"],
        'Description': 'A financial advisor drags his family from Chicago to the Missouri Ozarks, where he must launder money to appease a drug boss.',
        'Seasons': '4 seasons',
        'Rating': '8.5'
        }
)

table.put_item(
   Item={
        'year': 2017,
        'title': 'The Punisher',
        'Genre': ["Action", "Crime", "Drama", "Thriller"],
        'Description': 'After the murder of his family, Marine veteran Frank Castle becomes the vigilante known as "The Punisher," with only one goal in mind: to avenge them.',
        'Seasons': '2 seasons',
        'Rating': '8.5'
        }
)

table.put_item(
   Item={
        'year': 2010,
        'title': 'Spartacus',
        'Genre': ["Action", "Adventure", "Biography", "Drama", "History", "Romance"],
        'Description': 'The life of Spartacus, the gladiator who lead a rebellion against the Romans. From his time as an ally of the Romans, to his betrayal and becoming a gladiator, to the rebellion he leads and its ultimate outcome.',
        'Seasons': '3 seasons',
        'Rating': '8.5'
        }
)

table.put_item(
   Item={
        'year': 2011,
        'title': 'American Horror Story',
        'Genre': ["Drama", "Horror", "Sci-Fi", "Thriller"],
        'Description': 'An anthology series centering on different characters and locations, including a house with a murderous past, an insane asylum, a witch coven, a freak show circus, a haunted hotel, a possessed farmhouse, a cult, the apocalypse, a slasher summer camp, and a bleak beach town and desert valley.',
        'Seasons': '12 seasons',
        'Rating': '8.0'
        }
)

table.put_item(
   Item={
        'year': 2018,
        'title': 'The Haunting of Hill House',
        'Genre': ["Drama", "Horror", "Mystery"],
        'Description': 'Flashing between past and present, a fractured family confronts haunting memories of their old home and the terrifying events that drove them from it.',
        'Seasons': '1 season',
        'Rating': '8.6'
        }
)

table.put_item(
   Item={
        'year': 1993,
        'title': 'The X-Files',
        'Genre': ["Crime", "Drama", "Mystery", "Sci-Fi", "Thriller"],
        'Description': 'Two F.B.I Agents, Fox Mulder the believer and Dana Scully the skeptic, investigate the strange and unexplained, while hidden forces work to impede their efforts.',
        'Seasons': '11 seasons',
        'Rating': '8.6'
        }
)

table.put_item(
   Item={
        'year': 2006,
        'title': 'Dexter',
        'Genre': ["Crime", "Drama", "Mystery"],
        'Description': "He's smart. He's lovable. He's Dexter Morgan, America's favorite serial killer, who spends his days solving crimes and nights committing them.",
        'Seasons': '8 seasons',
        'Rating': '8.7'
        }
)

table.put_item(
   Item={
        'year': 2016,
        'title': 'Stranger Things',
        'Genre': ["Drama", "Fantasy", "Horror"],
        'Description': 'When a young boy disappears, his mother, a police cheif and his friends must confront terrifying supernatural forces in order to get him back.',
        'Seasons': '4 seasons',
        'Rating': '8.6'
        }
)

table.put_item(
   Item={
        'year': 2011,
        'title': 'Game of Thrones',
        'Genre': ["Actions", "Adventure", "Drama"],
        'Description': 'Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.',
        'Seasons': '8 seasons',
        'Rating': '9.2'
        }
)

table.put_item(
   Item={
        'year': 2004,
        'title': 'House M.D',
        'Genre': ["Drama", "Mystery"],
        'Description': 'An antisocial maverick doctor who specializes in diagnostic medicine does whatever it takes to solve puzzling cases that come his way using his crack team of doctors and his wits.',
        'Seasons': '8 seasons',
        'Rating': '8.7'
        }
)

#print out status of table upon completion
print("Table status:", table.table_status)

print("Table scan in progress...")
resp = dynamodb.Table('Shows').scan() #scans entire table
data = resp['Items'] #stores response in a variable 
print(data) #prints item info from table
