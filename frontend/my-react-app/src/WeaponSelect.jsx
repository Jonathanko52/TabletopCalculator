import { useEffect, useState } from "react";

import "./App.css";

function WeaponSelect(props) {
  const [selectOptions, setSelectOptions] = useState(null);
  const [weaponStats, setWeaponStats] = useState({});

  const handleChange = (selectedOption) => {
    console.log(props.options[selectedOption]);
    setWeaponStats(props.options[selectedOption]);
    props.setAttackerWeapon(props.options[selectedOption]);
  };

  const sortOptions = () => {
    let index = -1;
    setSelectOptions(
      props.options.map((cur) => {
        index++;
        return <option value={index}>{cur.Name}</option>;
      })
    );
  };

  useEffect(() => {
    if (props.options) {
      console.log("USE EFFECT", props.options);
      sortOptions();
      setWeaponStats(props.options[0]);
      props.setAttackerWeapon(props.options[0]);
    }
  }, [props.options]);

  return (
    <div className="mb-3">
      {props ? (
        <>
          <label htmlFor="floatingInput">{props.name}</label>

          <select
            className="form-select"
            onChange={(selectValue) => {
              handleChange(selectValue.target.value);
            }}
            aria-label="Default select example">
            {selectOptions}
          </select>
          <label class="fw-bold">Weapon Name: </label>
          <label>{weaponStats.Name}</label>
          <br></br>
          <label class="fw-bold">Attacks: </label>
          <label>{weaponStats.A}</label>
          <br></br>
          <label class="fw-bold">Armor Piercing: </label>
          <label>{weaponStats.AP}</label>
          <br></br>
          <label class="fw-bold">Ballistic Skill: </label>
          <label>{weaponStats.BS}</label>
          <br></br>
          <label class="fw-bold">Damage: </label>
          <label>{weaponStats.D}</label>
          <br></br>
        </>
      ) : null}
    </div>
  );
}

export default WeaponSelect;
