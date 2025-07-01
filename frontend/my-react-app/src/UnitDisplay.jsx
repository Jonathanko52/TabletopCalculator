import WeaponSelect from "./WeaponSelect";
import { useEffect } from "react";

import "./App.css";

function UnitDisplay(props) {
  let unit = props.unit;

  // useEffect(() => {
  //   console.log(props.Weapons);
  // }, []);

  return (
    <div className="mb-3 text-start overflow-wrap: break-word">
      <h5 className="box mt-3">Step 2: Your unit</h5>
      {unit ? (
        <>
          <label class="fw-bold">
            Unit Name: <span></span>
          </label>
          <label>
            <span> </span>
            {unit.Name}
          </label>
          <br></br>
          <label class="fw-bold">
            Cost:<span></span>{" "}
          </label>
          {unit ? (
            <label>
              <span> </span>
              {unit.Cost}
            </label>
          ) : null}
          <br></br>
          <label class="fw-bold">
            Toughness: <span></span>
          </label>
          {unit.characteristics ? (
            <label>
              <span> </span>
              {unit.characteristics.T}
            </label>
          ) : null}
          <br></br>
          <label class="fw-bold">
            Wounds:<span></span>
          </label>
          {unit.characteristics ? (
            <label>
              <span> </span>
              {unit.characteristics.W}
            </label>
          ) : null}
          <br></br>
          <label class="fw-bold">
            Saving Throw:<span></span>
          </label>
          {unit.characteristics ? (
            <label>
              <span> </span>
              {unit.characteristics.SV}
            </label>
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
