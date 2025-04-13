
sampleUnit = {
    "Name": "Intercessor Squad",
    "characteristics": {
      "M": "6\"",
      "T": "4",
      "SV": "3+",
      "W": "2",
      "LD": "6+",
      "OC": "2"
    },
    "Cost": "160",
    "ModelCount": 10,
    "Weapon": {
      "A":"5",
      "WS":"3+",
      "S":"4",
      "AP":"-1",
      "D":"1"
    }
  }





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

attackerModelCount = float(sampleUnit["ModelCount"])
attackerAttackCount = float(sampleUnit["Weapon"]["A"])
attackerwBSkill = sampleUnit["Weapon"]["WS"]
attackerStrength = float(sampleUnit["Weapon"]["S"])
attackerAP = float(sampleUnit["Weapon"]["AP"])
attackerDamage = float(sampleUnit["Weapon"]["D"])

defenderToughness = float(sampleUnit["characteristics"]["T"])
defenderArmorSave = sampleUnit["characteristics"]["SV"]
defenderWounds = float(sampleUnit["characteristics"]["W"])


defenderModelCount = float(sampleUnit["ModelCount"])
defenderModelCost = float(sampleUnit["Cost"])
defenderCostPerModel = defenderModelCost/defenderModelCount

totalDefenderWounds = defenderModelCount * defenderWounds
totalWoundsInflicted = 0
unsavedWounds = 0

result = 0
# Calculation goes as follows:
# 1. Number of models shooting with said weapon profile
attackerModelCount
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
print("WOUNDS INFLICTED", totalWoundsInflicted)
# 5. Saving throw against wounds:
unsavedWounds = totalWoundsInflicted * diceApprox[defenderArmorSave]
print("TOTAL WOUNDS INFLICTED", totalWoundsInflicted)
print("ARMOR SAVE ROLL",diceApprox[defenderArmorSave], defenderArmorSave)
#Not working as intended around here
print("UNSAVED WOUNDS", unsavedWounds) 
# 6. Subtract Wounds to determine models destroyed.
defenderWoundsLeft = float(totalDefenderWounds) - unsavedWounds

print("WOUNDS REMAINING:", defenderWoundsLeft)
if(defenderWoundsLeft > 0):
  remainingWhole = int(defenderWoundsLeft % defenderModelCount)
  remainingWounded = defenderWoundsLeft / defenderModelCount
  print("REMAINING WOUNDED MODELS:", remainingWounded )
  print("REMAINING WHOLE MODELS:", remainingWhole )
  

  defenderRemainingModels = defenderModelCount - remainingWhole
  print("POINTS OF DAMAGE LOST", defenderRemainingModels * defenderCostPerModel)


  