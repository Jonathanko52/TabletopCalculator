import { useEffect, useState } from "react";
import WeaponSelect from "./WeaponSelect";

import "./App.css";

function UnitDisplay(props) {
  let unit = props.unit;
  console.log(props.unit);
  return (
    <div className="mb-3 text-start">
      <h5 className="box mt-3">Step 2: Your unit</h5>
      {unit ? (
        <>
          <label class="fw-bold">Unit Name: </label>
          <label>{unit.Name}</label>
          <br></br>
          <label class="fw-bold">Cost: </label>
          {unit ? <label>{unit.Cost}</label> : null}
          <br></br>
          <label class="fw-bold">Toughness: </label>
          {unit.characteristics ? (
            <label>{unit.characteristics.T}</label>
          ) : null}
          <br></br>
          <label class="fw-bold">Wounds: </label>
          {unit.characteristics ? (
            <label>{unit.characteristics.W}</label>
          ) : null}
          <br></br>
          <label class="fw-bold">Saving Throw: </label>
          {unit.characteristics ? (
            <label>{unit.characteristics.SV}</label>
          ) : null}
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
