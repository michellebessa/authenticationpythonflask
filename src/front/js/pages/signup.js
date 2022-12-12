import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";

export const Signup = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  return (
    <div>
      {" "}
      <div className="mb-3 row">
        <label for="staticEmail" className="col-sm-2 col-form-label">
          Email
        </label>
        <div className="col-sm-10">
          <input
            type="text"
            className="form-control"
            onChange={(e) => setEmail(e.target.value)}
            id="staticEmail"
          />
        </div>
      </div>
      <div className="mb-3 row">
        <label for="inputPassword" className="col-sm-2 col-form-label">
          Password
        </label>
        <div className="col-sm-10">
          <input
            type="password"
            className="form-control"
            onChange={(e) => setPassword(e.target.value)}
            id="inputPassword"
          />
        </div>
      </div>
    </div>
  );
};
