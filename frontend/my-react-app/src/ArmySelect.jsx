import { useEffect, useState } from "react";

import "./App.css";

function ArmySelect(props) {
  const [selectOptions, setSelectOptions] = useState(null);

  const handleChange = (selectedOption) => {
    props.setArmy(selectedOption);
  };
  const sortOptions = () => {
    setSelectOptions(
      props.options.map((cur) => {
        return <option value={cur.value}>{cur.label}</option>;
      })
    );
  };

  useEffect(() => {
    sortOptions();
  }, [props.options]);

  return (
    <div className="mb-3">
      <label htmlFor="floatingInput">{props.name}</label>

      <select
        className="form-select"
        onChange={(selectValue) => {
          handleChange(selectValue.target.value);
        }}
        aria-label="Default select example">
        {selectOptions}
      </select>
    </div>
  );
}

export default ArmySelect;
