import React from "react";
import {
  useState
} from "react";

import {
  predictCustomer
} from "../services/api";


const initialForm = {

  gender: "Male",

  SeniorCitizen: 0,

  Partner: "Yes",

  Dependents: "No",

  tenure: 12,

  PhoneService: "Yes",

  MultipleLines: "No",

  InternetService: "Fiber optic",

  OnlineSecurity: "No",

  OnlineBackup: "No",

  DeviceProtection: "No",

  TechSupport: "No",

  StreamingTV: "No",

  StreamingMovies: "No",

  Contract: "Month-to-month",

  PaperlessBilling: "Yes",

  PaymentMethod: "Electronic check",

  MonthlyCharges: 70,

  TotalCharges: 840

};


export default function Prediction() {


  const [form, setForm] =
    useState(initialForm);


  const [result, setResult] =
    useState(null);


  const [loading, setLoading] =
    useState(false);


  const [error, setError] =
    useState("");


  function update(name, value) {

    setForm(
      previous => ({

        ...previous,

        [name]:

          [
            "SeniorCitizen",
            "tenure",
            "MonthlyCharges",
            "TotalCharges"
          ].includes(name)

            ? Number(value)

            : value

      })
    );

  }


  async function submit(event) {

    event.preventDefault();

    setLoading(true);

    setError("");

    setResult(null);


    try {

      const data =
        await predictCustomer(form);

      setResult(data);

    }

    catch (err) {

      console.error(err);

      setError(

        err.response?.data?.detail ||

        "Could not connect to FastAPI. Make sure the backend is running."

      );

    }

    finally {

      setLoading(false);

    }

  }


  const probability =

    result?.churn_probability ??

    result?.probability ??

    0;


  return (

    <>

      <header className="page-header">

        <div>

          <p className="eyebrow">
            MACHINE LEARNING
          </p>

          <h2>
            Customer Churn Prediction
          </h2>

          <p className="muted">
            Enter customer information and request
            a prediction from the trained model.
          </p>

        </div>

      </header>


      <div className="prediction-layout">


        {/* FORM */}

        <form
          className="card prediction-form"
          onSubmit={submit}
        >


          <div className="form-section">

            <h3>
              Customer Profile
            </h3>


            <div className="form-grid">


              <Field label="Gender">

                <select
                  value={form.gender}
                  onChange={e =>
                    update(
                      "gender",
                      e.target.value
                    )
                  }
                >

                  <option>
                    Male
                  </option>

                  <option>
                    Female
                  </option>

                </select>

              </Field>


              <Field label="Senior Citizen">

                <select
                  value={form.SeniorCitizen}
                  onChange={e =>
                    update(
                      "SeniorCitizen",
                      e.target.value
                    )
                  }
                >

                  <option value="0">
                    No
                  </option>

                  <option value="1">
                    Yes
                  </option>

                </select>

              </Field>


              <Field label="Partner">

                <select
                  value={form.Partner}
                  onChange={e =>
                    update(
                      "Partner",
                      e.target.value
                    )
                  }
                >

                  <option>
                    Yes
                  </option>

                  <option>
                    No
                  </option>

                </select>

              </Field>


              <Field label="Dependents">

                <select
                  value={form.Dependents}
                  onChange={e =>
                    update(
                      "Dependents",
                      e.target.value
                    )
                  }
                >

                  <option>
                    Yes
                  </option>

                  <option>
                    No
                  </option>

                </select>

              </Field>


              <Field label="Tenure (months)">

                <input
                  type="number"
                  min="0"
                  max="72"
                  value={form.tenure}
                  onChange={e =>
                    update(
                      "tenure",
                      e.target.value
                    )
                  }
                />

              </Field>


              <Field label="Monthly Charges">

                <input
                  type="number"
                  min="0"
                  step="0.01"
                  value={form.MonthlyCharges}
                  onChange={e =>
                    update(
                      "MonthlyCharges",
                      e.target.value
                    )
                  }
                />

              </Field>


              <Field label="Total Charges">

                <input
                  type="number"
                  min="0"
                  step="0.01"
                  value={form.TotalCharges}
                  onChange={e =>
                    update(
                      "TotalCharges",
                      e.target.value
                    )
                  }
                />

              </Field>


            </div>

          </div>


          {/* SERVICES */}

          <div className="form-section">

            <h3>
              Services
            </h3>


            <div className="form-grid">


              <SelectField
                name="PhoneService"
                value={form.PhoneService}
                update={update}
                options={[
                  "Yes",
                  "No"
                ]}
              />


              <SelectField
                name="MultipleLines"
                value={form.MultipleLines}
                update={update}
                options={[
                  "Yes",
                  "No",
                  "No phone service"
                ]}
              />


              <SelectField
                name="InternetService"
                value={form.InternetService}
                update={update}
                options={[
                  "DSL",
                  "Fiber optic",
                  "No"
                ]}
              />


              <SelectField
                name="OnlineSecurity"
                value={form.OnlineSecurity}
                update={update}
                options={[
                  "Yes",
                  "No",
                  "No internet service"
                ]}
              />


              <SelectField
                name="OnlineBackup"
                value={form.OnlineBackup}
                update={update}
                options={[
                  "Yes",
                  "No",
                  "No internet service"
                ]}
              />


              <SelectField
                name="DeviceProtection"
                value={form.DeviceProtection}
                update={update}
                options={[
                  "Yes",
                  "No",
                  "No internet service"
                ]}
              />


              <SelectField
                name="TechSupport"
                value={form.TechSupport}
                update={update}
                options={[
                  "Yes",
                  "No",
                  "No internet service"
                ]}
              />


              <SelectField
                name="StreamingTV"
                value={form.StreamingTV}
                update={update}
                options={[
                  "Yes",
                  "No",
                  "No internet service"
                ]}
              />


              <SelectField
                name="StreamingMovies"
                value={form.StreamingMovies}
                update={update}
                options={[
                  "Yes",
                  "No",
                  "No internet service"
                ]}
              />


            </div>

          </div>


          {/* BILLING */}

          <div className="form-section">

            <h3>
              Billing
            </h3>


            <div className="form-grid">


              <SelectField
                name="Contract"
                value={form.Contract}
                update={update}
                options={[
                  "Month-to-month",
                  "One year",
                  "Two year"
                ]}
              />


              <SelectField
                name="PaperlessBilling"
                value={form.PaperlessBilling}
                update={update}
                options={[
                  "Yes",
                  "No"
                ]}
              />


              <SelectField
                name="PaymentMethod"
                value={form.PaymentMethod}
                update={update}
                options={[
                  "Electronic check",
                  "Mailed check",
                  "Bank transfer (automatic)",
                  "Credit card (automatic)"
                ]}
              />


            </div>

          </div>


          <button
            className="primary-btn submit-btn"
            disabled={loading}
          >

            {loading
              ? "Predicting..."
              : "Predict Churn Risk"
            }

          </button>


        </form>


        {/* RESULT */}

        <div className="card result-card">

          <p className="eyebrow">
            MODEL OUTPUT
          </p>


          {!result && !error && (

            <div className="empty-result">

              <div className="result-circle">
                AI
              </div>

              <h3>
                Ready for prediction
              </h3>

              <p>
                Submit customer information
                to receive the model output.
              </p>

            </div>

          )}


          {error && (

            <div className="error-box">
              {error}
            </div>

          )}


          {result && (

            <div className="prediction-result">

              <div className="result-circle large">

                {Math.round(
                  probability * 100
                )}%

              </div>


              <h3>

                {result.prediction ??
                  result.churn_prediction ??
                  "Prediction received"}

              </h3>


              <p>
                Estimated churn probability
              </p>


              <div className="probability-bar">

                <span
                  style={{
                    width:
                      `${Math.min(
                        100,
                        Math.max(
                          0,
                          probability * 100
                        )
                      )}%`
                  }}
                />

              </div>


              <small>

                Model probability is an
                estimate and should be
                interpreted alongside
                validation metrics.

              </small>

            </div>

          )}

        </div>

      </div>

    </>

  );

}


/* FIELD */

function Field({
  label,
  children
}) {

  return (

    <label className="field">

      <span>
        {label}
      </span>

      {children}

    </label>

  );

}


/* SELECT FIELD */

function SelectField({
  name,
  value,
  update,
  options
}) {

  return (

    <Field label={name}>

      <select
        value={value}
        onChange={e =>
          update(
            name,
            e.target.value
          )
        }
      >

        {options.map(
          option => (

            <option
              key={option}
            >
              {option}
            </option>

          )
        )}

      </select>

    </Field>

  );

}