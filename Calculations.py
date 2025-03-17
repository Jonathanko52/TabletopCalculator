def calculateWounds(totalAttacks, strength, toughness):
  woundRoll = 0
  woundRollKey = "" 
  if(strength  * 2 >= toughness):
    woundRollKey = "2+"
  elif(strength > toughness):
    woundRollKey = "3+"
  elif(strength > toughness):
    woundRollKey = "3+"
  elif(strength == toughness):
    woundRollKey = "4+"
  elif(strength <= toughness *2):
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

attackerModelCount = 0
attackerAttackCount = 0
attackerwBSkill = ""
attackerStrength = 0
attackerAP = 0
attackerDamage = 0 

defenderToughness = 0
defenderArmorSave = ""
defenderWounds = 0
defenderModelCount = 0
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
# 3. Number of attacks connecting. Take the total number of attacks and multipliy it with the weapon/ballistic skill.
totalAttacksConnecting = totalAttacks * diceApprox[attackerwBSkill]
# 4. Number of attacks that wound.
totalWoundsInflicted = calculateWounds(totalAttacksConnecting, attackerStrength, defenderToughness)
# 5. Saving throw against wounds:
unsavedWounds = totalWoundsInflicted / diceApprox[defenderArmorSave]
# 6. Subtract Wounds to determine models destroyed.
defenderWoundsLeft = (totalDefenderWounds) - unsavedWounds
if(defenderWoundsLeft > 0):
  
modelsLeft




