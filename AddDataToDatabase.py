
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-e5a0f-default-rtdb.firebaseio.com/"

})
ref=db.reference('Students')

data={
    "02818011621":
    {
        "name":"Ketan Sharma ",
        "major":"Robotics",
        "starting_year":2017,
        "total_attendance":6,
        "year":2,
        "Last_attendance":"2023-04-26 01:30:54"

    },
 
    "35418011621":
    {
        "name":"Hunny",
        "major":"Artificial Intelligence",
        "starting_year":2021,
        "total_attendance":10,
        "year":2,
        "Last_attendance":"2023-04-26 01:30:54" 
    },

    "12818002721":
     {
        "name":"Anjali",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "02218011621":
     {
        "name":"Anuj",
        "major":"Aiml",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        " 20518011621":
     {
        "name":"Arin",
        "major":"Aiml",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "20318002721":
     {
        "name":"Arman",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "35518002721":
     {
        "name":"Aryanika",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "01518011621":
     {
        "name":"Hardik",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "36118002721":
     {
        "name":"Mishba",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "13518002721":
     {
        "name":"Nancy",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "03918011621":
     {
        "name":"Shashank",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "03218002721":
     {
        "name":"Navansh",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "00118002721":
     {
        "name":"Sahil",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "50418002721":
     {
        "name":"Sanya",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "07318002721":
     {
        "name":"Vidushi",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
        "20218002721":
     {
        "name":"Vidushi",
        "major":"CSE",
        "starting_year":2011,
        "total_attendance":10,
        "year":4,
        "Last_attendance":"2023-04-26 01:30:54" 
    },
    
}

for key,value in data.items():
    ref.child(key).set(value)
