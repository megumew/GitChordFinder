#4:5:6
def majorFreqs(baseFreq):
    ratio1 = baseFreq / 4
    frequencies.append(ratio1 * 5)
    frequencies.append(ratio1 * 6)
    print("\nMajor Chord: ")

#10:12:15
def minorFreqs(baseFreq):
    ratio1 = baseFreq / 10
    frequencies.append(ratio1 * 12)
    frequencies.append(ratio1 * 15)
    print("\nMinor Chord: ")

def genFreq(baseFreq, userType):
    ratio1 = baseFreq / chordTypes[userType]["baseRatio"]
    frequencies.append(ratio1 * chordTypes[userType]["middleRatio"])
    frequencies.append(ratio1 * chordTypes[userType]["TopRatio"])
    print("\n" + userType + " chord: ")

chordTypes = {
  "major":{
      "baseRatio":4,
      "middleRatio":5,
      "TopRatio":6
  } ,
  "minor":{
      "baseRatio":10,
      "middleRatio":12,
      "TopRatio":15
  }
}

print("Enter the number that corresponds with the chord you would like to generate.\n")
i = 1
for string in chordTypes:
    print(str(i) + ":\t" + string + " chord")
    i += 1
userType = input()
baseFreq = float(input("Enter base tone for chord:\t"))
frequencies = [baseFreq]
genFreq(baseFreq, userType)

print(frequencies)