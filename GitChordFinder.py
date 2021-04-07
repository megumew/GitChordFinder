def genFreq(baseFreq, userType):
    ratio1 = baseFreq / chordTypes[userType]["baseRatio"]
    frequencies.append(ratio1 * chordTypes[userType]["middleRatio"])
    frequencies.append(ratio1 * chordTypes[userType]["topRatio"])
    print("\n" + userType + " chord: ")

chordTypes = {
  "major":{
      "baseRatio":4.0,
      "middleRatio":5.0,
      "topRatio":6.0
  } ,
  "minor":{
      "baseRatio":10,
      "middleRatio":12.0,
      "topRatio":15.0
  },
  "diminished":{
      "baseRatio":160.0,
      "middleRatio":192.0,
      "topRatio":231.0 
      }
  
}

print("Enter the type of chord you would like to generate.\n")

i = 1
for string in chordTypes:
    print(str(i) + ":\t" + string + " chord")
    i += 1

reqInput = True 
while reqInput:
    userType = str.lower(input())
    if not userType in chordTypes:
        print("I'm sorry I could not find " + userType)
    else:
        reqInput = False
baseFreq = float(input("Enter root note in Hz for chord:\t"))
frequencies = [baseFreq]
genFreq(baseFreq, userType)

print(frequencies)

