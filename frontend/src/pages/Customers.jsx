import React from "react";
const customers = [

  {
    id: "7590-VHVEG",
    contract: "Month-to-month",
    tenure: 1,
    charge: 29.85,
    churn: "Yes"
  },

  {
    id: "5575-GNVDE",
    contract: "One year",
    tenure: 34,
    charge: 56.95,
    churn: "No"
  },

  {
    id: "3668-QPYBK",
    contract: "Month-to-month",
    tenure: 2,
    charge: 53.85,
    churn: "Yes"
  },

  {
    id: "7795-CFOCW",
    contract: "One year",
    tenure: 45,
    charge: 42.30,
    churn: "No"
  },

  {
    id: "9237-HQITU",
    contract: "Month-to-month",
    tenure: 2,
    charge: 70.70,
    churn: "Yes"
  },

  {
    id: "9305-CDSKC",
    contract: "Month-to-month",
    tenure: 8,
    charge: 99.65,
    churn: "Yes"
  }

];


export default function Customers() {

  return (

    <>

      <header className="page-header">

        <div>

          <p className="eyebrow">
            CUSTOMER DATA
          </p>

          <h2>
            Customer Overview
          </h2>

          <p className="muted">
            Customer records from the
            Telco churn dataset.
          </p>

        </div>

      </header>


      <div className="card table-card">

        <div className="table-header">

          <h3>
            Customer Records
          </h3>

          <p>
            Example records for the
            dashboard interface.
          </p>

        </div>


        <div className="table-wrap">

          <table>

            <thead>

              <tr>

                <th>
                  Customer ID
                </th>

                <th>
                  Contract
                </th>

                <th>
                  Tenure
                </th>

                <th>
                  Monthly Charge
                </th>

                <th>
                  Churn
                </th>

              </tr>

            </thead>


            <tbody>

              {customers.map(
                customer => (

                  <tr
                    key={customer.id}
                  >

                    <td>
                      {customer.id}
                    </td>

                    <td>
                      {customer.contract}
                    </td>

                    <td>
                      {customer.tenure}
                      {" "}months
                    </td>

                    <td>
                      $
                      {customer.charge.toFixed(2)}
                    </td>

                    <td>

                      <span
                        className={
                          `badge ${
                            customer.churn === "Yes"
                              ? "danger"
                              : "success"
                          }`
                        }
                      >

                        {customer.churn}

                      </span>

                    </td>

                  </tr>

                )
              )}

            </tbody>

          </table>

        </div>

      </div>

    </>

  );

}