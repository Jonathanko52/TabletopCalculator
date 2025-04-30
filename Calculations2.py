import json


# Modular approach

# codexName = "Orks"
# route = ('./Data/' + codexName + '.json')

# with open(route, 'r') as file:
#     data = json.load(file)

# Test Approach
with open('./data/Imperium - Adeptus Custodes.json', 'r') as file:
    data = json.load(file)

sampleUnit = data["Custodian Guard"]



def calculateWounds(totalAttacks, strength, toughness):
  woundRoll = 0
  woundRollKey = "" 
  if(strength  >=  2 * toughness):
    woundRollKey = "2+"
  elif(strength > toughness):
    woundRollKey = "3+"
  elif(strength == toughness):
    woundRollKey = "4+"
  elif(strength *2 <= toughness):
    woundRollKey = "6+"
  elif(strength < toughness):
    woundRollKey = "5+"
  woundRoll = diceApprox[woundRollKey]
  return totalAttacks * woundRoll


# Calculations:
# 6+ = 16%
# 5+ = 32%
# 4+ = 50%
# 3+ = 66%
# 2+ = 83%

# For this project, I've decided to use the percentage probability of a dice roll occuring over actually simulating
# the roll, as unit crunch does. 

# Table for directly translating warhammer +rolls into percentages. 6+ means 6 or higher on a die. 
# This is the probability of getting that roll.
diceApprox = { "6+":0.16, "5+": 0.33, "4+": 0.50, "3+": 0.66, "2+": 0.84, "1+": 1.0}

# attackerModelCount = float(sampleUnit["ModelCount"])
attackerModelCount = 5




attackerAttackCount = float(sampleUnit["Weapons"][0]["A"])
attackerwBSkill = sampleUnit["Weapons"][0]["WS"]
attackerStrength = float(sampleUnit["Weapons"][0]["S"])
attackerAP = float(sampleUnit["Weapons"][0]["AP"])
attackerDamage = float(sampleUnit["Weapons"][0]["D"])

defenderToughness = float(sampleUnit["characteristics"]["T"])
defenderArmorSave = sampleUnit["characteristics"]["SV"]
defenderWounds = float(sampleUnit["characteristics"]["W"])


# defenderModelCount = float(sampleUnit["ModelCount"])
defenderModelCount = 5
defenderModelCost = float(sampleUnit["Cost"])
defenderCostPerModel = defenderModelCost/defenderModelCount

totalDefenderWounds = defenderModelCount * defenderWounds
totalWoundsInflicted = 0
unsavedWounds = 0

result = 0
# Calculation goes as follows:
# 1. Number of models shooting with said weapon profile
# 2. Number of attacks per model shooting with this profile. 
# Multiply one by the other to get the total amount of attacks.
totalAttacks = attackerModelCount * attackerAttackCount
print("TOTAL ATTACKS", totalAttacks)
# 3. Number of attacks connecting. 
# Take the total number of attacks and multipliy it with the weapon/ballistic skill.
totalAttacksConnecting = float(totalAttacks) * diceApprox[attackerwBSkill]
print("ATTACKS CONNECTING", totalAttacksConnecting)
# 4. Number of attacks that wound.
totalWoundsInflicted = calculateWounds(totalAttacksConnecting, attackerStrength, defenderToughness)
print("WOUNDS INFLICTED", round(totalWoundsInflicted,2))
# 5. Saving throw against wounds:

armorSaveMinusAttackedAP = int(defenderArmorSave[0]) + int(-1 * attackerAP)
woundsSaved = totalWoundsInflicted * diceApprox[str(armorSaveMinusAttackedAP)+ "+"]
print("WOUNDS SAVED", totalWoundsInflicted * diceApprox[str(armorSaveMinusAttackedAP)+ "+"])
unsavedWounds = totalWoundsInflicted - woundsSaved
print("TOTAL WOUNDS INFLICTED", round(totalWoundsInflicted,2))
#Not working as intended around here
print("UNSAVED WOUNDS", round(unsavedWounds,2))
# 6. Subtract Wounds to determine models destroyed.
print("DEFENDER WOUNDS", totalDefenderWounds)
defenderWoundsLeft = float(totalDefenderWounds) - unsavedWounds

print("WOUNDS REMAINING:", round(defenderWoundsLeft,2))
if(defenderWoundsLeft > 0):
  remainingWhole = int(defenderWoundsLeft % defenderModelCount)
  remainingWounded = defenderWoundsLeft / defenderModelCount
  print("REMAINING WOUNDED MODELS:", round(remainingWounded ,2))
  print("REMAINING WHOLE MODELS:", remainingWhole )
  

  defenderRemainingModels = remainingWhole + round(remainingWounded ,2)
  print("POINTS OF DAMAGE LOST", (defenderModelCount *defenderCostPerModel) - (defenderRemainingModels * defenderCostPerModel))


  