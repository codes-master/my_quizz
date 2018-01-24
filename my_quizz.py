#This is a program that displays a quizz on the following course: Maths, Biology, Physics, Geography. It will also store the user's score according to user_name

from random import randrange
from random import randint
from random import choice
from random import sample
from time import sleep

congrats_msg = "Good work, That was the correct answer"
console_user = "Oops..Wrong answer,  try again.."
score = 0
question_index = 0

#this are the math questions
begineer_questions_maths = ["What is the term given to the perimeter around a circle?\n1. circumference\n2. diameter\n3. Radius",
"What is the name of the manual calculating device which consists of beads?\n1. Calculator\n2. Braclet\n3. Abacus",
"What is an isosceles triangle?\n1. A triangle with three equal sides \n2. A triangle with at least two sides equal in length\n3. A triangle with no equal sides",
"How many sides does a decagon have?\n1. Sixteen (16)\n2. Eight(8)\n3. Ten (10)",
"What is 70.3 divided by 10?\n1. 17.4\n2. 5.34\n3. 7.03",
"What is two thirds of 270?\n1. One hundred and eighty (180)\n2. Seventy (70)\n3. Two hundred (200)",
"What is the square root of 81?\n1. seven (7)\n2. Nine (9)\n3. Five (5)",
"How many degrees are there in a right angle?\n1. Thirty degrees (30)\n2. Sixty degrees (60)\n3. Ninety degrees (90)",
"What is the smallest prime number?\n1. One (1)\n2. Two (2)\n3. Zero (0)",
"What is 0.88 as a percentage?\n1. Eighty-eight percent (88%)\n2. Eight percent (8%)\n3. Forty percent(40%)",
"What is three fifths of 50?\n1. Thirty (30)\n2. Twenty-five (25)\n3. Ten (10)",
"What is the meaning of Pi in Math?\n1. it's the cube of the Radius\n2. It's the ratio of a circle's circumference to its diameter\n3. The total surface area covereed by the circle",
"How many straight edges does a cube have?\n1. Eight (8)\n2. Fourteen (14)\n3. Twelve (12)",
"What is the square root of 100?\n1. Ten (10)\n2. One thousand (1000)\n3. Five (8)",
"What is 4 x 9?\n1. Fifty-four (54)\n2. Thirty-six (36)\n3. Twenty-nine (29)",
"What is 4995 divided by 15?\n1. 486\n2. 256\n3. 333",
"What do the numbers 16, 25 and 36 have in common?\n1. They are all square numbers\n2. They are all prime numbers\n3. They are all odd numbers",
"What device is used to measure angles?\n1. A ruler\n2. A protractor\n3. A compass",
"What is 11 x 7?\n1. One hundred and five (105)\n2. Seventy-seven (77)\n3. Fifty-seven (57)",
"What is 0.75 as the lowest possible fraction?\n1. 3/4\n2. 1/2\n3. 1/5",
"What is the total number of degrees in a triangle?\n1. One hundred degress (100)\n2. One hundred and thirty degress (130)\n3. One hundred and eighty degrees (180)",
"How many hours are there in seven days?\n1. Ninety-two (92)\n2. One hundred and sixty-eight (168)\n3. One hundred and twenty (120)",
"What is 9 x 6?\n1. Forty-three (43)\n2. Fifty-four (54)\n3. Sixty-four (64)",
"What is 60% of 40?\n1. Twenty-four (24)\n2. Twenty (20)\n3. Fourteen (14)",
"What is the square route of 144?\n1. Thirteen (13)\n2. Twelve (12)\n3. Eleven (11)",
"What is 11 x 11?\n1. One hundred and one (101)\n2.One hundred and fifty-one (151) \n3. One hundred and twenty-one (121)",
"What is 100 – 151?\n1. Minus fifty-one (-51)\n2. Thirty-one (31)\n3. fifty-one (51)",
"What number must you add to 66 to make the sum of 121\n1. Fifty-one (51)\n2. Fifty-five (55)\n3. Forty-three (43)",
"What is 12 x 6?\n1. Seventy-two (72)\n2. Forty-eight (48)\n3. One hundred and twenty-four (124)"]





#This is a function that gets the index of the question
def get_question_index(lst):
	index_list = []
	for question in lst:
		index_num = lst.index(question)
		index_list.append(index_num)
	return index_list

#the variable below stores the list of index of the randomized questions
def randomize_index(index_list):
	random_index = sample(index_list, 10)
	return random_index



question_list = get_question_index(begineer_questions_maths)
questions = randomize_index(question_list)
# this is a function that picks the question based on the index returned by question_index variable
def ask_question(lst):
	global question_index
	final_question = questions[question_index]
	return lst[final_question]


#this function prints the math question, gets the user's answer and then matches them to check if correct or wrong
def get_user_answer_math():
	global score
	math_final_question = ask_question(begineer_questions_maths)
	print(math_final_question)
	sleep(0.2)
	user_answer = input("Please, select options 1, 2 & 3 only. Type in the correct number: ")
	user_answer = int(user_answer)
	print(user_answer)
	sleep(0.2)
	if (user_answer < 1 or user_answer > 3) or user_answer == "":
		print("Invalid option...Try again")
	else:
		if math_final_question == begineer_questions_maths[0] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[1] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[2] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[3] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[4] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[5] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[6] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[7] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[8] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[9] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[10] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[11] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[12] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[13] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[14] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[15] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[16] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[17] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[18] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[19] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[20] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[21] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[22] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[23] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[24] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[25] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[26] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[27] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif math_final_question == begineer_questions_maths[28] and user_answer == 1:
			print(congrats_msg)
			score += 10
		else:
			print(console_user)

#Thus function starts the math quizz section
def math_quizz():
	global score
	global question_index
	number_of_questions = 10

	print("Welcome to the math quizz.......")
	sleep(1)
	while number_of_questions > 0:
		get_user_answer_math()
		print()
		question_index += 1
		number_of_questions -= 1
    
	print("Calculating score.................")
	sleep(1.5)
	print("Your score: %s" % (str(score)))

#this are the biology questions
begineer_questions_biology = ["A dog is following the scent of a jackrabbit. Which of the following accurately describes\n how the dog's brain integrates information for smell?\n1. Chemoreceptors in the brain send impulses for smell in the nasal cavity\n2. Chemoreceptors cells in the nasal cavity send impulses to the approriate area of the brain\n3. Receptors originating in the nose send action potentials to the motor regions of the brain",
"Thrips are insects that feed on rose pollen. Scientist noted the Thrips population increased in the spring and decreased\ndramatically during the summer. The researchers hypothesized that food abundance was limiting the factor pf population. Which of the following types of data would be\nmost useful for scientist to collect at regular intervals on a designated test plot of rose plants ?\n1. Density of rose pollen produced(g/m ^ 2)\n2. Mean temperature(°C)\n3. Amount of pollen produced by each flower(g/flower)",
"if ATP breakdown(hydrolysis) is inbited, which of the following types of movement across cell membranes is also inhibited ?\n1. Movement of oxygen into a cell \n2. Facilitated diffusion of a premeable substance\n3. Passage of a solute against its concentration gradient",
"Which of the following questions is most relevant to understanding the Calvin cycle?\n1. How does chlorophyll capture light\n2. How is ATP used in the formation of 3-carbon carbohydrates\n3. How is ATP produced in chemíosmosis?",
"Rosalind Franklin's x-ray diffraction images taken in the 1950s most directly support which of the following claims about\nDNA?\n1.The two strands of DNA are antiparallel \n2. The ratios of base pairs are constant\n3. The basic molecular structure is a helix",
"What is the name of the bony framework that supports the body?\n1. Fermur\n2. Skeleton (70)\n3. Pivot",
"Which of the following best describes Biology?\n1. This is the study of animals and their behaviour\n2. This is the study of earth and its constituents\n3. This is the study of life and everything in it(i.e, Both plants, animal, unicellular organisms, etc.)",
"Ordinary table salt is sodium chloride. What is baking soda?\n1. Potassium carbonate\n2. Potassium hydroxide\n3. Sodium bicarbonate",
"Ozone hole refers to?\n1. Hole in ozone layer\n2. Increase in the thickness of ozone layer in troposphere\n3. Decrease in thickness of ozone layer in stratosphere",
"Pollination is best defined as?\n1. Transfer of pollen from anther to stigma\n2. Germination of pollen grains\n3. Growth of pollen tube in ovule",
"Plants receive their nutrients mainly from?\n1. Atmosphere\n2. Soil\n3. Light",
"Photosynthesis generally takes place in which parts of the plant?\n1. Leaf and other chloroplast bearing parts\n2. Stem and leaf\n3. Bark and leaf",
"Plants synthesis protein from?\n1. Amino acids\n2. Fatty acids\n3. Sugar",
"Out of 900 reported species of living gymnosperms, conifers are represented by about 500 species, About 2,50,000 species of\nangiosperms (flowering plants) have also been reported in the world. The vast and dominant woodlands in Europe, Asia, North America\nand mountains such as Himalayas are wooded with?\n1. Only conifers\n2. All gymnosperms, except conifers\n3. Angiosperms and all gymnosperms except conifers",
"One of the following is not a function of bones.?\n1. Protection of vital organs\n2. Secretion of hormones for calcium regulation in blood and bones\n3. Production of blood corpuscles",
"Photo-oxidation is?\n1. Photorespiration\n2. All of the above\n3. Photolysis",
"Process of cell division can take place by?\n1. Heterosis\n2.Fusion\n3. Mitosis",
"Most highly intelligent mammals are?\n1. Whales\n2. Kangaroos\n3. Dolphins",
"Plant development is influenced by?\n1. Quality and quantity of light\n2. Quality, quantity and duration of light\n3. Quality of light only",
"Prokaryotic cells lack?\n1. Nucleolus\n2. Nuclear membrane & membrane bound by organelles\n3. All of these",
"Photosynthesis takes place faster in?\n1. White light\n2. Yellow light\n3. Red light",
"Nucleus, the genetic material containing rounded body in each cell, was first discovered in 1831 by?\n1. Robert Hooke\n2. Theodore Schwann\n3. Robert Brown",
"Primary phloem develops from?\n1. Provascular tissue\n2. Lateral meristem\n3. Extrastelar cambium",
"Other than spreading malaria, anopheles mosquitoes are also vectors of?\n1. Encephalitis\n2. Filariasis\n3. Dengue fever",
"Plants that grow in saline water are called?\n1. Hydrophytes\n2. Halophytes\n3. Thallophytes",
"Pyorrhoea is a disease of the?\n1. Gums\n2. Nose\n3. Lungs",
"Placenta is the structure formed?\n1. By the union of foetal and uterine tissue\n2. By foetus only\n3. None of these)",
"Plants hormone that induces cell division is?\n1. Gibberellins\n2. Kinins\n3. Domins",
"Neurospora is used as genetic material because?\n1. The product of single meiosis can be easily analysed\n2. Meiotic products are linearly arranged in the form of ordered tetrads\n3. it has short life cycle of 10 days"]

#this function prints the biology question, gets the user's answer and then matches them to check if correct or wrong
def get_user_answer_biology():
	global score
	biology_final_question = ask_question(begineer_questions_biology)
	print(biology_final_question)
	sleep(0.2)
	user_answer = input("Please, select options 1, 2 & 3 only. Type in the correct number: ")
	user_answer = int(user_answer)
	print(user_answer)
	sleep(0.2)

	if (user_answer < 1 or user_answer > 3) or user_answer == "":
		print("Invalid option...Try again")
	else:
		if biology_final_question == begineer_questions_biology[0] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[1] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[2] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[3] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[4] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[5] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[6] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[7] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[8] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[9] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[10] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[11] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[12] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[13] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[14] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[15] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[16] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[17] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[18] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[19] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[20] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[21] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[22] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[23] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[24] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[25] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[26] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[27] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif biology_final_question == begineer_questions_biology[28] and user_answer == 3:
			print(congrats_msg)
			score += 10
		else:
			print(console_user)

#Thus function starts the biology quizz section
def biology_quizz():
	global score
	global question_index
	number_of_questions = 10

	print("Welcome to the biology quizz.......")
	sleep(1)
	while number_of_questions > 0:
		get_user_answer_biology()
		print()
		question_index += 1
		number_of_questions -= 1
    
	print("Calculating score...........")
	sleep(1.5)
	print("Your score: %s" % (str(score)))

#this are the geography questions
begineer_questions_geography = ["Which one of the following zones of the atmosphere is rich in Ozone gas?\n1. Troposphere\n2. Stratosphere\n3. Mesosphere",
"The mass of water vapour per unit volume of air is known as?\n1. Relative humidity\n2. Variable humidity\n3. Absolute humidity",
"Which one of the four regions above Earth has smallest height (Km)?\n1. Mesosphere\n2. Stratosphere\n3. Troposphere",
"The latitudinal differences in pressure delineate a number of major pressure zones, which correspond with?\n1. Zones of climate\n2. Zones of cyclonic depressions\n3. Zones of land",
"The great Victoria Desert is located in?\n1. Canada\n2. Australia\n3. West Africa",
"The intersecting lines drawn on maps and globes are?\n1. Geographic grids\n2. Longitudes\n3. Latitudes",
"The landmass of which of the following continents is the least?\n1. Africa\n2. Australia\n3. Europe",
"The habitats valuable for commercially harvested species are called?\n1. Coral reefs\n2. Hot spots\n3. Sea grass bed",
"Which of the following is tropical grassland?\n1. Prairies\n2. Savannah\n3. Taiga",
"The groundwater can become confined between two impermeable layers. This type of enclosed water is called?\n1. Unconfined groundwater\n2. Artesian well\n3. Artesian",
"The ionosphere includes?\n1. Thermosphere and exosphere\n2. Mesosphere\n3. Thermosphere, exosphere and mesosphere",
"The group of minerals chemically containing hydrocarbons is?\n1. Hydride group\n2. Silicate group\n3. Organic group",
"The least explosive type of volcano is called?\n1. Basalt plateau\n2. Composite volcanoes\n3. Shield volcanoes",
"The largest country of the world by geographical area is?\n1. USA\n2. Russia\n3. Australia",
"The infrared radiation by sun are strongly absorbed by?\n1. Water vapours\n2. Carbon dioxide\n3. Ozone",
"The latitude of a place expresses its angular position relative to the plane of?\n1. Axis of earth\n2. North pole\n3. Equator",
"The largest part of our hydrosphere is?\n1. Pacific ocean\n2. Atlantic Ocean\n3. Indian Ocean",
"The largest continent in the world is?\n1. Africa\n2. Asia\n3. Australia",
"The landforms that are created by massive earth movements due to place tectonics are called?\n1. Structural landforms\n2. Weathering landforms\n3. Depositional landforms",
"The latitude 'AA' on the map represents the?\n1. Tropic of Cancer\n2. Tropic of Capricorn\n3. Equator",
"The horizontal of soil profile is composed of?\n1. Unweathered bedrock\n2. Material affected by translocation & organic modification\n3. Weathered parent material that is not affected by translocation and organic modification",
"The largest gulf in the world is?\n1. Persian Gulf\n2. Gulf of Mexico\n3. Gulf of Carpentaria",
"The minor planets revolving between the orbits of Jupiter and Mars are called?\n1. Asteroids\n2. Meteors\n3. Comets",
"The luminous coloured ring, surrounding the sun is called the?\n1. Corona\n2. Nebula\n3. Comet",
"The longest ship canal in the world is the?\n1. St. Laurence Seaway (USA and Canada)\n2. Suez canal, Egypt\n3. Kiel canal, Germany",
"The meridian passing through London is called the?\n1. Equator\n2. Prime Meridian of 0º Meridian\n3. Tropic of Cancer",
"The most important factor that is affecting all the chemical weathering processes is?\n1. Vegetation\n2. Climate\n3. Topography",
"The most important force that provide resistance to particles towards entertainment is?\n1. Momentum\n2. Particle cohesive bonds\n3. Frictional resistance",
"The major cause of species extinction is?\n1. Extraction (including mining, fishing, logging)\n2. Development (human settlements, industry)\n3. Habitat loss and degradation"]

#this function prints the geography question, gets the user's answer and then matches them to check if correct or wrong
def get_user_answer_geography():
	global score
	geography_final_question = ask_question(begineer_questions_geography)
	print(geography_final_question)
	sleep(0.2)
	user_answer = input("Please, select options 1, 2 & 3 only. Type in the correct number: ")
	user_answer = int(user_answer)
	print(user_answer)
	sleep(0.2)

	if (user_answer < 1 or user_answer > 3) or user_answer == "":
		print("Invalid option...Try again")
	else:
		if geography_final_question == begineer_questions_geography[0] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[1] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[2] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[3] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[4] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[5] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[6] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[7] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[8] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[9] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[10] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[11] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[12] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[13] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[14] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[15] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[16] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[17] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[18] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[19] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[20] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[21] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[22] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[23] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[24] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[25] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[26] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[27] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif geography_final_question == begineer_questions_geography[28] and user_answer == 3:
			print(congrats_msg)
			score += 10
		else:
			print(console_user)

#Thus function starts the geography quizz section
def geography_quizz():
	global score
	global question_index
	number_of_questions = 10

	print("Welcome to the geography quizz.......")
	sleep(1)
	while number_of_questions > 0:
		get_user_answer_geography()
		print()
		question_index += 1
		number_of_questions -= 1
    
	print("Calculating score.............")
	sleep(1.5)
	print("Your score: %s" % (str(score)))

#this are the physics questions
begineer_questions_physics = ["Radiocarbon is produced in the atmosphere as a result of?\n1. Lightning discharge in atmosphere\n2. Action of solar radiations particularly cosmic rays on carbon dioxide present in the atmosphere\n3. Collision between fast neutrons and nitrogen nuclei present in the atmosphere",
"The absorption of ink by blotting paper involves?\n1. Viscosity of ink\n2. Siphon action\n3. Capillary action phenomenon",
"Nuclear sizes are expressed in a unit named?\n1. Fermi\n2. Tesla\n3. Angstrom",
"Light year is a unit of?\n1. Time\n2. Distance\n3. Light",
"Mirage is due to?\n1. Equal heating of different parts of the atmosphere\n2. Magnetic disturbances in the atmosphere\n3. Unequal heating of different parts of the atmosphere",
"Light from the Sun reaches us in nearly?\n1. 4 minutes\n2. 8 minutes\n3. 16 minutes",
"Stars appears to move from east to west because?\n1. The earth rotates from west to east\n2. The earth rotates from east to west\n3. The background of the stars moves from west to east",
"Pa(Pascal) is the unit for?\n1. Thrust\n2. Pressure\n3. Frequency",
"Metals are good conductors of electricity because?\n1. The atoms are lightly packed\n2. They have high melting point\n3. They contain free electrons",
"Let a thin capillary tube be replaced with another tube of insufficient length then, we find water?\n1. Will overflow\n2. Will not rise\n3. Change its meniscus",
"Out of the following pairs, choose the pair in which the physical quantities do not have identical dimension?\n1. Pressure and Young's modules\n2. Impulse and moment of force\n3. Planck's constant and Angular momentum",
"Pick out the scalar quantity?\n1. Pressure\n2. Force\n3. Acceleration",
"Rectifiers are used to convert?\n1. Alternating current to Direct current\n2. Direct current to Alternating current\n3. High voltage to Low voltage",
"Out of the following, which is not emitted by radioactive substance?\n1. Neutrons\n2. Electrons\n3. Alpha particles",
"Sound waves in air are?\n1. Transverse\n2. Longitudinal\n3. Electromagnetic",
"Magnetism at the centre of a bar magnet is?\n1. Zero\n2. Minimum\n3. Maximum",
"Of the following properties of a wave, the one that is independent of the other is its?\n1. Velocity\n2. Wavelength\n3. Amplitude",
"Lux is the SI unit of?\n1. Luminous efficiency\n2. Luminous intensity\n3. Intensity of illumination",
"Materials for rain-proof coats and tents owe their water-proof properties to?\n1. Viscosity\n2. Surface tension\n3. Elasticity",
"RADAR is used for?\n1. Detecting and locating the position of objects such as aeroplanes\n2. Locating submerged submarines\n3. Locating geostationary satellites",
"Sound of frequency below 20 Hz is called?\n1. Infrasonic\n2. Ultrasonic\n3. Supersonics",
"Suitable impurities are added to a semiconductor depending on its use. This is done in order to?\n1. Increase its life\n2. Increase its electrical conductivity\n3. Enable it to withstand higher voltages",
"Moment of inertia is?\n1. Vector\n2. Phasor\n3. Tensor",
"Of the following natural phenomena, tell which one known in Sanskrit as 'deer's thirst'?\n1. Rainbow\n2. Mirage\n3. Halo",
"Sound travels at the fastest speed in?\n1. Water\n2. Vacuum\n3. Steel",
"Light travels at the fastest speed in?\n1. Glass\n2. Vacuum\n3. Water",
"Light Emitting Diodes (LED) is used in fancy electronic devices such as toys emit?\n1. X-rays\n2. Ultraviolet light\n3. Visible light",
"Optical fibre works on the?\n1. Total internal reflection\n2. Scattering\n3. Interference",
"In which of the following industries is mica as a raw material?\n1. Glass and Pottery\n2. Iron and Steel\n3. Electrical"]

#this function prints the physics question, gets the user's answer and then matches them to check if correct or wrong
def get_user_answer_physics():
	global score
	physics_final_question = ask_question(begineer_questions_physics)
	print(physics_final_question)
	sleep(0.2)
	user_answer = input("Please, select options 1, 2 & 3 only. Type in the correct number: ")
	user_answer = int(user_answer)
	print(user_answer)
	sleep(0.2)

	if (user_answer < 1 or user_answer > 3) or user_answer == "":
		print("Invalid option...Try again")
	else:
		if physics_final_question == begineer_questions_physics[0] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[1] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[2] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[3] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[4] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[5] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[6] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[7] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[8] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[9] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[10] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[11] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[12] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[13] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[14] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[15] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[16] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[17] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_maths[18] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[19] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[20] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[21] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[22] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[23] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[24] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[25] and user_answer == 2:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[26] and user_answer == 3:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[27] and user_answer == 1:
			print(congrats_msg)
			score += 10
		elif physics_final_question == begineer_questions_physics[28] and user_answer == 3:
			print(congrats_msg)
			score += 10
		else:
			print(console_user)

#Thus function starts the physics quizz section
def physics_quizz():
	global score
	global question_index
	number_of_questions = 10

	print("Welcome to the physics quizz.......")
	sleep(1)
	while number_of_questions > 0:
		get_user_answer_physics()
		print()
		question_index += 1
		number_of_questions -= 1
    
	print("Calculating score..............")
	sleep(1.5)
	print("Your score: %s" % (str(score)))

#Thus function starts the game itself and directs the user to the room selected
def play_quizz():
	print("Available rooms are;\n1. Maths\n2. Biology\n3. Geography\n4. Physics")
	room_choice = int(input("Which Room do you choose: "))
	if room_choice <= 0 or room_choice > 4:
		print("Invalid room number")
	else:
		if room_choice == 1:
			sleep(0.5)
			math_quizz()
		elif room_choice == 2:
			sleep(0.5)
			biology_quizz()
		elif room_choice == 3:
			geography_quizz()
		elif room_choice == 4:
			physics_quizz()
		else:
			pass


play_quizz()