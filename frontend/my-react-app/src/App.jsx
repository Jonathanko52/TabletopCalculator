import { useState, useEffect } from "react";
import "./App.css";
import ArmySelect from "./ArmySelect";
import UnitDisplay from "./UnitDisplay";

import axios from "axios";
import CharacterForm from "./form";
// import data from "./../../../Data/Imperium - Adeptus Custodes.json";
import data from "./../../../Data/Imperium - Adeptus Custodes.json";
import availableArmies from "./assets/availableArmies.json";
import Calculator from "./Calculator";
import Breakdown from "./Breakdown";

function App() {
  const [attackerArmy, setAttackerArmy] = useState("");
  const [defenderArmy, setDefenderArmy] = useState("");
  const [attackerUnit, setAttackerUnit] = useState([]);
  const [attackerUnitProfile, setAttackerUnitProfile] = useState([]);
  const [defenderUnit, setDefenderUnit] = useState([]);
  const [attackerArmyRoster, setAttackerArmyRoster] = useState([]);
  const [defenderArmyRoster, setDefenderArmyRoster] = useState([]);
  const [attackerWeapon, setAttackerWeapon] = useState({});
  const [selectedForDetails, setSelectedForDetails] = useState({});

  const retrieveAttackerUnits = () => {
    import(`./../../../Data/${attackerArmy}.json`)
      .then((result) => {
        let attackerUnits = Object.keys(result.default).map((cur) => {
          return { value: cur, label: cur };
        });
        setAttackerArmyRoster(attackerUnits);
      })
      .catch((error) => {
        console.error("Error loading component:", error);
      });
  };

  const retrieveDefenderUnits = () => {
    import(`./../../../Data/${defenderArmy}.json`)
      .then((result) => {
        let defenderUnits = Object.keys(result.default).map((cur) => {
          return { value: cur, label: cur };
        });
        setDefenderArmyRoster(defenderUnits);
      })
      .catch((error) => {
        console.error("Error loading component:", error);
      });
  };

  const retrieverAttackUnit = () => {
    import(`./../../../Data/${attackerArmy}.json`)
      .then((result) => {
        setAttackerUnitProfile(result.default[attackerUnit]);
      })
      .catch((error) => {
        console.error("Error loading component:", error);
      });
  };

  useEffect(() => {
    retrieveAttackerUnits();
    retrieveDefenderUnits();
  }, []);

  useEffect(() => {
    retrieveAttackerUnits();
  }, [attackerArmy]);

  useEffect(() => {
    retrieveDefenderUnits();
  }, [defenderArmy]);

  useEffect(() => {
    retrieverAttackUnit();
  }, [attackerUnit]);

  return (
    <div className="container-fluid py-5 h-100">
      <div className="row  h-25 mb-4 justify-content-center">
        <div className="col-9 h-50 border border-primary">
          <div className="box">Warhammer Tabletop Calculator</div>
        </div>
      </div>
      <div className="row justify-content-center h-75 g-3">
        <div className="col-2 m-4 border border-primary">
          <h5 className="box mt-3">Step 1: Pick units</h5>
          <ArmySelect
            name={"Select your faction"}
            setArmy={setAttackerArmy}
            options={availableArmies}
          />
          <ArmySelect
            name={"Select your unit"}
            setArmy={setAttackerUnit}
            options={attackerArmyRoster}
          />
          <ArmySelect
            name={"Select opponent's faction"}
            setArmy={setDefenderArmy}
            options={availableArmies}
          />
          <ArmySelect
            name={"Select opponent's unit"}
            setArmy={setDefenderUnit}
            options={defenderArmyRoster}
          />
        </div>
        <div className="col-2 m-4 border border-primary">
          <UnitDisplay
            unit={attackerUnitProfile}
            setAttackerWeapon={setAttackerWeapon}
          />
        </div>
        <div className="col-2 m-4 border border-primary">
          <Calculator
            setSelectedForDetails={setSelectedForDetails}
            opposingArmy={defenderArmy}
            attackerWeapon={attackerWeapon}
          />
        </div>
        <div className="col-2 m-4 border border-primary">
          <Breakdown
            selectedForDetails={selectedForDetails}
            attackerWeapon={attackerWeapon}
          />
        </div>
      </div>
    </div>
  );
}

export default App;
