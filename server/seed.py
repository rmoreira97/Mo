# seed.py
from app import create_app
from extensions import db
from models import MomoFamily
from datetime import datetime
import json

app = create_app()

def seed_database():
    with app.app_context():  # Enter the application context
        db.create_all()  # Create the database tables (only do this once, not every time you seed)

        # Define your data here...
        data = [
   
 {
   "Name":"Genki",
   "About":{
      "role":[
         "Mother",
         "Wife"
      ],
      "gender":"Female",
      "birthdate":"June 24th, 1986",
      "location":"Kyoto City Zoo"
   },
   "ProfilePic":"https://i.pinimg.com/736x/d3/18/20/d318201fb5c8b7aee7efc855e1fff01e.jpg",
   "CoverPhoto":"https://bzmaestroeats.files.wordpress.com/2021/10/genki.jpg",
   "Gallery":[
      "https://i.ytimg.com/vi/qoygtJASsqo/maxresdefault.jpg",
      "https://i.redd.it/2mgyw3c1mj961.jpg"
   ],
   "Posts": 
   [
  {
    "PostID": "1",
    "Date": "2023-11-28 10:30 AM",
    "Caption": "Enjoying a beautiful day at Kyoto City Zoo!",
    "Media": {
      "Url": "https://example.com/post1.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "2",
    "Date": "2023-11-27 04:45 PM",
    "Caption": "Family time with Genki and Kintaro!",
    "Media": {
      "Url": "https://example.com/post2.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "3",
    "Date": "2023-11-26 08:15 AM",
    "Caption": "Looking back at my journey at Kyoto City Zoo. #memories",
    "Media": {
      "Url": "https://example.com/post3.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "4",
    "Date": "2023-11-25 02:00 PM",
    "Caption": "Just hanging out with Annie from Higashiyama Zoo!",
    "Media": {
      "Url": "https://example.com/post4.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "5",
    "Date": "2023-11-24 09:45 AM",
    "Caption": "A sunny day with my gorilla friends. 🌞",
    "Media": {
      "Url": "https://example.com/post5.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "6",
    "Date": "2023-11-23 05:20 PM",
    "Caption": "Exploring the jungle today. Such a fascinating place!",
    "Media": {
      "Url": "https://example.com/post6.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "7",
    "Date": "2023-11-22 11:10 AM",
    "Caption": "Gorilla playtime! 🦍",
    "Media": {
      "Url": "https://example.com/post7.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "8",
    "Date": "2023-11-21 03:55 PM",
    "Caption": "Relaxing in my favorite spot. Peace and tranquility. 🌿",
    "Media": {
      "Url": "https://example.com/post8.jpg",
      "Type": "image"
    }
  }

],
   
   "Bio":{
      "Feature":"Genki was born at Kyoto City Zoo. Her parents were Makk and Hiromi. In her youth, Genki was known for being a bit of a troublemaker, which posed challenges for Hiromi in raising her. Genki was moved to Ueno in Tokyo for a breeding project, where she encountered Biju, a male gorilla who was initially compatible with her until Momoko entered the scene. Biju fell for Momoko, affecting his relationship with Genki, leading to Genki's emotional struggles. She became mentally unstable and even resorted to self-mutilation, a behavior that continued after her return to Kyoto Zoo. Her return was necessitated by the significant weight loss and danger to her life. Genki would pick at her hands and feet during this time. However, the reunion with her mother, Hiromi, helped her regain her original weight and mental stability. The turning point in Genki's life was her meeting with Momotaro, who turns out to be the son of Genki's former lover, Biju, and her rival, Momoko. Prior to their meeting, the Kyoto City Zoo had shown her images of Momotaro in order to prepare her for his arrival and study her reactions. Their encounter was swift, and they fell in love quickly, with Genki seeing shades of her past love, Biju, in Momotaro. Now, Genki has two sons, Gentaro and Kintaro, and has been an excellent partner for Momotaro. She is known for having a big appetite, which could be attributed to her love for food and potential digestion issues."
   },
   "Timeline":{
      "Events":[
         {
            "event_date":"1986-06-24",
            "event_description":"Genki was born at Kyoto City Zoo. Her father is Makk, and her mother is Hiromi."
         },
         {
            "event_date":"1997-03-19",
            "event_description":"Genki was relocated to Ueno Zoological Gardens at a healthy weight of 106.5 kg."
         },
         {
            "event_date":"1999-11-29",
            "event_description":"Genki was relocated back to Kyoto City Zoo after being involved in a love triangle with Momoko, competing for the attention of Biju. Genki returned to Kyoto in a depressed state with a weight of 68 kg."
         },
         {
            "event_date":"2011-12-21",
            "event_description":"After being introduced to Momotaro and eventually falling in love, Genki successfully gave birth to Gentaro, whose father was Momotaro. This birth marked the first successful mating between two gorillas born in Japan."
         },
         {
            "event_date":"2012",
            "event_description":"Genki was unable to produce sufficient milk for Gentaro to survive. As a result, the two were separated for almost a year, as Gentaro had to be artificially raised by a zookeeper to ensure his survival."
         },
         {
            "event_date":"2013-2018",
            "event_description":"Genki was eventually reunited with Gentaro and successfully raised him to become an admirable, healthy gorilla boy."
         },
         {
            "event_date":"2018-12-19",
            "event_description":"Genki gave birth to Kintaro, whose father was Momotaro. Genki had to be given supplements in order to produce sufficient milk for Kintaro. When this failed, Kintaro would be fed by zookeepers, but there was no need to separate him from the troop."
         },
         {
            "event_date":"2019-2023",
            "event_description":"Genki successfully raised Kintaro to become an independent and remarkably strong gorilla boy, like Gentaro before him."
         }
      ]
   }
},
{
   "Name":"Momotaro",
   "About":{
      "role":[
         "Father",
         "Husband"
      ],
      "gender":"Male",
      "birthdate":"July 3rd, 2000",
      "location":"Kyoto City Zoo"
   },
   "ProfilePic":"https://i.imgur.com/ILxhXKh.jpeg",
   "CoverPhoto":"https://i.imgur.com/UIfiXa5.jpg",
   "Gallery":[
      "https://pbs.twimg.com/media/E3sEnOfWUAc7-uw.jpg",
      "https://i.pinimg.com/originals/71/06/15/71061590e8f78f5501af7a91f3ac10a1.png",
      "https://pds.exblog.jp/pds/1/201710/11/39/e0363539_20575501.jpg"
   ],
   
   "Posts": 
   [
  {
    "PostID": "1",
    "Date": "2023-11-28 10:30 AM",
    "Caption": "Enjoying a beautiful day at Kyoto City Zoo!",
    "Media": {
      "Url": "https://example.com/post1.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "2",
    "Date": "2023-11-27 04:45 PM",
    "Caption": "Family time with Genki and Kintaro!",
    "Media": {
      "Url": "https://example.com/post2.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "3",
    "Date": "2023-11-26 08:15 AM",
    "Caption": "Looking back at my journey at Kyoto City Zoo. #memories",
    "Media": {
      "Url": "https://example.com/post3.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "4",
    "Date": "2023-11-25 02:00 PM",
    "Caption": "Just hanging out with Annie from Higashiyama Zoo!",
    "Media": {
      "Url": "https://example.com/post4.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "5",
    "Date": "2023-11-24 09:45 AM",
    "Caption": "A sunny day with my gorilla friends. 🌞",
    "Media": {
      "Url": "https://example.com/post5.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "6",
    "Date": "2023-11-23 05:20 PM",
    "Caption": "Exploring the jungle today. Such a fascinating place!",
    "Media": {
      "Url": "https://example.com/post6.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "7",
    "Date": "2023-11-22 11:10 AM",
    "Caption": "Gorilla playtime! 🦍",
    "Media": {
      "Url": "https://example.com/post7.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "8",
    "Date": "2023-11-21 03:55 PM",
    "Caption": "Relaxing in my favorite spot. Peace and tranquility. 🌿",
    "Media": {
      "Url": "https://example.com/post8.jpg",
      "Type": "image"
    }
  }

],
   "Bio":{
      "Feature":"Momotaro was born in Ueno Zoo in Tokyo, his mother being Momoko, who is also the mother of Sumomo. He is Momoko's first child, and his father was Biju, who passed away at the age of 12. Unfortunately, Momotaro never had the chance to see his father as he was born after Biju's death. At that time, Ueno Zoo had a gathering of many gorillas from across Japan, and Genki was among them. Initially, Genki and other female gorillas were Biju's partners, but things changed when Momoko joined the herd after Biju fell for her. Momoko and Momotaro spent their time together as mother and child after Biju's demise, which meant Momotaro had never interacted with other gorillas, except for a brief period with a female gorilla named Laura. Over time, Momoko and Momotaro moved between Ueno and Chiba. Upon returning to Ueno, Momoko was living with a male gorilla, leaving Momotaro alone. Then, the day came for Momotaro to leave for the Kyoto City Zoo. Some interesting facts about Momotaro include his aversion to soil, which likely stems from growing up on concrete. He also has a strong attachment to food, as he never had to compete for it due to his upbringing. Additionally, Momotaro dislikes helmets, likely due to a traumatic experience during his move from Ueno to Kyoto. His drumming behavior is relatively rare, occurring around 10 times a year and more commonly when Gentaro is drumming. As for Momotaro's interactions with female gorillas, it's suggested that his lack of experience living with other gorillas may be a significant factor. However, with his current living situation alongside Genki and his two sons, Gentaro and Kintaro, it's unlikely that he is inherently bad with female gorillas."
   },
   "Timeline":{
      "Events":[
         {
            "event_date":"2000-07-03",
            "event_description":"Momotaro was born at Ueno Zoological Gardens in Tokyo, Japan. He was brought up by his mother, Momoko."
         },
         {
            "event_date":"2002-07-08",
            "event_description":"Momotaro and Momoko moved to Chiba Zoological Park, where they resided for several years."
         },
         {
            "event_date":"2008-12-02",
            "event_description":"Momotaro and Momoko returned to Ueno Zoological Gardens in Tokyo."
         },
         {
            "event_date":"2010-10-18",
            "event_description":"Momotaro was relocated to Kyoto City Zoo with the intention of breeding with Genki. The acclimation process was successful, and they became a happy couple."
         },
         {
            "event_date":"2011-12-21",
            "event_description":"Gentaro was born at Kyoto City Zoo, becoming Momotaro's son. His mother was Genki. In the years to come, Momotaro would gradually learn to become a father."
         },
         {
            "event_date":"2018-12-19",
            "event_description":"Kintaro was born at Kyoto City Zoo, becoming Momotaro's second son. His mother was also Genki. Momotaro and Kintaro eventually developed a strong relationship as Momotaro displayed once again his superb abilities as a father."
         }
      ]
   }
},
{
   "Name":"Gentaro",
   "About":{
      "role":[
         "Son",
         "Brother"
      ],
      "gender":"Male",
      "birthdate":"December 21st, 2011",
      "location":"Kyoto City Zoo"
   },
   "ProfilePic":"https://pbs.twimg.com/media/EuC8B3MXUAUNXGa.jpg:large",
   "CoverPhoto":"https://i.imgur.com/9j8Sg50.jpg",
   "Gallery":[
      "https://shigen.nig.ac.jp/gain/image_data/gori/indi/0096/20120625183625_0_20120623WP077.jpg",
      "https://shigen.nig.ac.jp/gain/image_data/gori/indi/0096/20140910184446_1_IMG_2226.jpg",
      "https://pbs.twimg.com/media/E1MW7KYXIAItCV9?format=jpg&name=large",
      "https://pbs.twimg.com/media/FHEfdjXWYAkX2kp.jpg:large"
   ],
   
   "Posts": [
   {
    "PostID": "1",
    "Date": "2023-11-28 10:30 AM",
    "Caption": "A show of force!.... Gorillas avoid looking eachother in the eye, as it is a sign of aggression and here, Gentaro was simply testing the waters...",
    "Media": {
      "Url": "https://firebasestorage.googleapis.com/v0/b/mofamily-4c06a.appspot.com/o/posts%2F3%2Fyqdf6z.mp4?alt=media&token=02e9621e-74dd-4d2e-9a35-d5567bf86bb7",
      "Type": "video"
    }
  },
  {
    "PostID": "2",
    "Date": "2023-11-27 04:45 PM",
    "Caption": "Family time with Genki and Kintaro!",
    "Media": {
      "Url": "https://example.com/post2.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "3",
    "Date": "2023-11-26 08:15 AM",
    "Caption": "Looking back at my journey at Kyoto City Zoo. #memories",
    "Media": {
      "Url": "https://example.com/post3.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "4",
    "Date": "2023-11-25 02:00 PM",
    "Caption": "Just hanging out with Annie from Higashiyama Zoo!",
    "Media": {
      "Url": "https://example.com/post4.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "5",
    "Date": "2023-11-24 09:45 AM",
    "Caption": "A sunny day with my gorilla friends. 🌞",
    "Media": {
      "Url": "https://example.com/post5.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "6",
    "Date": "2023-11-23 05:20 PM",
    "Caption": "Exploring the jungle today. Such a fascinating place!",
    "Media": {
      "Url": "https://example.com/post6.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "7",
    "Date": "2023-11-22 11:10 AM",
    "Caption": "Gorilla playtime! 🦍",
    "Media": {
      "Url": "https://example.com/post7.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "8",
    "Date": "2023-11-21 03:55 PM",
    "Caption": "Relaxing in my favorite spot. Peace and tranquility. 🌿",
    "Media": {
      "Url": "https://example.com/post8.jpg",
      "Type": "image"
    }
  }

],
   "Bio":{
      "Feature":"Gentaro was born in Kyoto City Zoo at 12:12 am on December 21st, 2011, making him the first child born between two gorillas born in Japan. Initially, Gentaro faced challenges in getting enough milk from his mother, Genki, which led to him being artificially fed. However, the zookeepers introduced Gentaro to Genki so that he could eventually return to his family. Their reunion had its initial challenges, with Genki needing time to figure out how to interact with Gentaro, and vice versa. Despite being mother and child, they were sometimes separated at night during this period. However, this separation didn't last long, and Genki quickly resumed her role as Gentaro's caregiver. Gentaro's upbringing differed from that of human babies, as gorilla infants spend 24 hours a day with their mothers during their first year. It's also mentioned that Gentaro might become a silverback when he's older, but the exact timing is uncertain and may depend on various factors. Additionally, the question of when Gentaro will leave his family remains unanswered and is subject to negotiations between zoos. There's also speculation about Gentaro potentially partnering with Annie from Higashiyama Zoo, although discussions among zoos play a significant role in these decisions.."
   },
   "Timeline":{
      "Events":[
         {
            "event_date":"2011-12-21",
            "event_description":"Gentaro's birth at Kyoto City Zoo, marking him as the first child born between two gorillas in Japan."
         },
         {
            "event_date":"2012",
            "event_description":"The early months of Gentaro's life, during which he faced challenges in obtaining sufficient milk from his mother, Genki. Zookeepers initiated artificial feeding to ensure his well-being."
         },
         {
            "event_date":"2013",
            "event_description":"Gentaro's reunion with Genki after their initial separation. They both needed time to adapt to their roles, and Genki resumed her critical role as Gentaro's primary caregiver."
         },
         {
            "event_date":"2014",
            "event_description":"Gentaro finally adjusted to life as a young gorilla and became the jewel of the family until Kintaro's arrival in the following years."
         },
         {
            "event_date":"2018-2022",
            "event_description":"During this period, Gentaro received less attention from his mother due to Kintaro's birth. He adapted and learned how to become a big brother, caring for Kintaro gently. This process had its ups and downs, but Gentaro has become a role model sibling."
         },
         {
            "event_date":"2023",
            "event_description":"In the year 2023, Gentaro has shown substantial growth in size and muscle development. He has grown to be on the cusp of silverback-hood. However, due to Momotaro's presence, he has not fully realized the transformation into an adult."
         }
      ]
   }
},
{
   "Name":"Kintaro",
   "About":{
      "role":[
         "Son",
         "Brother"
      ],
      "gender":"Male",
      "birthdate":"December 19th, 2018",
      "location":"Kyoto City Zoo"
   },
   "ProfilePic":"https://bzmaestroeats.files.wordpress.com/2021/10/kintaro.jpg",
   "CoverPhoto":"https://i.pinimg.com/originals/c2/a7/7a/c2a77a148358a89a60c4f6986ce4c5c0.jpg",
   "Gallery":[
      "https://pbs.twimg.com/media/FKmjMQ4XMAAxY2X.jpg:large",
      "https://i.pinimg.com/1200x/3f/9b/d9/3f9bd9001a425f24f95fa97b2a196211.jpg",
      "https://i.ytimg.com/vi/Z2DnBFtqbto/maxresdefault.jpg",
      "https://i.pinimg.com/736x/ec/10/2a/ec102ac948632962afcdeeab120bbbef.jpg",
      "https://yt3.googleusercontent.com/MG-pAdNp8brlUGFp0LVI8PV5oGQ20BYk2EdNHeoJ81KS5wPM_io9fF1xxqQGiKbDgBGrWW_h=s900-c-k-c0x00ffffff-no-rj"
   ],"Posts": [
  {
    "PostID": "1",
    "Date": "2023-11-28 10:30 AM",
    "Caption": "Kintaro with his Dad, Momotaro!",
    "Media": {
      "Url": "https://firebasestorage.googleapis.com/v0/b/mofamily-4c06a.appspot.com/o/posts%2F4%2Fmaxresdefault%20(1).jpg?alt=media&token=edbb69f8-d5bf-43d5-9dd2-67b2968224e1",
      "Type": "image"
    }
  },
  {
    "PostID": "2",
    "Date": "2023-11-27 04:45 PM",
    "Caption": "A few years later with his Dad..",
    "Media": {
      "Url": "https://firebasestorage.googleapis.com/v0/b/mofamily-4c06a.appspot.com/o/posts%2F4%2FEyTF7utWQAgWTMN.jpg?alt=media&token=8fe10488-4680-43d4-8ebc-1f1b132bf84b",
      "Type": "image"
    }
  },
  {
    "PostID": "3",
    "Date": "2023-11-26 08:15 AM",
    "Caption": "Looking back at my journey at Kyoto City Zoo. #memories",
    "Media": {
      "Url": "https://example.com/post3.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "4",
    "Date": "2023-11-25 02:00 PM",
    "Caption": "Just hanging out with Annie from Higashiyama Zoo!",
    "Media": {
      "Url": "https://example.com/post4.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "5",
    "Date": "2023-11-24 09:45 AM",
    "Caption": "A sunny day with my gorilla friends. 🌞",
    "Media": {
      "Url": "https://example.com/post5.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "6",
    "Date": "2023-11-23 05:20 PM",
    "Caption": "Exploring the jungle today. Such a fascinating place!",
    "Media": {
      "Url": "https://example.com/post6.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "7",
    "Date": "2023-11-22 11:10 AM",
    "Caption": "Gorilla playtime! 🦍",
    "Media": {
      "Url": "https://example.com/post7.jpg",
      "Type": "image"
    }
  },
  {
    "PostID": "8",
    "Date": "2023-11-21 03:55 PM",
    "Caption": "Relaxing in my favorite spot. Peace and tranquility. 🌿",
    "Media": {
      "Url": "https://example.com/post8.jpg",
      "Type": "image"
    }
  }

],
   "Bio":{
      "Feature":"Kintaro was born in Kyoto City Zoo on December 19th, 2018. He is the son of Momotaro and Genki, making him a valuable addition to the gorilla family. Kintaro was raised by his mother, Genki, but his milk intake required supplementation during his early years due to Genki's low milk production. Despite this, Kintaro observed how Momotaro and Gentaro interacted and showed great progress in becoming a strong, independent gorilla despite his age and initial trials in life. He has a strong-willed and caring nature, becoming a cherished member of the family. Kintaro's journey as a young gorilla is just beginning, and he holds a special place in the hearts of those who follow the family's story.."
   },
   "Timeline":{
      "Events":[
         {
            "event_date":"2018-12-19",
            "event_description":"Kintaro's birth at Kyoto City Zoo, becoming the second son of Momotaro and Genki."
         },
         {
            "event_date":"2019-2021",
            "event_description":"During his early years, Kintaro's milk intake required supplementation due to Genki's low milk production. Despite this, there was no need to separate him from his mother."
         },
         {
            "event_date":"2022",
            "event_description":"Kintaro observed how Momotaro and Gentaro interacted, showing great progress in becoming a strong, independent gorilla despite his age and initial trials in life."
         }
      ]
   }
}
]
# Seed the data into the database
        for item in data:
            # Check if 'Posts' key exists in the dictionary
            if 'Posts' in item:
                # Convert the "Posts" field to JSON format if it exists
               posts_data = item['Posts']
            else:
                # Handle the case where 'Posts' key does not exist
                posts_data = []  # Assign an empty list if 'Posts' is not present
            
            gorilla = MomoFamily(**item)
            db.session.add(gorilla)

        db.session.commit()  # Commit the changes to the database
        db.session.close()  # Close the database session

    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()