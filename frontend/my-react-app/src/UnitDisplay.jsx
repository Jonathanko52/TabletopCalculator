import { useEffect, useState } from "react";
import WeaponSelect from "./WeaponSelect";

import "./App.css";

function UnitDisplay(props) {
  let unit = props.unit;

  return (
    <div className="mb-3 text-start">
      <h5 className="box mt-3">Step 2: Your unit</h5>
      {unit ? (
        <>
          <label class="fw-bold">Unit Name: </label>
          <label>{unit.Name}</label>
          <br></br>
          <label class="fw-bold">Cost: </label>
          <label>{unit.Cost}</label>
          <br></br>
          <label class="fw-bold">Toughness: </label>
          <label>{unit.Cost}</label>
          <br></br>
          <label class="fw-bold">Wounds: </label>
          <label>{unit.Cost}</label>
          <br></br>
          <label class="fw-bold">Saving Throw: </label>
          <label>{unit.Cost}</label>
          <br></br>
          <WeaponSelect
            options={unit.Weapons}
            setAttackerWeapon={props.setAttackerWeapon}></WeaponSelect>
        </>
      ) : null}
    </div>
  );
}

export default UnitDisplay;
