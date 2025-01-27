"use client";

import React, { useState } from "react";

export default function AddUserForm() {
  const [name, setName] = useState<string>("");
  const [age, setAge] = useState<number>(0);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log({ name, age });
  };
  return (
    <form onSubmit={handleSubmit} className="space-y-2">
      <label className="block">
        Name:
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <label className="block">
        Age:
        <input
          type="text"
          className="appearance-none"
          value={age}
          pattern="\d*"
          placeholder="input age"
          onChange={(e) => setAge(Number(e.target.value))}
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
