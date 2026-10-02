import React from "react";
import axios from "axios";

const API = axios.create({
  baseURL: "https://customer-churn-project-otwi.onrender.com",
});

export const predictCustomer = async (customer) => {
  const response = await API.post("/predict", customer);
  return response.data;
};

export default API;                                                                                     