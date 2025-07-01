import { useEffect, useState } from "react";

import "./App.css";

function Calculator(props) {
  const [topTen, setTopTen] = useState([]);

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

  const retieveArmyAndRunCalc = () => {
    let objKeys;
    import(`./../../../Data/${props.opposingArmy}.json`)
      .then((result) => {
        let calculatedValues = [];
        objKeys = Object.keys(result.default);
        objKeys.forEach((cur) => {
          calculatedValues.push(
            calculations(result.default[cur], props.attackerWeapon)
          );
        });
        return calculatedValues;
      })
      .then((result) => {
        return result.sort((a, b) => b[1] - a[1]);
      })
      .then((result) => {
        result = result.filter((cur) => {
          return cur != undefined;
        });
        setTopTen(result);
      })
      .catch((error) => {
        console.error("Error loading component:", error);
      });
  };

  const calculations = (sampleUnit, sampleWeapon) => {
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
      // console.log("TOTAL ATTACKS:", totalAttacks);

      const totalAttacksConnecting = parseFloat(
        totalAttacks * diceApprox[attackerwBSkill]
      );
      // console.log("ATTACKS CONNECTING:", totalAttacksConnecting);

      const totalWoundsInflicted = calculateWounds(
        totalAttacksConnecting,
        attackerStrength,
        defenderToughness
      );

      // Saving throw
      const armorSaveVal = parseFloat(defenderArmorSave[0]);
      const effectiveSave = parseFloat(armorSaveVal - attackerAP);
      const woundsSaved = parseFloat(
        totalWoundsInflicted * diceApprox[`${effectiveSave}+`]
      );
      const unsavedWounds = parseFloat(totalWoundsInflicted - woundsSaved);

      // Model casualties
      const defenderWoundsLeft = parseFloat(
        totalDefenderWounds - unsavedWounds
      );

      // if (defenderWoundsLeft > 0) {
      console.log("START----------");
      console.log("WOUNDS LEFT", defenderWoundsLeft);
      console.log("MODEL COUNT", defenderModelCount);
      console.log("DEFENDER WOUNDS", defenderWounds);
      const remainingWhole = Math.floor(defenderWoundsLeft / defenderWounds);
      const remainingWounded =
        defenderWoundsLeft / (defenderModelCount * defenderWounds);

      console.log("REMAINING WOUNDED MODELS:", remainingWounded.toFixed(2));
      console.log("REMAINING WHOLE MODELS:", remainingWhole);

      const defenderRemainingModels = remainingWhole + remainingWounded;
      const pointsLost =
        defenderModelCount * defenderCostPerModel -
        defenderRemainingModels * defenderCostPerModel;

      if ((sampleUnit, sampleWeapon)) {
        console.log(
          "COMPARING " + sampleUnit.Name + " AGAINST " + sampleWeapon.Name
        );
        console.log("POINTS LOST: " + pointsLost.toFixed(2));
      }
      return [sampleUnit, pointsLost.toFixed(2)];
    }
  };

  useEffect(() => {
    retieveArmyAndRunCalc();
  }, [props.opposingArmy, props.attackerWeapon]);

  return (
    <div
      className="mb-3 scrollable-div"
      style={{ maxHeight: "100vh", overflowY: "auto" }}>
      <label htmlFor="floatingInput"></label>
      {topTen.length >= 1
        ? topTen.map((cur) => {
            return (
              <div
                value={cur[0].Name}
                onClick={() => {
                  props.setSelectedForDetails(cur[0]);
                }}>
                <label class="fw-bold">{cur[0].Name}:</label>:
                <label>{cur[1]}</label>
              </div>
            );
          })
        : null}
      <button
        type="button"
        className="btn btn-primary"
        onClick={() => {
          console.log("Calculalator Props", props);
        }}>
        Print State App
      </button>
    </div>
  );
}

export default Calculator;
