import React from "react";
import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const predictCustomer = async (customer) => {
  const response = await API.post("/predict", customer);
  return response.data;
};

export default API;                                                                                     