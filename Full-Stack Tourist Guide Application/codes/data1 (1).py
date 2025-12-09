import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd='admin',database='tourism')
cur=con.cursor()

cur.execute('''insert into states values('KARNATAKA','','S'),
('KARNATAKA','BENGALURU','C'),
('KARNATAKA','MYSURU','C'),
('KARNATAKA','CHIKKAMAGALURU','C'),
('KARNATAKA','MANGALURU','C'),
('KARNATAKA','SHIVAMOGGA','C')''')
con.commit()

cur.execute("""insert into places values
('KARNATAKA','MYSURU','MYSORE PALACE','An incredibly breathtaking example of Indo - Saracenic style of architecture, the Mysore Palace is a magnificent edifice located in Mysore in the state of Karnataka.\nThe facade of the palace is a harmonious blend of Hindu, Muslim, Rajput and Gothic styles which imparts it a regal quality.'),
('KARNATAKA','MYSURU','BRINDAVAN GARDENS','The Brindavan Gardens, spread over 60 acres, is located at a distance of 21 km away from Mysore.\nBuilt across the notable river of India, Cauvery, it took around five years to complete the project.'),
('KARNATAKA','MYSURU','MYSORE ZOO',"The Zoo's meticulous planning is responsible for making it a special zoological garden. It tends to create a natural habitat for the animals in it.\nLocated near the palace in Mysore, The Zoological Garden covers an area of 157 acres.\nIt is one of the oldest and most famous zoos in India"),
('KARNATAKA','MYSURU','BONSAI GARDEN','One of the more unique attractions of the Royal Mysore, the Bonsai Garden of Mysore is home to over a 100 different varieties of Bonsai trees spread across this vast estate.The beauty of the garden is accentuated by the stream that flows within, as well as the placement of Buddha statues and monkey statues around the area, representative of the zen culture from where the art of Bonsai was evolved.'),
('KARNATAKA','MYSURU','RAIL MUSEUM','The Mysore Rail Museum is the second of its kind in India, right after the National Railways Museum of Delhi. It was built in the year 1979 by the Indian Railways and has been the safehouse of Railway collectables ever since.'),

('KARNATAKA','BENGALURU','LAL BAGH BOTANICAL GARDEN','Lalbagh is one of the oldest botanical gardens in India and is also a major tourist attraction in South India.\nThe garden itself is spread over an area of 240 acres and its construction was commissioned by the famous ruler Hyder Ali.'),
('KARNATAKA','BENGALURU','BANGALORE PALACE',"The Palace is a perfect representation of the lavishness and splendour with which India's most resilient dynasties ruled.\nFamous for its opulent architecture and amusement activities, the Palace is visited by several visitors every day."),
('KARNATAKA','BENGALURU','BANNERGHATTA NATIONAL PARK','Located on the outskirts of Bangalore, and usually known as BBBP, the Bengaluru Bannerghatta Biological Park is amongst the most popular and frequently visited destinations in the city.\nThe Bannerghatta Biological Park is also the first biological park in all of India, which has a fenced forested elephant sanctuary.'),
('KARNATAKA','BENGALURU','NANDI HILLS','Nandi Hills, a small albeit beautiful town, is just 60 km away from the city of Bangalore and has emerged as the perfect weekend getaway for its people.\nThe place was previously used by the famous ruler Tipu Sultan as a summer retreat, and several traces of the Sultan’s life and legacy can be found in the area.'),
('KARNATAKA','BENGALURU',"TIPU SULTAN'S SUMMER PALACE",'This summer residence of Tipu Sultan was built in the year 1791.\nThe ceilings and walls of the palace have a floral touch with Islamic carvings and decorations.'),

('KARNATAKA','CHIKKAMAGALURU','COFFEE MUSEUM','Coffee Museum in Chikmagalur is a haven for experiencing the fresh aroma of original coffee.\nThe building is amidst lush greenery and it is surrounded by small coffee plant pots.'),
('KARNATAKA','CHIKKAMAGALURU','BALLALARAYANA DURGA FORT','The fort dates as far back as the 12th century and once belonged to the Hoysala Empire.\nIt follows the Karnata Dravida architectural style and forms an excellent backdrop for photographs.'),
('KARNATAKA','CHIKKAMAGALURU','MAHATMA GANDHI PARK','The park has footpaths which zigzag through the open spaces and large, shady trees and is one of the best places to visit.\nIt is one of the most beautiful places to visit in Chikmagalur with the entire family which is located within the city limits.'),
('KARNATAKA','CHIKKAMAGALURU','BHADRA WILDLIFE SANCTUARY','A protected area and Project Tiger area, this wildlife sanctuary is home to a number of wild animals and birds.\nThe flora and fauna that you find here is exotic and worth watching.'),
('KARNATAKA','CHIKKAMAGALURU','KUDREMUKH NATIONAL PARK','Located in the pristine environs of the Western Ghats, the park is located at an altitude of around 1800 metres above sea level.\nThere is a hill here that is shaped like the head of a horse.\n[In Kannada, a horse is called Kudre and the Kannada word for face is Mukha].'),

('KARNATAKA','SHIVAMOGGA','SHIVAPPA NAYAKA PALACE MUSEUM','Lying on the banks of River Tunga, the Shivappa Nayaka Palace is a popular attraction in Shimoga town.\nA very much sought-after destination among tourists, the palace was established by Shivappa Naik of Keladi during the 16th century and was crafted brilliantly out of rosewood.'),
('KARNATAKA','SHIVAMOGGA','TYAVAREKOPPA TIGER AND LION SAFARI','Covering a huge area of 200 hectares, the place is renowned for its Lion and Tiger Safari which commenced in the year 1998.\nApart from safari, the place also houses wildlife species like leopard, deer, sloth bear etc.'),
('KARNATAKA','SHIVAMOGGA','GUDAVI BIRD SANCTUARY','Gudavi Bird Sanctuary is located in the town of Sorab in Shimoga on the banks of Gudavi Lake.\nIt serves as a popular destination in the region and inhabits various species of migratory birds like white ibis, little cormorant, Indian cormorant, pariah kite, little grebe, jungle fowl etc.'),
('KARNATAKA','SHIVAMOGGA','LINGANAMAKKI DAM','Linganamakki Dam is one of the largest human-made water reservoirs of the country.\nThe length of the dam is a mere 2.4 km but owing to the width, its water storing capacity is much higher than any other dam.'),
('KARNATAKA','SHIVAMOGGA','JOG FALLS','The second-highest plunge waterfall in India, Jog Falls is a major tourist attraction in Karnataka and is the highest waterfall in the state.\nSecond to the Nohkalikai Falls of Meghalaya, Jog falls drops about a huge 253 m (850 ft.) in a single fall.'),

('KARNATAKA','MANGALURU','KADRI HILLS PARK',"Housing a wide variety of wild animals, this is the largest garden in Mangalore as well as the city's most popular picnic/jogging spot.\nRare species of birds, anteaters and various other animals are seen in the animal conservatory."),
('KARNATAKA','MANGALURU','ST ALOYSIUS CHAPEL','St Aloysius Chapel is a Catholic Church and a famous attraction set atop the Lighthouse Hill and has a regal look which is breathtaking right from the entrance.\nThe unique wall paintings of St. Aloysius Chapel are stunning and attract visitors in large numbers.'),
('KARNATAKA','MANGALURU','BEJAI MUSEUM',"The Srimanthi Bai Government Museum or the Bejai Museum is located in the heart of the city and is also Mangalore's only museum.\nIt has a collection of ancient coins, paintings, statues and inscriptions which display the rich heritage of India."),
('KARNATAKA','MANGALURU','PILIKULA NISARGADHAMA',"Pilikula Nisargadhama is a famous multi-purpose tourist attraction in Mangalore created amidst nature to provide a rejuvenating experience.\nIn Tulu, the name Pilikula means 'a pool of Tigers'. The region was once the natural habitat of Tigers who would visit the lake to drink water."),
('KARNATAKA','MANGALURU','KUDROLI SRI GOKARNANATHA KSHETRA','The Gokarnanatheshwara Temple, otherwise known as Kudroli Sri Gokarnanatha Kshetra, is in the Kudroli area of Mangalore in Karnataka, India.\nIt was consecrated by Narayana Guru.\nIt is dedicated to Gokarnanatha, a form of Lord Shiva.')

""")
con.commit()

con.close()
