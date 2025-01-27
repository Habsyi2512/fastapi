"use client";

import React, { useState } from "react";

export default function AddUserForm() {
  const [name, setName] = useState<string>("");
  const [age, setAge] = useState<string>("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/api/users/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name,
          age: Number(age),
        }),
      });
      if (!response.ok) {
        throw new Error("Something went wrong!");
      }
      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.error(error);
    }
    setName("");
    setAge("");
    alert("Data berhasil ditambahkan!");
  };
  return (
    <form onSubmit={handleSubmit} method="POST" className="space-y-2">
      <label className="block">
        Name:
        <input
          type="text"
          placeholder="Masukkan Nama"
          className="p-2 rounded border border-gray-300 focus:outline-none focus:ring focus:ring-blue-500 focus:border-blue-500"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <label className="block">
        Age:
        <input
          type="text"
          className="appearance-none p-2 rounded border border-gray-300 focus:outline-none focus:ring focus:ring-blue-500 focus:border-blue-500"
          value={age}
          placeholder="Masukkan Umur"
          onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
            const formattedValue = e.target.value.replace(/[^\d]/g, "");
            setAge(formattedValue);
          }}
        />
      </label>
      <button
        type="submit"
        className="bg-blue-500 px-4 text-white rounded hover:bg-blue-600 active:bg-blue-500 py-2"
      >
        submit
      </button>
    </form>
  );
}
