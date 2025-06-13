import { useEffect, useState } from "react";

import "./App.css";

function Breakdown(props) {
  const [totalAttacks, setTotalAttacks] = useState(0.0);
  const [totalAttacksConnecting, setTotalAttacksConnecting] = useState(0.0);
  const [totalWoundsInflicted, setTotalWoundsInflicted] = useState(0.0);
  const [woundsSaved, setWoundsSaved] = useState(0.0);
  const [unsavedWounds, setUnsavedWounds] = useState(0.0);
  const [totalDefenderWounds, setTotalDefenderWounds] = useState(0.0);
  const [defenderWoundsLeft, setDefendersWoundsLeft] = useState(0.0);
  const [remainingWounded, setRemainingWounded] = useState(0.0);
  const [remainingWhole, setRemainingWhole] = useState(0.0);
  const [pointsLost, setPointsLost] = useState(0.0);

  const diceApprox = {
    "6+": 0.16,
    "5+": 0.33,
    "4+": 0.5,
    "3+": 0.66,
    "2+": 0.84,
    "1+": 1.0,
  };

  // Function to calculate wounds
  const calculateWounds = (totalAttacks, strength, toughness) => {
    let woundRollKey = "";

    if (strength >= 2 * toughness) {
      woundRollKey = "2+";
    } else if (strength > toughness) {
      woundRollKey = "3+";
    } else if (strength === toughness) {
      woundRollKey = "4+";
    } else if (strength * 2 <= toughness) {
      woundRollKey = "6+";
    } else if (strength < toughness) {
      woundRollKey = "5+";
    }

    const woundRoll = diceApprox[woundRollKey];
    return parseFloat(totalAttacks * woundRoll);
  };

  const calculations = (sampleUnit, sampleWeapon) => {
    console.log("CALCS", pointsLost);
    // Approximate dice roll success probabilities
    if ("characteristics" in sampleUnit) {
      // Sample usage with preloaded data (replace this with dynamic import or fetch as needed)
      const attackerModelCount = 5;
      const attackerAttackCount = parseFloat(sampleWeapon.A);
      const attackerwBSkill = sampleWeapon.WS;
      const attackerStrength = parseFloat(sampleWeapon.S);
      const attackerAP = parseFloat(sampleWeapon.AP);
      const attackerDamage = parseFloat(sampleWeapon.D);

      const defenderToughness = parseFloat(sampleUnit.characteristics.T);
      const defenderArmorSave = sampleUnit.characteristics.SV;
      const defenderWounds = parseFloat(sampleUnit.characteristics.W);
      const defenderModelCount = 5;
      const defenderModelCost = parseFloat(sampleUnit.Cost);
      const defenderCostPerModel = defenderModelCost / defenderModelCount;

      const totalDefenderWounds = defenderModelCount * defenderWounds;

      // Step-by-step calculation
      const totalAttacks = attackerModelCount * attackerAttackCount;

      const totalAttacksConnecting = parseFloat(
        totalAttacks * diceApprox[attackerwBSkill]
      );

      const totalWoundsInflicted = calculateWounds(
        totalAttacksConnecting,
        attackerStrength,
        defenderToughness
      );

      const armorSaveVal = parseFloat(defenderArmorSave[0]);
      const effectiveSave = parseFloat(armorSaveVal - attackerAP);
      const woundsSaved = parseFloat(
        totalWoundsInflicted * diceApprox[`${effectiveSave}+`]
      );
      const unsavedWounds = parseFloat(totalWoundsInflicted - woundsSaved);

      const defenderWoundsLeft = parseFloat(
        totalDefenderWounds - unsavedWounds
      );

      const remainingWhole = Math.floor(defenderWoundsLeft / defenderWounds);
      const remainingWounded =
        defenderWoundsLeft / (defenderModelCount * defenderWounds);

      const defenderRemainingModels = remainingWhole + remainingWounded;
      const pointsLost =
        defenderModelCount * defenderCostPerModel -
        defenderRemainingModels * defenderCostPerModel;
      console.log("POINTS OF DAMAGE LOST:", typeof pointsLost, pointsLost);
      console.log("CALCS", pointsLost.toFixed(2));

      if ((sampleUnit, sampleWeapon)) {
        if (pointsLost.toFixed(2) >= 0) {
          setTotalAttacks(totalAttacks);
          setTotalAttacksConnecting(totalAttacksConnecting);
          setTotalWoundsInflicted(totalWoundsInflicted.toFixed(2));
          setWoundsSaved(woundsSaved.toFixed(2));
          setUnsavedWounds(unsavedWounds.toFixed(2));
          setTotalDefenderWounds(totalDefenderWounds);
          setDefendersWoundsLeft(defenderWoundsLeft.toFixed(2));
          setRemainingWounded(remainingWounded.toFixed(2));
          setRemainingWhole(remainingWhole);
          setPointsLost(pointsLost.toFixed(2));
        }
      }
      return [sampleUnit, pointsLost.toFixed(2)];
    }
  };

  useEffect(() => {
    calculations(props.selectedForDetails, props.attackerWeapon);
  }, [props.selectedForDetails, props.attackerWeapon]);

  return (
    <div className="mb-3">
      <label htmlFor="floatingInput"></label>
      {props.selectedForDetails.Name ? (
        <div>
          <div>
            <h5 class="fw-bold">{props.selectedForDetails.Name}</h5>
          </div>
          <div>
            <label class="fw-bold">Total Attacks:</label>
            {totalAttacks}
          </div>
          <div>
            <label class="fw-bold">Attacks Connect:</label>
            {totalAttacksConnecting};
          </div>
          <div>
            <label class="fw-bold">Wounds Infliced:</label>
            {totalWoundsInflicted}
          </div>
          <div>
            <label class="fw-bold">Wounds Saved:</label>
            {woundsSaved}
          </div>
          <div>
            <label class="fw-bold">Unsaved Wounds:</label>
            {unsavedWounds};
          </div>
          <div>
            <label class="fw-bold">Defenders Wounds:</label>
            {totalDefenderWounds};
          </div>
          <div>
            <label class="fw-bold">Wounds Remaining:</label>
            {defenderWoundsLeft};
          </div>
          <div>
            <label class="fw-bold">Remaining wounded models:</label>
            {remainingWounded}
          </div>
          <div>
            <label class="fw-bold">Remaining whole models:</label>
            {remainingWhole}
          </div>
          <div>
            <label class="fw-bold">Points lost:</label> {pointsLost}
          </div>
        </div>
      ) : null}
      <button
        type="button"
        className="btn btn-primary"
        onClick={() => {
          console.log("Unit", props.selectedForDetails);
          console.log("Weapon", props.attackerWeapon);
        }}>
        Print State App
      </button>
    </div>
  );
}

export default Breakdown;
