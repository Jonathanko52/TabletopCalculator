import React, { useState } from "react";

const CharacterForm = () => {
  const [formData, setFormData] = useState({
    name: "",
    cost: "",
    M: "",
    T: "",
    SV: "",
    W: "",
    LD: "",
    OC: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/api/characters/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        alert("Character created!");
        setFormData({
          name: "",
          cost: "",
          M: "",
          T: "",
          SV: "",
          W: "",
          LD: "",
          OC: "",
        });
      } else {
        alert("Error creating character");
        console.error(response);
      }
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      {Object.entries(formData).map(([key, value]) => (
        <div key={key}>
          <label className="block font-medium capitalize">{key}</label>
          <input
            type="text"
            name={key}
            value={value}
            onChange={handleChange}
            className="border p-2 w-full"
          />
        </div>
      ))}
      <button
        type="submit"
        className="bg-blue-500 text-white px-4 py-2 rounded">
        Create Character
      </button>
    </form>
  );
};

export default CharacterForm;
